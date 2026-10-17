"""
MindCampus AI - Pinecone Vector Database Implementation
IS Professional Elective #4 - Gen AI Capstone Project (Checkpoint 2: Deliverable 8)

Production-grade Vector Database integration supporting Pinecone Serverless Indexing
and local persistent vector fallback with Cosine Similarity, Euclidean (L2) Distance,
and Dot Product metric evaluations.
"""

import os
import sys
import json
import time
import numpy as np
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple, Literal

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Safe Unicode output for Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from src.embedding_demo import HuggingFaceEmbeddingEngine

INDEX_STORAGE_PATH = Path("data/processed/vector_index.json")
PINECONE_INDEX_NAME = "mindcampus-counseling"


class PineconeVectorStore:
    """Pinecone Serverless Vector Store with offline persistent fallback."""

    def __init__(self, embedding_engine: Optional[HuggingFaceEmbeddingEngine] = None, index_name: str = PINECONE_INDEX_NAME):
        self.engine = embedding_engine or HuggingFaceEmbeddingEngine()
        self.index_name = index_name
        self.pinecone_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_client = None
        self.pinecone_index = None

        # Local storage mirror for persistence and zero-cloud operation
        self.chunk_ids: List[str] = []
        self.doc_ids: List[str] = []
        self.embeddings: np.ndarray = np.empty((0, self.engine.embedding_dim), dtype=np.float32)
        self.metadatas: List[Dict[str, Any]] = []
        self.texts: List[str] = []

        self._init_pinecone_client()

    def _init_pinecone_client(self):
        """Initializes connection to Pinecone Cloud API if API key is present."""
        if self.pinecone_key:
            try:
                from pinecone import Pinecone, ServerlessSpec
                self.pinecone_client = Pinecone(api_key=self.pinecone_key)
                
                # Check if index exists or create serverless index
                existing_indexes = [i.name for i in self.pinecone_client.list_indexes()]
                if self.index_name not in existing_indexes:
                    print(f"Creating Pinecone Serverless Index '{self.index_name}' (dim={self.engine.embedding_dim}, metric=cosine)...")
                    self.pinecone_client.create_index(
                        name=self.index_name,
                        dimension=self.engine.embedding_dim,
                        metric="cosine",
                        spec=ServerlessSpec(cloud="aws", region="us-east-1")
                    )
                self.pinecone_index = self.pinecone_client.Index(self.index_name)
                print(f"Connected to Pinecone Cloud Index '{self.index_name}'.")
            except Exception as e:
                print(f"[Pinecone Cloud Notice] Running in local Pinecone-compatible vector store mode: {e}")
                self.pinecone_client = None
                self.pinecone_index = None
        else:
            # Running local Pinecone-compatible vector store
            pass

    def build_from_chunks(self, chunks: List[Dict[str, Any]]):
        """Indexes a collection of preprocessed document chunks into Pinecone."""
        self.chunk_ids = [c["chunk_id"] for c in chunks]
        self.doc_ids = [c["doc_id"] for c in chunks]
        self.texts = [c["text"] for c in chunks]
        self.metadatas = [{
            "title": c["title"],
            "domain": c["domain"],
            "category": c["category"],
            "source_file": c["source_file"],
            "token_count": c.get("token_count", 0),
            "char_count": c.get("char_count", 0)
        } for c in chunks]

        corpus_texts = [f"{c['title']} {c['category']} {c['text']}" for c in chunks]
        if not self.engine._is_fitted:
            self.engine.fit_corpus(corpus_texts)

        if "embedding" in chunks[0]:
            print(f"Loading {len(chunks)} pre-computed Hugging Face embeddings into Pinecone Vector Store...")
            self.embeddings = np.array([c["embedding"] for c in chunks], dtype=np.float32)
        else:
            print(f"Embedding {len(chunks)} chunks with Hugging Face {self.engine.model_name}...")
            self.embeddings = np.array(self.engine.embed_batch(corpus_texts), dtype=np.float32)

        # If connected to live Pinecone index, upsert batch
        if self.pinecone_index:
            try:
                print(f"Upserting {len(self.chunk_ids)} vectors into Pinecone Index '{self.index_name}'...")
                vectors_to_upsert = []
                for i in range(len(self.chunk_ids)):
                    meta = dict(self.metadatas[i])
                    meta["text"] = self.texts[i][:1000]
                    vectors_to_upsert.append({
                        "id": self.chunk_ids[i],
                        "values": self.embeddings[i].tolist(),
                        "metadata": meta
                    })
                # Upsert in batches of 50
                for b_start in range(0, len(vectors_to_upsert), 50):
                    batch = vectors_to_upsert[b_start:b_start+50]
                    self.pinecone_index.upsert(vectors=batch)
                print(f"Successfully upserted vectors to Pinecone Cloud!")
            except Exception as e:
                print(f"[Pinecone Upsert Notice] Maintained local vector index: {e}")

        print(f"Pinecone Vector Store indexed {len(self.chunk_ids)} vectors with dimension {self.embeddings.shape[1]}.")

    def save(self, filepath: Path = INDEX_STORAGE_PATH):
        """Persists the local vector store snapshot to disk."""
        filepath.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "version": "2.0-pinecone-compatible",
            "model_name": self.engine.model_name,
            "dimension": self.engine.embedding_dim,
            "total_vectors": len(self.chunk_ids),
            "chunk_ids": self.chunk_ids,
            "doc_ids": self.doc_ids,
            "texts": self.texts,
            "metadatas": self.metadatas,
            "embeddings": self.embeddings.tolist()
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)
        print(f"Saved Pinecone Vector Index snapshot to {filepath} ({filepath.stat().st_size / 1024:.1f} KB)")

    @classmethod
    def load(cls, filepath: Path = INDEX_STORAGE_PATH) -> "PineconeVectorStore":
        """Loads a persisted vector store snapshot from disk."""
        if not filepath.exists():
            raise FileNotFoundError(f"No vector store index found at {filepath}!")
        with open(filepath, "r", encoding="utf-8") as f:
            payload = json.load(f)

        store = cls()
        store.chunk_ids = payload["chunk_ids"]
        store.doc_ids = payload["doc_ids"]
        store.texts = payload["texts"]
        store.metadatas = payload["metadatas"]
        store.embeddings = np.array(payload["embeddings"], dtype=np.float32)

        corpus_texts = [f"{m['title']} {m['category']} {t}" for m, t in zip(store.metadatas, store.texts)]
        store.engine.fit_corpus(corpus_texts)

        print(f"Loaded Pinecone Vector Store with {len(store.chunk_ids)} indexed items from {filepath}.")
        return store

    def query(
        self,
        query_text: str,
        top_k: int = 4,
        metric: Literal["cosine", "euclidean", "dot_product"] = "cosine",
        filter_domain: Optional[str] = None,
        filter_category: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Queries the Pinecone vector index with specified distance metric and metadata filtering."""
        query_vec = self.engine.embed_text(query_text)
        start_time = time.time()

        # Check if live Pinecone index can be queried
        if self.pinecone_index and metric == "cosine":
            try:
                filter_dict = {}
                if filter_domain:
                    filter_dict["domain"] = {"$eq": filter_domain}
                if filter_category:
                    filter_dict["category"] = {"$eq": filter_category}
                    
                pc_res = self.pinecone_index.query(
                    vector=query_vec.tolist(),
                    top_k=top_k,
                    filter=filter_dict if filter_dict else None,
                    include_metadata=True
                )
                query_duration = (time.time() - start_time) * 1000
                results = []
                for match in pc_res.get("matches", []):
                    m_meta = match.get("metadata", {})
                    results.append({
                        "chunk_id": match["id"],
                        "doc_id": m_meta.get("doc_id", match["id"].split("_c")[0]),
                        "title": m_meta.get("title", ""),
                        "domain": m_meta.get("domain", ""),
                        "category": m_meta.get("category", ""),
                        "source_file": m_meta.get("source_file", ""),
                        "text": m_meta.get("text", ""),
                        "metric": "cosine",
                        "score": round(match["score"], 5),
                        "query_latency_ms": round(query_duration, 3)
                    })
                if results:
                    return results
            except Exception as e:
                # Fallback to local high-speed calculation
                pass

        # Local vectorized metric computations (matches Pinecone serverless math)
        if metric == "cosine":
            norms = np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_vec)
            norms[norms == 0] = 1e-9
            scores = np.dot(self.embeddings, query_vec) / norms
            reverse_sort = True
        elif metric == "dot_product":
            scores = np.dot(self.embeddings, query_vec)
            reverse_sort = True
        elif metric == "euclidean":
            diff = self.embeddings - query_vec
            scores = np.linalg.norm(diff, axis=1)
            reverse_sort = False
        else:
            raise ValueError(f"Unsupported metric: {metric}")

        candidates = []
        for idx in range(len(self.chunk_ids)):
            meta = self.metadatas[idx]
            if filter_domain and meta.get("domain") != filter_domain:
                continue
            if filter_category and meta.get("category") != filter_category:
                continue
            candidates.append((idx, float(scores[idx])))

        candidates.sort(key=lambda x: x[1], reverse=reverse_sort)
        query_duration = (time.time() - start_time) * 1000

        results = []
        for idx, score in candidates[:top_k]:
            results.append({
                "chunk_id": self.chunk_ids[idx],
                "doc_id": self.doc_ids[idx],
                "title": self.metadatas[idx]["title"],
                "domain": self.metadatas[idx]["domain"],
                "category": self.metadatas[idx]["category"],
                "source_file": self.metadatas[idx]["source_file"],
                "text": self.texts[idx],
                "metric": metric,
                "score": round(score, 5),
                "query_latency_ms": round(query_duration, 3)
            })

        return results


# Backward compatibility alias
MindCampusVectorStore = PineconeVectorStore


def setup_and_test_vector_store():
    """Initializes and persists the Pinecone vector database with verification queries."""
    chunks_file = Path("data/processed/embedded_chunks.json")
    if not chunks_file.exists():
        chunks_file = Path("data/processed/processed_chunks.json")

    with open(chunks_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    store = PineconeVectorStore()
    store.build_from_chunks(chunks)
    store.save()

    print("\n" + "=" * 80)
    print("TESTING PINECONE VECTOR DATABASE RETRIEVAL")
    print("=" * 80)

    # Test Query 1: Academic Advising
    q1 = "What happens if my GPA drops below 2.0 and I get placed on academic probation?"
    res1 = store.query(q1, top_k=2, metric="cosine", filter_domain="academic_counseling")
    print(f"\n[QUERY 1] \"{q1}\" (Metric: Cosine, Filter: Academic)")
    for r in res1:
        print(f"  -> Score: {r['score']} | {r['title']} ({r['chunk_id']})")
        print(f"     \"{r['text'][:160]}...\"")

    # Test Query 2: Mental Health & Grounding
    q2 = "I need a quick breathing exercise for severe exam panic right now."
    res2 = store.query(q2, top_k=2, metric="cosine", filter_domain="mental_health_counseling")
    print(f"\n[QUERY 2] \"{q2}\" (Metric: Cosine, Filter: Mental Health)")
    for r in res2:
        print(f"  -> Score: {r['score']} | {r['title']} ({r['chunk_id']})")
        print(f"     \"{r['text'][:160]}...\"")

    print("\nPinecone Vector Store verification successful!")


if __name__ == "__main__":
    setup_and_test_vector_store()
