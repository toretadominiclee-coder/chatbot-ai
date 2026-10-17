# Deliverable 5: Data Messiness & Preprocessing Engineering Reflection

**Project:** MindHaven AI — Gen AI Capstone Project  
**Checkpoint:** Checkpoint 1 — Foundation & Data Pipeline  
**Deliverable Type:** 1/2 Page Engineering Reflection (Mental Health & Emotional Expression Corpus)  

---

## 1. What Was Messy About the Raw Mental Health Data?

Processing authentic collegiate mental health circulars, clinical CBT toolkits, and student emotional guidance documents revealed complex structural and semantic data challenges:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   RAW MENTAL HEALTH TEXT CHALLENGES IDENTIFIED                         │
├──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│ 1. Administrative Noise  │ 2. Clinical Jargon Ambiguity│ 3. Multi-Step Worksheets      │
│ • [PAGE 1 OF 6 - CONFID] │ • RSD vs SAD vs DBT vs PMR  │ • 5-4-3-2-1 Sensory Methods   │
│ • *** UNCONTROLLED COPY  │ • TIPP Protocol Acronyms    │ • Granularity Emotion Wheels  │
│ • Border lines & Headers │ • FERPA / HIPAA Disclaimers │ • Sentence Starter Prompts    │
└──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

1. **Scanned Headers and Institutional Watermarks:** Clinical handouts from University Psychological Services contained repetitive headers (e.g., `*** UNCONTROLLED COPY WHEN PRINTED -- FOR STUDENT PEER COUNSELING ***`, `[CONFIDENTIAL - CLINICAL COUNSELOR HANDBOOK]`, `[PAGE 2 OF 5]`). Embedding these verbatim skewed vector centroids toward generic administrative metadata rather than emotional coping techniques.
2. **Tabular Emotion Wheels & Multi-Step Worksheets:** Clinical protocols like DBT TIPP skills, 5-4-3-2-1 grounding, and the Geneva Emotion Wheel were formatted with complex ASCII delimiters (`+---+---+`, `| Step 1 | Action |`). Standard tokenizers broke these into disjointed symbols, fragmenting the relationship between emotional triggers and coping steps.
3. **Sensitive Clinical & Acronym Density:** Heavy use of clinical abbreviations (`RSD`, `SAD`, `CBT`, `TIPP`, `PMR`, `ANTs`, `CAPS`, `SDAS`) risked subword token degradation without proper canonicalization.

---

## 2. How We Handled and Engineered Solutions

Our multi-stage pipeline in `src/preprocessing.py` resolved each challenge:

- **Stage 1 (Targeted Noise Removal):** Regular expressions stripped page headers, confidentiality watermarks, and divider lines (`^[=\-+*_]{3,}`) while preserving clinical instructions intact.
- **Stage 2 (Unicode & Typography Normalization):** Normalized curly quotes, typographic dashes, and bullet points (`•`, `*`, `-->`) into canonical Markdown `- ` format to ensure consistent tokenization.
- **Stage 3 (Worksheet & Table Flattening):** Converted ASCII tables into structured bullet points with explicit step-by-step markers (e.g., `* T - Temperature: Splash cold water... | Drops heart rate 10-25%`), preserving the semantic link between emotion intensity and physiological reset.
- **Stage 4 (Emotionally Cohesive Chunking):** Implemented section-aware chunking targeting **180 tokens with a 25-token sliding overlap**, ensuring therapeutic exercises (e.g., the complete 4-step CBT reframing workflow) remain intact in a single chunk rather than being split across boundaries.

---

## 3. Lessons Learned for Downstream RAG

1. **Emotional Context Preservation:** In mental health retrieval, fragmenting a coping exercise mid-sentence increases student anxiety. Overlapping chunk boundaries ensured complete, self-contained coping instructions.
2. **Text-Based Accessibility:** Introverted students in crisis strongly prefer text-based lifelines (like Crisis Text Line `HOME to 741741`). Explicitly structuring and indexing text-accessible resources proved essential for low-barrier student care.
