# Capstone Project Proposal: MindHaven AI
## AI-Driven Mental Health & Emotional Expression Companion for College Students (Special Focus on Introverts & Hidden Feelings)

**Course:** IS Professional Elective #4 — Generative AI Capstone  
**Academic Year:** 1st Sem, A.Y. 2026–2027  
**Checkpoint:** Checkpoint 1 — Foundation & Data Pipeline (Performance Task 1)  
**Authors:** Marjorie & Project Team  
**Theme:** Online Counseling with AI-Driven Support for College Schools (100% Mental Health & Emotional Expression)  

---

## 1. Executive Summary & Problem Statement

Higher education presents acute psychological hurdles that disproportionately impact introverted, introspective, and socially anxious students:

1. **The "Silent Suffering" & Emotional Bottling of Introverts:** Over 40% of college students identify as introverted or highly sensitive. In loud, hyper-social campus environments, introverted students frequently suppress internal distress, emotional numbness, and loneliness rather than seeking help. Fear of judgment, phone call anxiety, and the exhausting nature of social interaction create massive barriers to traditional counseling.
2. **Counseling Caseload Overload:** Campus Counseling and Psychological Services (CAPS) centers experience severe staffing constraints, with counselor-to-student ratios often exceeding **350:1**. Routine wait times of 3 to 6 weeks leave students stranded during high-stress periods (midterms, finals, roommate conflicts, transition shock).

**MindHaven AI** is a specialized, retrieval-augmented conversational AI companion engineered to provide low-barrier, emotionally safe mental health guidance. It acts as an empathetic emotional mirror—helping students **access, name, and express their internal feelings**, practice Cognitive Behavioral Therapy (CBT) thought reframing, de-escalate social/test anxiety, and access 24/7 crisis safety lifelines.

```
+-----------------------------------------------------------------------------------+
|                                  MINDHAVEN AI                                     |
|           AI Mental Health & Emotional Expression Companion for Introverts        |
+-----------------------------------------+-----------------------------------------+
|      PILLAR 1: EMOTIONAL ACCESS         |   PILLAR 2: SOMATIC & CBT RESILIENCE    |
+-----------------------------------------+-----------------------------------------+
| • Emotion Naming & Granularity Wheel    | • Test Anxiety & Classroom Panic De-esc.|
| • Guided Private Expressive Journaling  | • Somatic Grounding (4-7-8, TIPP Skills)|
| • Deconstructing Imposter Syndrome      | • Dormitory Overstimulation & Recharge  |
| • Loneliness vs. Restorative Solitude   | • Low-Barrier Digital CAPS Intake Guide |
| • Rejection Sensitivity (RSD) Coping    | • 24/7 Crisis Triage & 988 Escalation   |
+-----------------------------------------+-----------------------------------------+
```

---

## 2. Target Users & Stakeholder Ecosystem

| User Persona | Primary Emotional & Psychological Pain Points | MindHaven AI Value Proposition |
| :--- | :--- | :--- |
| **Introverted & Quiet Students** | Difficulty accessing and verbalizing unexpressed feelings, emotional bottling, social battery exhaustion. | Non-judgmental, private emotional sounding board with guided journaling prompts and emotion granularity wheels. |
| **Socially Anxious Students** | Intense fear of classroom participation, shaking voice when spotlighted, group project anxiety. | Graded micro-exposure ladders, CBT thought reframing to dismantle the "Spotlight Effect." |
| **Overstimulated Dorm Residents** | Severe sensory overload from loud communal living, inability to recharge, roommate friction. | Boundary-setting communication scripts and campus quiet sanctuary locator. |
| **Students in Acute Distress** | Hopelessness, severe depressive episodes, crisis overwhelm, fear of calling hotlines. | Instant zero-delay safety triaging providing 24/7 text-based resources (Crisis Text Line `HOME to 741741`, 988). |

---

## 3. Chosen Theme & Core Functional Pillars

### Pillar A: Accessing Hidden Feelings & Emotional Expression
- **Emotion Wheel Granularity:** Helps students transition from vague discomfort ("I feel terrible") to precise emotional labels (*overstimulated, neglected, grieving, anxious*).
- **Expressive Writing & Guided Prompts:** Provides structured sentence stems (e.g., *"What I wish I could say out loud right now is..."*) that bypass internal inhibition.
- **Normalizing Introvert Solitude:** Reframes introversion, deep listening, and quiet analytical strengths, distinguishing healthy restorative solitude from painful isolation.

### Pillar B: Somatic De-Escalation, CBT & Safety Triage
- **Somatic Nervous System Resets:** Real-time guided box breathing (4x4), 4-7-8 relaxing breath, and DBT TIPP temperature resets (cold water dive reflex) for acute panic.
- **Cognitive Restructuring:** Identifies and reframes cognitive distortions (catastrophizing, all-or-nothing thinking, mind reading, imposter syndrome).
- **Emergency Crisis Triaging:** 100% deterministic detection of self-harm or suicidal keywords, instantly displaying the **988 Suicide & Crisis Lifeline**, Crisis Text Line (`741741`), and campus emergency clinicians.

---

## 4. Dataset Sources & Collection Scope

The knowledge base comprises **28 authentic, domain-specific mental health and emotional wellness documents** stored in `data/raw/`:

```
data/raw/
├── Emotional Expression & Journaling (Docs 01, 27)
├── Social Anxiety & Classroom Coping (Docs 02, 07, 08, 23, 26)
├── Dorm Overstimulation & Solitude Recharge (Docs 03, 10, 14, 22)
├── CBT & Cognitive Reframing (Docs 04, 05, 12, 24)
├── Somatic Grounding & Stress Management (Docs 06, 09, 11, 13, 20)
├── Crisis Safety & Emergency Lifelines (Docs 15, 21, 28)
└── Therapy Intake & Self-Advocacy (Docs 16, 17, 18, 19, 25)
```

---

## 5. Success Criteria & Evaluation Metrics

### 1. Quantitative Technical Metrics
- **Retrieval Accuracy (Recall@3):** $\ge 90\%$ on diverse emotional expression and anxiety queries.
- **Retrieval Latency:** Sub-10ms query execution across the Pinecone serverless vector index.
- **Embedding Efficiency:** Hugging Face 384-dimensional dense vectors (`all-MiniLM-L6-v2`) for instant edge processing.
- **Safety Triaging Recall:** **100% recall** on crisis expressions with zero conversational drift or delay.

### 2. Qualitative & Ethical Guardrails
- **Empathetic, Safe Tone:** Unhurried, validating, and destigmatizing language.
- **Strict Non-Clinical Boundaries:** Always frames advice within psychoeducation and peer coping techniques; never prescribes medication or diagnoses disorders.
- **Low-Barrier Accessibility:** Provides text-based crisis contacts for students with severe phone call anxiety.
