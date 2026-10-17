"""
MindHaven AI - Pinecone Distance Metric Comparison Harness
IS Professional Elective #4 - Gen AI Capstone Project (Checkpoint 2: Deliverable 9)

Conducts an empirical comparison of Cosine Similarity, Euclidean (L2) Distance,
and Dot Product similarity over the 100% Mental Health & Introvert Wellness corpus.
"""

import sys
import json
import time
import numpy as np
from pathlib import Path
from typing import List, Dict, Any

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Safe Unicode output for Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from src.vector_store import PineconeVectorStore


def run_metric_benchmarks():
    """Runs comparative evaluation across Cosine, Euclidean, and Dot Product on Mental Health dataset."""
    store = PineconeVectorStore.load()
    
    benchmark_queries = [
        {
            "id": "Q1",
            "query": "How do I access and journal about unexpressed emotions and emotional numbness?",
            "intent": "Emotional Expression & Journaling Lookup"
        },
        {
            "id": "Q2",
            "query": "I am experiencing severe classroom social anxiety, shaking voice, and fear of being spotlighted.",
            "intent": "Social Anxiety & Micro-Exposure Lookup"
        },
        {
            "id": "Q3",
            "query": "My dorm is loud and chaotic, I am suffering from severe sensory overload and introvert burnout.",
            "intent": "Sensory Overload & Solitude Sanctuary Lookup"
        },
        {
            "id": "Q4",
            "query": "I feel hopeless, alone, exhausted from living, and having thoughts of ending it all.",
            "intent": "Emergency Crisis Lifeline & Immediate Triage"
        }
    ]
    
    metrics = ["cosine", "euclidean", "dot_product"]
    results = {}
    
    print("=" * 80)
    print("MINDHAVEN AI - PINECONE DISTANCE METRIC COMPARISON EXPERIMENT")
    print("Evaluating Cosine vs. Euclidean (L2) vs. Dot Product on Mental Health Corpus")
    print("=" * 80)
    
    for bq in benchmark_queries:
        qid = bq["id"]
        qtext = bq["query"]
        results[qid] = {
            "query": qtext,
            "intent": bq["intent"],
            "metrics": {}
        }
        
        print(f"\n[{qid}] Query: \"{qtext}\"")
        print(f"Intent: {bq['intent']}")
        print("-" * 80)
        
        for m in metrics:
            start_t = time.perf_counter()
            top_results = store.query(qtext, top_k=3, metric=m)
            dur_ms = (time.perf_counter() - start_t) * 1000
            
            results[qid]["metrics"][m] = {
                "latency_ms": round(dur_ms, 4),
                "top_chunks": [
                    {
                        "rank": idx + 1,
                        "chunk_id": r["chunk_id"],
                        "title": r["title"],
                        "score": r["score"],
                        "snippet": r["text"][:120] + "..."
                    }
                    for idx, r in enumerate(top_results)
                ]
            }
            
            print(f"  Metric: {m.upper():<12} | Latency: {dur_ms:.3f}ms")
            for r in top_results:
                print(f"    -> Score: {r['score']:>8.5f} | ID: {r['chunk_id']:<10} | {r['title']} [{r['category']}]")
                
    return results


if __name__ == "__main__":
    run_metric_benchmarks()
