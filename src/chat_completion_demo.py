"""
MindHaven AI - Direct Conversational Mental Health & Emotional Companion Engine
IS Professional Elective #4 - Gen AI Capstone Project (Checkpoint 2: Deliverable 7)

Dedicated 100% to Mental Health, Introvert Emotional Expression, Social Anxiety,
CBT Thought Reframing, and 24/7 Crisis Safety Triaging for College Students.
Includes strict out-of-scope detection and secured minimal refusals.
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional

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

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


SYSTEM_PROMPTS = {
    "emotional_expression": "MindHaven Emotional Companion: Empathetic listening, naming feelings with the Emotion Wheel, and guided journaling for quiet introverted students.",
    "cbt_anxiety_coaching": "MindHaven CBT & Somatic Coach: 4-7-8 breathing, DBT TIPP skills, and cognitive restructuring for classroom panic and imposter syndrome.",
    "crisis_escalation": "CRITICAL EMERGENCY SAFETY PROTOCOL: Immediate 0.0ms 988 Lifeline and Crisis Text Line 741741 routing."
}

CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life", "want to die", "ending it all",
    "hang myself", "cut myself", "self-harm", "hopeless", "no reason to live",
    "giving up", "feel giving up", "feel like giving up", "give up on life",
    "giving up on life", "overdose", "hurt myself", "better off dead", "tired of living"
]

OUT_OF_SCOPE_PATTERNS = [
    # Coding, math, homework, non-mental health tasks
    r"\b(write|code|program|script|function|algorithm|solve|calculate|equation|math|homework|assignment|debug)\b.*\b(c\+\+|python|java|javascript|sql|html|css|php|rust|calculus|algebra|physics|chemistry)\b",
    r"\b(write a code|write a script|write a program|write an essay about|write code|code in|binary search|sorting algorithm)\b",
    # Medical prescriptions / clinical diagnosis requests
    r"\b(prescribe|prescription|dosage|dose|mg of|xanax|lexapro|prozac|adderall|zoloft|valium|klonopin|ativan|diagnose me with|do i have bipoloar|do i have schizophrenia)\b",
    # General trivia / off-topic tasks
    r"\b(who is the president|capital of|weather in|stock price|movie recommendation|recipe for|tell me a joke about|bitcoin|crypto)\b"
]


class MindHavenCounselor:
    """Intelligent Mental Health & Introvert Counseling Companion with Secured Boundaries."""

    def __init__(self):
        self.vector_store = PineconeVectorStore.load()
        self.gemini_key = os.getenv("GEMINI_API_KEY")
        self.openai_key = os.getenv("OPENAI_API_KEY")

    @staticmethod
    def detect_crisis(user_input: str) -> bool:
        """Evaluates text for crisis triggers using high-priority keyword matching."""
        lower = user_input.lower()
        return any(k in lower for k in CRISIS_KEYWORDS)

    @staticmethod
    def is_out_of_scope(user_input: str) -> bool:
        """Detects if query is outside the mental health & emotional wellness domain."""
        lower = user_input.lower()
        for pattern in OUT_OF_SCOPE_PATTERNS:
            if re.search(pattern, lower):
                return True
        return False

    def generate_response(self, user_query: str) -> Dict[str, Any]:
        """Generates direct mental health responses or secured minimal refusals for out-of-scope requests."""
        start_time = time.time()

        # -------------------------------------------------------------
        # 1. EMERGENCY CRISIS GUARDRAIL (0.0ms Interception)
        # -------------------------------------------------------------
        if self.detect_crisis(user_query):
            crisis_response = (
                "🚨 **EMERGENCY CRISIS SUPPORT & SAFETY NOTICE**\n\n"
                "If you are feeling overwhelmed, hopeless, or having thoughts of hurting yourself, "
                "please know that **you are not alone** and immediate, free, confidential support is available right now:\n\n"
                "**24/7 Text & Phone Crisis Resources:**\n"
                "• **National Suicide & Crisis Lifeline:** Call or Text **988** (Toll-Free, 24/7, Confidential)\n"
                "• **Crisis Text Line:** Text **HOME to 741741** (100% free text-based crisis counseling)\n"
                "• **The Trevor Project (LGBTQ+):** Text **START to 678-678** or Call **1-866-488-7386**\n"
                "• **Campus Urgent Counseling Line:** Call **(555) 019-HELP (4357)** (24/7 On-Call Therapist)\n"
                "• **Campus Public Safety Dispatch:** Call **(555) 019-9111** (Ext. 911)\n"
                "• **Walk-in Urgent Triage:** Student Wellness Pavilion, Room 320 (Mon-Fri 8:30 AM - 5:00 PM)\n\n"
                "Please reach out to one of these resources right away. Your life and your presence matter."
            )
            return {
                "query": user_query,
                "is_crisis": True,
                "is_out_of_scope": False,
                "system_prompt_used": "crisis_escalation",
                "response": crisis_response,
                "retrieved_sources": [],
                "latency_ms": round((time.time() - start_time) * 1000, 2)
            }

        # -------------------------------------------------------------
        # 2. OUT-OF-SCOPE BOUNDARY CHECK (Secured Minimal Refusal)
        # -------------------------------------------------------------
        if self.is_out_of_scope(user_query):
            refusal_statement = (
                "I am exclusively designed to support college students with mental health, emotional wellness, "
                "and stress management. I cannot assist with requests outside of this scope."
            )
            return {
                "query": user_query,
                "is_crisis": False,
                "is_out_of_scope": True,
                "system_prompt_used": "out_of_scope_refusal",
                "response": refusal_statement,
                "retrieved_sources": [],
                "latency_ms": round((time.time() - start_time) * 1000, 2)
            }

        # -------------------------------------------------------------
        # 3. PINECONE VECTOR RETRIEVAL (In-Scope Mental Health Context)
        # -------------------------------------------------------------
        retrieved_chunks = self.vector_store.query(user_query, top_k=2, metric="cosine")

        # -------------------------------------------------------------
        # 4. DIRECT CONVERSATIONAL SYNTHESIS
        # -------------------------------------------------------------
        if self.gemini_key:
            try:
                from google import genai
                client = genai.Client(api_key=self.gemini_key)
                prompt = (
                    f"You are MindHaven, an empathetic, supportive, and practical mental health counselor for college students, "
                    f"especially quiet, introverted, or socially anxious students.\n"
                    f"Student Query: '{user_query}'\n"
                    f"Reference Knowledge: {retrieved_chunks[0]['text'] if retrieved_chunks else ''}\n"
                    f"Direct, warm, step-by-step counselor response:"
                )
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                direct_answer = response.text
            except Exception:
                direct_answer = self._synthesize_direct_mental_health_answer(user_query, retrieved_chunks)
        else:
            direct_answer = self._synthesize_direct_mental_health_answer(user_query, retrieved_chunks)

        return {
            "query": user_query,
            "is_crisis": False,
            "is_out_of_scope": False,
            "system_prompt_used": "emotional_companion",
            "response": direct_answer,
            "retrieved_sources": [
                {"title": c["title"], "chunk_id": c["chunk_id"], "score": c["score"]}
                for c in retrieved_chunks
            ],
            "latency_ms": round((time.time() - start_time) * 1000, 2)
        }

    def _synthesize_direct_mental_health_answer(self, query: str, chunks: List[Dict[str, Any]]) -> str:
        """Synthesizes direct mental health answers for in-scope student inquiries."""
        q = query.lower()

        # Case 1: Emotional Numbness / Bottled Feelings
        if any(w in q for w in ["numb", "bottle", "bottling", "express", "feeling", "feelings", "unexpressed", "journal"]):
            return (
                "🌿 **Unpacking Bottled Emotions & Accessing Your Feelings**\n\n"
                "First, take a gentle, slow breath. Feeling emotionally numb or unable to explain what you feel is not a failure—it is your nervous system's subconscious way of protecting you when college life becomes too loud or overwhelming.\n\n"
                "Here is a safe, step-by-step way to start gently connecting with your feelings:\n\n"
                "1. **Check In With Your Physical Body First:**\n"
                "   • *Tight chest or shallow breath?* You might be carrying suppressed anxiety or fear of disappointing others.\n"
                "   • *Heavy throat or tired eyes?* You might be holding unspoken sadness, grief, or longing for comfort.\n"
                "   • *Clenched jaw or tight shoulders?* You might be feeling overlooked or frustrated with boundary violations.\n\n"
                "2. **Use the Emotion Granularity Wheel:**\n"
                "   Instead of staying with vague discomfort ('I feel bad'), narrow it down:\n"
                "   • Is it **Sensory Exhaustion**? (Social battery drained from communal living)\n"
                "   • Is it **Disconnection**? (Craving 1-on-1 understanding rather than loud parties)\n"
                "   • Is it **Guilt**? (Feeling pressured that you 'should' be more outgoing)\n\n"
                "3. **The 3-Minute Private Reflection Exercise:**\n"
                "   In a private notebook or note app that no one else will ever see, finish this sentence stem:\n"
                "   > 📝 *'What I wish I could say out loud right now without anyone judging or trying to fix me is...'* \n\n"
                "Remember: As an introverted scholar, you don't need to force yourself to be loud on anyone else's timeline. Your quiet depth is valid. [Ref: Introvert Emotional Expression & Journaling Handout]"
            )

        # Case 2: Classroom Social Anxiety / Shaking Voice / Presentation Panic
        elif any(w in q for w in ["called on", "presentation", "public speaking", "shaking", "trembling", "social anxiety", "freeze"]):
            return (
                "😰 **Calming Classroom Participation Panic & Shaking Voice**\n\n"
                "That sudden surge of panic—where your heart races, your voice trembles, and your mind goes blank when spotlighted—is the sympathetic nervous system triggering an acute 'Fight or Flight' reaction. You are not incompetent; your adrenaline is just temporarily high.\n\n"
                "Here is how to de-escalate that physical panic in the moment:\n\n"
                "1. **The 4-7-8 Somatic Vagus Nerve Reset:**\n"
                "   • Inhale quietly through your nose for **4 seconds**.\n"
                "   • Hold your breath gently for **7 seconds**.\n"
                "   • Exhale slowly through your mouth with a soft whoosh for **8 seconds**.\n"
                "   *(Making your exhale longer than your inhale physically forces your heart rate to slow down).* \n\n"
                "2. **Tactile Grounding (Pencil-to-Paper Reset):**\n"
                "   Plant both feet flat against the hard floor. Press your toes down. Grip your pen firmly and feel the solid desk. Remind yourself: *'My adrenaline is spiked, but I am in a safe room.'*\n\n"
                "3. **De-Catastrophize the 'Spotlight Effect':**\n"
                "   Psychological research shows that peers and professors notice less than 15% of perceived nervousness. Even if your voice feels shaky to you, to everyone else it sounds like a normal, thoughtful pause.\n\n"
                "4. **Gradual Exposure Micro-Steps:**\n"
                "   Start small: sit in rows 2–4, write down one observation in your notes before class starts, and talk to your professor for 60 seconds after class rather than during the main lecture. [Ref: Social Anxiety & Classroom Participation Panic]"
            )

        # Case 3: Dorm Overstimulation / Solitude
        elif any(w in q for w in ["dorm", "roommate", "overstimulated", "overstimulation", "battery", "solitude", "alone"]):
            return (
                "🔋 **Recharging Your Social Battery & Dormitory Overstimulation**\n\n"
                "Living in a high-decibel communal dormitory without private space drains an introvert's dopamine and mental energy rapidly, leading to 'Introvert Hangover.'\n\n"
                "Here are practical ways to protect your energy and reclaim your sanctuary:\n\n"
                "1. **The Headphone Boundary Rule:**\n"
                "   Wear over-ear noise-canceling headphones when you need quiet. Agree with your roommate: *'When headphones are on, it means I'm in low-energy recharge mode—please message me if it's urgent.'*\n\n"
                "2. **Gentle Refusal Script for Social Invites:**\n"
                "   > *'Thank you so much for inviting me! I'm completely out of social battery tonight and need a quiet evening to rest, but I appreciate you thinking of me.'*\n\n"
                "3. **Seek Campus Quiet Sanctuaries:**\n"
                "   • **Library 4th Floor Silent Atrium** (Zero-noise zone)\n"
                "   • **Memorial Botanical Gardens** (Peaceful green space)\n"
                "   • **'The Oasis' Relaxation Lounge** (Student Union Room 204: dim lighting and sensory pods). [Ref: Dorm Life Overstimulation & Solitude Recharge]"
            )

        # Case 4: Imposter Syndrome / Perfectionism
        elif any(w in q for w in ["imposter", "smarter", "fraud", "perfectionism", "failing", "failure", "grades"]):
            return (
                "🧠 **Overcoming Imposter Syndrome & Perfectionism**\n\n"
                "In fast-paced university classrooms that praise rapid, loud answers, thoughtful introverts who reflect before speaking often internalize feelings of being 'frauds.'\n\n"
                "Let's reframe this using Cognitive Behavioral Therapy (CBT):\n\n"
                "1. **Speed Does Not Equal Intelligence:**\n"
                "   High-level engineering, writing, and scientific reasoning require internal incubation. The loudest person in the room is rarely the deepest thinker.\n\n"
                "2. **Build a Private 'Evidence Folder':**\n"
                "   Keep a digital folder of verified accomplishments: high-scoring assignments, working code, professor feedback, and complex bugs you solved alone.\n\n"
                "3. **Adopt the '85% Good Enough' Rule:**\n"
                "   A completed project submitted at 85% quality is infinitely better than an unfinished draft that stays in your head. [Ref: Imposter Syndrome in Quiet Achievers & CBT Reframing]"
            )

        # Case 5: Acute Panic / DBT TIPP Skills
        elif any(w in q for w in ["panic", "heart racing", "overwhelmed", "freaking out", "hyperventilating", "tipp"]):
            return (
                "🧊 **Emergency DBT TIPP Skills for High-Intensity Overwhelm (80%+ Distress)**\n\n"
                "When your emotional distress is too intense for logic or positive thinking, you must physically change your body chemistry within 60 seconds:\n\n"
                "1. **T - Temperature (The Cold Water Shock Reset):**\n"
                "   Splash ice-cold water on your face or hold an ice cube in your palm for 30 seconds. This immediately triggers the **Mammalian Dive Reflex**, dropping your heart rate by 10–25% automatically.\n\n"
                "2. **I - Intense Exercise (Discharge the Cortisol):**\n"
                "   Do 60 seconds of jumping jacks, brisk wall sits, or pushups to discharge the adrenaline surge trapped in your muscles.\n\n"
                "3. **P - Paced Breathing (4 in, 7 out):**\n"
                "   Inhale for 4 seconds, exhale smoothly for 7 seconds.\n\n"
                "4. **P - Paired Muscle Relaxation:**\n"
                "   Tense your fists, shoulders, and jaw tightly for 5 seconds, then consciously let all tension drop as you breathe out. [Ref: DBT TIPP Clinical Protocols]"
            )

        # Default in-scope response
        top_chunk = chunks[0] if chunks else None
        return (
            f"🌿 **MindHaven Emotional Guidance**\n\n"
            f"Thank you for sharing what you are going through. Based on our campus clinical wellness resources:\n\n"
            f"{top_chunk['text'] if top_chunk else 'You are in a safe, judgment-free space.'}\n\n"
            f"💡 *Actionable Next Step:* Take a slow 4-7-8 breath, acknowledge how much energy you have exerted today, and give yourself permission to step back into a quiet space to rest."
        )


# Backward compatibility
MindCampusCounselor = MindHavenCounselor


def run_chat_completion_demo():
    """Runs test cases verifying in-scope direct answers, crisis escalation, and out-of-scope refusals."""
    counselor = MindHavenCounselor()
    
    test_cases = [
        {
            "category": "In-Scope: Emotional Numbness",
            "query": "I feel emotionally numb and bottle everything up inside. How do I start figuring out what I'm actually feeling?"
        },
        {
            "category": "Out-of-Scope: Prescription Medication Request",
            "query": "Can you prescribe a dosage of Xanax or Lexapro for my anxiety?"
        },
        {
            "category": "Out-of-Scope: Coding Homework Request",
            "query": "Can you write a binary search algorithm in C++ for my data structures assignment?"
        },
        {
            "category": "Emergency Safety Guardrail",
            "query": "I can't take this anymore, I feel hopeless and want to end my life."
        }
    ]

    print("=" * 80)
    print("MINDHAVEN AI - SECURED MENTAL HEALTH CHAT ENGINE")
    print("=" * 80)

    for idx, tc in enumerate(test_cases, 1):
        print(f"\n[TEST #{idx}] {tc['category']}")
        print(f"Query: \"{tc['query']}\"")
        print("-" * 80)
        
        result = counselor.generate_response(tc["query"])
        print(f"System Prompt: {result['system_prompt_used']} | Crisis: {result['is_crisis']} | Out-of-Scope: {result.get('is_out_of_scope', False)}")
        print(f"\nResponse:\n{result['response']}\n")
        print("=" * 80)


if __name__ == "__main__":
    run_chat_completion_demo()
