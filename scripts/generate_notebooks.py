"""
Script to create clean, rich Jupyter Notebooks for Checkpoints 1 and 2
dedicated 100% to Mental Health & Introvert Emotional Expression Counseling
incorporating Hugging Face embeddings and Pinecone Vector Database.
"""

import json
from pathlib import Path

NOTEBOOKS_DIR = Path("notebooks")
NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------
# Notebook 1: Checkpoint 1 (Mental Health Preprocessing & HF Embeddings)
# -------------------------------------------------------------
nb1_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# MindHaven AI — Checkpoint 1: Mental Health & Emotional Expression Pipeline\n",
            "**Course:** IS Professional Elective #4 — Gen AI Capstone (1st Sem, A.Y. 2026–2027)\n",
            "**Theme:** AI-Driven Mental Health & Emotional Expression Companion for College Introverts\n",
            "**Embedding Architecture:** Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`)\n",
            "\n",
            "This notebook demonstrates:\n",
            "1. **Raw Document Ingestion** (28 authentic institutional mental health & introvert emotional guidance documents)\n",
            "2. **Multi-Stage Text Preprocessing** (Removing scanned headers, normalizing Unicode, flattening multi-step worksheets)\n",
            "3. **Before vs. After Transformations**\n",
            "4. **Semantic Chunking & Emotion Granularity Tags**\n",
            "5. **Hugging Face Dense Embedding Generation & Cosine Similarity Search Demo**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os\n",
            "import sys\n",
            "import json\n",
            "from pathlib import Path\n",
            "\n",
            "# Set working path\n",
            "ROOT_DIR = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()\n",
            "sys.path.insert(0, str(ROOT_DIR))\n",
            "\n",
            "from src.preprocessing import run_pipeline, TextCleaner\n",
            "from src.embedding_demo import HuggingFaceEmbeddingEngine, SemanticSearchDemo\n",
            "\n",
            "print(\"Mental Health preprocessing & Hugging Face embedding engines loaded successfully!\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 1. Raw Mental Health Document Inspection\n",
            "Let's inspect a raw introvert emotional expression document containing header noise and clinical worksheet formatting."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 2,
        "metadata": {},
        "outputs": [],
        "source": [
            "raw_sample_path = ROOT_DIR / 'data' / 'raw' / 'doc_01_introvert_emotional_expression_and_journaling.txt'\n",
            "with open(raw_sample_path, 'r', encoding='utf-8') as f:\n",
            "    raw_content = f.read()\n",
            "\n",
            "print(\"=== RAW DOCUMENT SAMPLE (First 500 characters) ===\")\n",
            "print(raw_content[:500])\n",
            "print(\"\\n... [Truncated] ...\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 2. Execute Preprocessing & Chunking Pipeline\n",
            "We now clean all 28 raw mental health documents into 39 standardized semantic chunks."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 3,
        "metadata": {},
        "outputs": [],
        "source": [
            "all_chunks, corpus_metadata, before_after_samples = run_pipeline()\n",
            "\n",
            "print(f\"\\nCorpus Statistics:\")\n",
            "print(f\"• Total Mental Health Documents: {corpus_metadata['total_documents']}\")\n",
            "print(f\"• Total Semantic Chunks: {corpus_metadata['total_chunks']}\")\n",
            "print(f\"• Raw Characters: {corpus_metadata['total_raw_characters']:,}\")\n",
            "print(f\"• Cleaned Characters: {corpus_metadata['total_cleaned_characters']:,}\")\n",
            "print(f\"• Noise Reduction: {corpus_metadata['average_reduction_percentage']}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 3. Before vs. After Transformation Analysis"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 4,
        "metadata": {},
        "outputs": [],
        "source": [
            "for sample in before_after_samples[:2]:\n",
            "    print(\"=\" * 80)\n",
            "    print(f\"DOCUMENT: {sample['title']} ({sample['doc_id']})\")\n",
            "    print(\"=\" * 80)\n",
            "    print(\"--- BEFORE (RAW) ---\")\n",
            "    print(sample['raw_sample'])\n",
            "    print(\"\\n--- AFTER (CLEANED) ---\")\n",
            "    print(sample['cleaned_sample'])\n",
            "    print(\"\\n--- TRANSFORMATIONS APPLIED ---\")\n",
            "    for change in sample['changes_applied']:\n",
            "        print(f\"  ✓ {change}\")\n",
            "    print(\"\\n\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 4. Hugging Face Dense Embedding Generation & Emotional Retrieval Demo\n",
            "We generate 384-dimensional dense vectors using Hugging Face and test retrieval on student emotional confessions and panic queries."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 5,
        "metadata": {},
        "outputs": [],
        "source": [
            "search_demo = SemanticSearchDemo()\n",
            "\n",
            "queries = [\n",
            "    (\"I feel emotionally numb and bottle up my feelings. How can I start expressing what I feel?\", \"Emotional Expression & Journaling\"),\n",
            "    (\"I get intense panic attacks when the professor calls on me in class and my voice shakes.\", \"Social Anxiety & Classroom Coping\")\n",
            "]\n",
            "\n",
            "for q, cat_filter in queries:\n",
            "    print(\"=\" * 80)\n",
            "    print(f\"QUERY: \\\"{q}\\\"\")\n",
            "    print(f\"CATEGORY: {cat_filter}\")\n",
            "    print(\"-\" * 80)\n",
            "    results = search_demo.search(q, top_k=2, category_filter=cat_filter)\n",
            "    for rank, r in enumerate(results, 1):\n",
            "        print(f\"[Rank #{rank}] Cosine Similarity: {r['score']} | Chunk: {r['chunk_id']}\")\n",
            "        print(f\"Source: {r['title']} [{r['category']}]\")\n",
            "        print(f\"Snippet: {r['snippet']}\\n\")"
        ]
    }
]

nb1 = {
    "cells": nb1_cells,
    "metadata": {
        "language_info": {"name": "python", "version": "3.14.0"},
        "orig_nbformat": 4
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(NOTEBOOKS_DIR / "01_data_preprocessing_and_embeddings.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb1, f, indent=2)


# -------------------------------------------------------------
# Notebook 2: Checkpoint 2 (Prompts & Pinecone Vector Database)
# -------------------------------------------------------------
nb2_cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# MindHaven AI — Checkpoint 2: Mental Health Prompts & Pinecone Indexing\n",
            "**Course:** IS Professional Elective #4 — Gen AI Capstone (1st Sem, A.Y. 2026–2027)\n",
            "**Theme:** AI-Driven Mental Health & Emotional Expression Companion for College Introverts\n",
            "**Vector Database:** Pinecone Serverless Index (`mindcampus-counseling`)\n",
            "\n",
            "This notebook demonstrates:\n",
            "1. **Pinecone Vector Database Setup & Ingestion** (39 mental health chunks)\n",
            "2. **Pinecone Distance Metric Comparison** (Cosine vs. Euclidean L2 vs. Dot Product)\n",
            "3. **Structured Mental Health Prompt Architecture** (Emotional Access, CBT Anxiety Reset, Crisis Triage)\n",
            "4. **Anti-Hallucination, Non-Clinical Boundaries & 988 Safety Escalation**"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os\n",
            "import sys\n",
            "import json\n",
            "from pathlib import Path\n",
            "\n",
            "ROOT_DIR = Path.cwd().parent if Path.cwd().name == 'notebooks' else Path.cwd()\n",
            "sys.path.insert(0, str(ROOT_DIR))\n",
            "\n",
            "from src.vector_store import PineconeVectorStore\n",
            "from src.chat_completion_demo import MindHavenCounselor, SYSTEM_PROMPTS\n",
            "from src.metric_comparison import run_metric_benchmarks\n",
            "\n",
            "print(\"Pinecone Vector Store & Mental Health Prompt modules loaded successfully!\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 1. Load Pinecone Mental Health Vector Database"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 2,
        "metadata": {},
        "outputs": [],
        "source": [
            "store = PineconeVectorStore.load()\n",
            "print(f\"Pinecone Index Name: {store.index_name}\")\n",
            "print(f\"Total Indexed Mental Health Chunks: {len(store.chunk_ids)}\")\n",
            "print(f\"Embedding Dimension: {store.embeddings.shape[1]}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 2. Empirical Distance Metric Comparison on Mental Health Corpus\n",
            "We evaluate Cosine Similarity, Euclidean Distance, and Dot Product on student emotional queries."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 3,
        "metadata": {},
        "outputs": [],
        "source": [
            "metric_results = run_metric_benchmarks()\n",
            "print(\"Pinecone Distance Metric evaluation complete!\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 3. End-to-End Chat Completion & Mental Health Safety Guardrail Demo\n",
            "We test the 3 production system prompts:\n",
            "1. **Prompt 1 (Emotional Expression Companion)**: Emotion naming and private journaling.\n",
            "2. **Prompt 2 (CBT & Somatic Anxiety Coach)**: Classroom social panic and 4-7-8 breathing.\n",
            "3. **Prompt 3 (Crisis Escalation)**: Immediate 0.0ms 988 Suicide & Crisis Lifeline intervention."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 4,
        "metadata": {},
        "outputs": [],
        "source": [
            "counselor = MindHavenCounselor()\n",
            "\n",
            "queries = [\n",
            "    \"I feel emotionally numb and bottle everything up inside. How do I start expressing what I feel?\",\n",
            "    \"I get intense panic attacks when the professor calls on me in class, my voice shakes and I freeze. What can I do?\",\n",
            "    \"I can't take this anymore, I feel hopeless and want to end my life.\"\n",
            "]\n",
            "\n",
            "for idx, q in enumerate(queries, 1):\n",
            "    print(\"=\" * 80)\n",
            "    print(f\"TEST CASE #{idx}: \\\"{q}\\\"\")\n",
            "    print(\"=\" * 80)\n",
            "    resp = counselor.generate_response(q)\n",
            "    print(f\"Active System Prompt: {resp['system_prompt_used']}\")\n",
            "    print(f\"Crisis Triaged: {resp['is_crisis']} | Latency: {resp['latency_ms']}ms\")\n",
            "    print(f\"\\nCounselor Response:\\n{resp['response']}\\n\")"
        ]
    }
]

nb2 = {
    "cells": nb2_cells,
    "metadata": {
        "language_info": {"name": "python", "version": "3.14.0"},
        "orig_nbformat": 4
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(NOTEBOOKS_DIR / "02_prompts_and_vector_indexing.ipynb", "w", encoding="utf-8") as f:
    json.dump(nb2, f, indent=2)

print("Created updated mental health notebooks in notebooks/!")
