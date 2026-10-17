# MindHaven AI — Mental Health & Emotional Expression Companion
> **IS Professional Elective #4 — Generative AI Capstone Project (A.Y. 2026–2027)**  
> **Theme:** 100% Mental Health & Emotional Wellness Counseling for College Students (Special Focus on Introverts & Accessing Feelings)  
> **Embeddings:** Hugging Face (`sentence-transformers/all-MiniLM-L6-v2`)  
> **Vector Database:** Pinecone Serverless Index (`mindcampus-counseling`)  
> **Checkpoints 1 & 2 Complete Implementation**

---

## 🌟 Executive Summary
**MindHaven AI** is an empathetic, retrieval-augmented conversational AI companion specifically tailored to support introverted, socially anxious, and quiet college students. It helps students navigate emotional bottlenecks (unexpressed feelings, classroom panic, dorm overstimulation, imposter syndrome, and loneliness) with evidence-based CBT reframing, somatic grounding, and 24/7 crisis safety triaging.

---

## 📂 Repository Architecture

```
Chatbot.ai/
├── README.md                                    # Root Capstone documentation
├── main.py                                      # All-in-One Interactive Terminal Console
├── requirements.txt                             # Python dependencies (Pinecone, Hugging Face, etc.)
│
├── deliverables/                                # Official Capstone Submission Documents
│   ├── 01_PROJECT_PROPOSAL.md                   # Checkpoint 1: 1–2 page Mental Health & Introvert Proposal
│   ├── 04_EMBEDDING_MODEL_SELECTION.md          # Checkpoint 1: Hugging Face model selection & rationale
│   ├── 05_DATA_REFLECTION.md                    # Checkpoint 1: 1/2 page data reflection on mental health text
│   ├── 06_PROMPT_ENGINEERING.md                 # Checkpoint 2: 3 structured emotional & crisis prompts
│   └── 09_DISTANCE_METRIC_COMPARISON.md         # Checkpoint 2: 1-page Pinecone metric comparison report
│
├── data/
│   ├── raw/                                     # Checkpoint 1: 28 authentic mental health & introvert documents (.txt)
│   │   ├── doc_01: Introvert Emotional Expression & Journaling
│   │   ├── doc_02: Social Anxiety & Classroom Participation Panic
│   │   ├── doc_03: Dorm Life Overstimulation & Solitude Recharge
│   │   ├── ... (28 Comprehensive Clinical Wellness Documents)
│   │   └── doc_28: 24/7 Emergency Mental Health & Text Crisis Directory
│   └── processed/                               # Cleaned, normalized, and embedded chunks
│       ├── processed_chunks.json                # 39 normalized semantic chunks with emotion tags
│       ├── embedded_chunks.json                 # 39 chunks with 384-D Hugging Face embeddings
│       ├── corpus_metadata.json                 # Preprocessing statistics
│       └── vector_index.json                    # Pinecone Vector Database snapshot
│
├── src/                                         # Core Python Engine
│   ├── __init__.py
│   ├── preprocessing.py                         # Multi-stage cleaning, regex noise removal, & chunker
│   ├── embedding_demo.py                        # Hugging Face 384-D dense embedding generator
│   ├── vector_store.py                          # Pinecone Serverless Vector Database integration
│   ├── chat_completion_demo.py                  # Grounded emotional companion & 988 safety triaging
│   └── metric_comparison.py                     # Pinecone metric evaluation script
│
├── notebooks/                                   # Interactive Jupyter Notebooks
│   ├── 01_data_preprocessing_and_embeddings.ipynb   # Checkpoint 1: Mental Health Pipeline & HF Embeddings
│   └── 02_prompts_and_vector_indexing.ipynb         # Checkpoint 2: Prompts & Pinecone Vector Store
│
├── scripts/
│   ├── generate_raw_data.py                     # Mental health raw document generator
│   ├── generate_notebooks.py                    # Jupyter notebook builder
│   └── execute_notebooks.py                     # Automated notebook runner & output populator
│
└── web_demo/                                    # Interactive Web Visualizer Application
    ├── index.html                               # Modern responsive UI
    ├── style.css                                # Dark mode glassmorphism styles
    └── app.js                                   # Client-side simulator, vector playground, & diff viewer
```

---

## 🚀 Quickstart: Run in Terminal

### 1. Launch All-in-One Interactive Console
```bash
python main.py
```

### 2. Standalone Verification Commands
```bash
python src/preprocessing.py        # Clean 28 mental health documents
python src/embedding_demo.py        # Generate Hugging Face embeddings & test queries
python src/vector_store.py          # Initialize & query Pinecone vector database
python src/metric_comparison.py     # Run Pinecone distance metric benchmarks
python src/chat_completion_demo.py  # Test emotional companion & 988 crisis guardrails
python scripts/execute_notebooks.py # Re-run and populate both Jupyter notebooks
```
