"""
MindHaven AI - Interactive Terminal CLI
IS Professional Elective #4 - Gen AI Capstone Project

Dedicated 100% to Mental Health & Introvert Emotional Expression Counseling for College Students.
Allows running the entire capstone pipeline and chatting with the AI Counselor in your terminal.
"""

import os
import sys
import time
from pathlib import Path

# Safe Unicode output for Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.preprocessing import run_pipeline
from src.embedding_demo import SemanticSearchDemo
from src.vector_store import PineconeVectorStore
from src.metric_comparison import run_metric_benchmarks
from src.chat_completion_demo import MindHavenCounselor


def print_banner():
    print("=" * 80)
    print("   🌱 MindHaven AI — Mental Health & Introvert Emotional Companion 🌱")
    print("   Helping College Students & Introverts Access Feelings, CBT & Safety")
    print("   IS Capstone: Checkpoints 1 & 2 | Hugging Face + Pinecone Serverless")
    print("=" * 80)


def interactive_chat():
    counselor = MindHavenCounselor()
    print("\n--- MindHaven Emotional Companion & Counselor ---")
    print("Share what you are feeling, test somatic grounding, or express quiet thoughts.")
    print("Type 'exit' or 'back' to return to menu.")
    print("-" * 80)

    while True:
        try:
            user_input = input("\n[You] > ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "back", "quit", "q"]:
                break

            print("\n[Reflecting & Searching Clinical Wellness Knowledge...]")
            response = counselor.generate_response(user_input)

            if response["is_crisis"]:
                print("\n" + "!" * 80)
                print(response["response"])
                print("!" * 80)
            else:
                print(f"\n[Active Prompt: {response['system_prompt_used']} | Latency: {response['latency_ms']}ms]")
                if response["retrieved_sources"]:
                    sources = ", ".join([f"{s['title']} ({s['chunk_id']})" for s in response["retrieved_sources"]])
                    print(f"[Grounded Context: {sources}]")
                print(f"\n[MindHaven Companion]:\n{response['response']}")

        except (KeyboardInterrupt, EOFError):
            break


def interactive_vector_search():
    store = PineconeVectorStore.load()
    print("\n--- Pinecone Mental Health Vector Search Playground ---")
    print("Type an emotional query to inspect Top-K retrieved mental health chunks.")
    print("-" * 80)

    while True:
        try:
            query = input("\n[Search Query] (or 'back') > ").strip()
            if not query or query.lower() in ["back", "exit", "q"]:
                break

            print("\nSelect Distance Metric:")
            print("  1. Cosine Similarity (Default)")
            print("  2. Euclidean (L2) Distance")
            print("  3. Dot Product")
            metric_choice = input("Choice (1-3, press Enter for 1): ").strip()
            metric = "cosine" if metric_choice in ["1", ""] else ("euclidean" if metric_choice == "2" else "dot_product")

            results = store.query(query, top_k=3, metric=metric)
            print(f"\nTop-3 Pinecone Retrieval Results for \"{query}\" (Metric: {metric.upper()}):")
            print("-" * 80)
            for idx, r in enumerate(results, 1):
                print(f"Rank #{idx} | Score: {r['score']} | Chunk ID: {r['chunk_id']}")
                print(f"Title: {r['title']} [{r['category']}]")
                print(f"Text: \"{r['text'][:200]}...\"\n")

        except (KeyboardInterrupt, EOFError):
            break


def main_menu():
    while True:
        print_banner()
        print("\nSelect an action to run in terminal:")
        print("  [1] Chat with AI Emotional Companion (Introvert Feelings & CBT Support)")
        print("  [2] Query Pinecone Mental Health Vector Database")
        print("  [3] Run Text Preprocessing Pipeline (Clean 28 Mental Health Documents)")
        print("  [4] Run Hugging Face Embedding Demo & Cosine Search")
        print("  [5] Run Pinecone Distance Metric Benchmarks (Cosine vs Euclidean vs Dot Product)")
        print("  [6] Execute & Update all Jupyter Notebooks")
        print("  [0] Exit")
        print("-" * 80)

        choice = input("Enter choice (0-6): ").strip()

        if choice == "1":
            interactive_chat()
        elif choice == "2":
            interactive_vector_search()
        elif choice == "3":
            print("\nExecuting Mental Health Preprocessing Pipeline...")
            run_pipeline()
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            print("\nExecuting Hugging Face Embedding Demo...")
            search_demo = SemanticSearchDemo()
            results = search_demo.search("I feel emotionally numb and bottle up my feelings.", top_k=2)
            for r in results:
                print(f"-> Score: {r['score']} | {r['title']} [{r['category']}]\n   \"{r['snippet']}\"\n")
            input("\nPress Enter to return to menu...")
        elif choice == "5":
            print("\nRunning Pinecone Distance Metric Benchmark...")
            run_metric_benchmarks()
            input("\nPress Enter to return to menu...")
        elif choice == "6":
            print("\nExecuting all Jupyter Notebooks...")
            from scripts.execute_notebooks import main as run_nb
            run_nb()
            input("\nPress Enter to return to menu...")
        elif choice in ["0", "exit", "q"]:
            print("\nExiting MindHaven AI. Take care of yourself!\n")
            break
        else:
            print("\nInvalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
