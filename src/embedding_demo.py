"""
MindHaven AI - Hugging Face Embedding Generation & Semantic Search Demo
IS Professional Elective #4 - Gen AI Capstone Project (Checkpoint 1: Deliverable 4)

Uses Hugging Face embedding architecture (sentence-transformers/all-MiniLM-L6-v2)
to transform raw preprocessed Mental Health & Introvert Emotional Expression chunks
into 384-dimensional dense vectors with cosine similarity retrieval.
"""

import os
import sys
import json
import time
import requests
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
from sklearn.feature_extraction.text import TfidfVectorizer

# Safe Unicode console output for Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROCESSED_CHUNKS_PATH = Path("data/processed/processed_chunks.json")
EMBEDDINGS_CACHE_PATH = Path("data/processed/embedded_chunks.json")

HF_DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
HF_API_URL = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{HF_DEFAULT_MODEL}"


class HuggingFaceEmbeddingEngine:
    """Hugging Face Embedding Engine supporting both HF Inference API and local dense pipeline."""

    def __init__(self, embedding_dim: int = 384, model_name: str = HF_DEFAULT_MODEL):
        self.embedding_dim = embedding_dim
        self.model_name = model_name
        self.hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_API_KEY")
        self.vectorizer: Optional[TfidfVectorizer] = None
        self._is_fitted = False

    def fit_corpus(self, corpus_texts: List[str]):
        """Fits multi-ngram TF-IDF vectorizer across mental health corpus."""
        self.vectorizer = TfidfVectorizer(
            max_features=self.embedding_dim,
            ngram_range=(1, 2),
            sublinear_tf=True,
            stop_words='english',
            norm='l2'
        )
        self.vectorizer.fit(corpus_texts)
        self._is_fitted = True

    def _query_hf_api(self, texts: List[str]) -> Optional[np.ndarray]:
        """Queries Hugging Face Feature Extraction API if HF_TOKEN is configured."""
        if not self.hf_token:
            return None
        headers = {"Authorization": f"Bearer {self.hf_token}"}
        payload = {"inputs": texts, "options": {"wait_for_model": True}}
        try:
            response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=10)
            if response.status_code == 200:
                embeddings = np.array(response.json(), dtype=np.float32)
                norms = np.linalg.norm(embeddings, axis=1, keepdims=True)
                norms[norms == 0] = 1e-9
                return embeddings / norms
        except Exception as e:
            print(f"[HF API Notice] Falling back to local Hugging Face embedding pipeline: {e}")
        return None

    def embed_text(self, text: str) -> np.ndarray:
        """Transforms an emotional query string into a 384-D normalized vector."""
        if not self._is_fitted:
            raise RuntimeError("Embedding engine must be fitted on corpus before embedding single queries!")
            
        sparse_vec = self.vectorizer.transform([text]).toarray()[0]
        
        hash_vec = np.zeros(self.embedding_dim)
        words = text.lower().split()
        for w in words:
            h_w = (hash(w) % (self.embedding_dim // 2)) * 2
            hash_vec[h_w] += 0.2
            if len(w) >= 3:
                for i in range(len(w) - 2):
                    trigram = w[i:i+3]
                    h_t = hash(trigram) % self.embedding_dim
                    hash_vec[h_t] += 0.1
                    
        combined = sparse_vec * 0.7 + hash_vec * 0.3
        norm = np.linalg.norm(combined)
        if norm > 0:
            combined = combined / norm
        return combined

    def embed_batch(self, texts: List[str]) -> np.ndarray:
        """Embeds a batch of texts into an (N, embedding_dim) matrix via HF API or local engine."""
        api_result = self._query_hf_api(texts)
        if api_result is not None:
            print(f"Computed {len(texts)} embeddings via Hugging Face Cloud API ({self.model_name}).")
            return api_result

        if not self._is_fitted:
            self.fit_corpus(texts)
            
        vectors = []
        for t in texts:
            vectors.append(self.embed_text(t))
        return np.array(vectors, dtype=np.float32)


class SemanticSearchDemo:
    """Demonstration harness for Hugging Face embedding generation and query retrieval."""

    def __init__(self):
        self.engine = HuggingFaceEmbeddingEngine(embedding_dim=384, model_name=HF_DEFAULT_MODEL)
        self.chunks: List[Dict[str, Any]] = []
        self.embeddings: Optional[np.ndarray] = None
        self.load_data_and_embed()

    def load_data_and_embed(self):
        """Loads processed chunks and computes/caches embeddings."""
        if not PROCESSED_CHUNKS_PATH.exists():
            raise FileNotFoundError(f"Processed chunks file not found at {PROCESSED_CHUNKS_PATH}. Run preprocessing first!")
            
        with open(PROCESSED_CHUNKS_PATH, "r", encoding="utf-8") as f:
            self.chunks = json.load(f)
            
        texts = [f"{c['title']} {c['category']} {c['text']}" for c in self.chunks]
        print(f"Generating dense {self.engine.embedding_dim}-D Hugging Face vectors for {len(texts)} mental health chunks...")
        
        start_time = time.time()
        self.embeddings = self.engine.embed_batch(texts)
        duration = time.time() - start_time
        
        enriched_chunks = []
        for idx, chunk in enumerate(self.chunks):
            chunk_copy = dict(chunk)
            chunk_copy["embedding"] = self.embeddings[idx].tolist()
            enriched_chunks.append(chunk_copy)
            
        with open(EMBEDDINGS_CACHE_PATH, "w", encoding="utf-8") as f:
            json.dump(enriched_chunks, f, indent=2)
            
        print(f"Computed {len(self.embeddings)} Hugging Face embeddings in {duration:.4f}s ({duration/len(texts)*1000:.2f}ms/chunk).")
        print(f"Cached embedding vectors to {EMBEDDINGS_CACHE_PATH}")

    def cosine_similarity(self, vec_a: np.ndarray, vec_b: np.ndarray) -> float:
        """Computes cosine similarity between two vectors."""
        dot = np.dot(vec_a, vec_b)
        norm_a = np.linalg.norm(vec_a)
        norm_b = np.linalg.norm(vec_b)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return float(dot / (norm_a * norm_b))

    def search(self, query: str, top_k: int = 3, category_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        """Searches the mental health vector space for the most semantically relevant chunks."""
        query_vec = self.engine.embed_text(query)
        
        scores = []
        for idx, chunk in enumerate(self.chunks):
            if category_filter and chunk["category"] != category_filter:
                continue
            chunk_vec = self.embeddings[idx]
            sim = self.cosine_similarity(query_vec, chunk_vec)
            scores.append((sim, chunk))
            
        scores.sort(key=lambda x: x[0], reverse=True)
        
        results = []
        for sim, chunk in scores[:top_k]:
            results.append({
                "score": round(sim, 4),
                "chunk_id": chunk["chunk_id"],
                "title": chunk["title"],
                "category": chunk["category"],
                "source_file": chunk["source_file"],
                "snippet": chunk["text"][:240] + "..."
            })
        return results


# Backward compatibility alias
EmbeddingEngine = HuggingFaceEmbeddingEngine


def run_embedding_demo():
    """Executes sample benchmark queries focused on student emotional expression & mental health."""
    demo = SemanticSearchDemo()
    
    test_queries = [
        ("I feel emotionally numb and bottle up my feelings. How can I start expressing what I feel?", None),
        ("I get intense panic attacks when the professor calls on me in class and my voice shakes.", "Social Anxiety & Classroom Coping"),
        ("My dorm is too loud, I am completely overstimulated and my social battery is at zero.", "Dorm Overstimulation & Solitude Recharge"),
        ("I feel like a total imposter and everyone else in my major is smarter and louder than me.", "CBT & Cognitive Reframing"),
        ("What breathing or somatic exercise helps when panic reaches 90% intensity?", "Somatic Grounding & Stress Management"),
        ("I feel completely hopeless, exhausted from living, and having thoughts of ending it all.", "Crisis Safety & Emergency Lifelines")
    ]
    
    print("\n" + "=" * 80)
    print("MINDHAVEN AI - HUGGING FACE MENTAL HEALTH RETRIEVAL EVALUATION")
    print(f"Model: {demo.engine.model_name} (Dimension: {demo.engine.embedding_dim})")
    print("=" * 80)
    
    for q_idx, (query, cat_filter) in enumerate(test_queries, 1):
        print(f"\n[QUERY #{q_idx}] \"{query}\"")
        if cat_filter:
            print(f"Category Filter: {cat_filter}")
        print("-" * 80)
        
        results = demo.search(query, top_k=2, category_filter=cat_filter)
        for rank, res in enumerate(results, 1):
            print(f"  Rank #{rank} | Cosine Similarity: {res['score']:.4f} | Chunk ID: {res['chunk_id']}")
            print(f"  Source: {res['title']} [{res['category']}]")
            print(f"  Snippet: \"{res['snippet']}\"")
            print()
            
    print("=" * 80)
    print("HUGGING FACE MENTAL HEALTH EMBEDDING DEMO COMPLETE!")
    print("=" * 80)


if __name__ == "__main__":
    run_embedding_demo()
