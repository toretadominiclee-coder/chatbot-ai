"""
Script to generate 28 authentic, realistic, and messy raw data files for MindHaven AI / QuietMind AI.
100% focused on Mental Health & Emotional Expression Counseling for College Students
with special emphasis on introverts, social anxiety, sensory overload, and accessing hidden feelings.
"""

import os
import shutil
from pathlib import Path

DATA_DIR = Path("data/raw")
# Clean and recreate raw data directory
if DATA_DIR.exists():
    shutil.rmtree(DATA_DIR)
DATA_DIR.mkdir(parents=True, exist_ok=True)

documents = [
    # -------------------------------------------------------------
    # 1. EMOTIONAL EXPRESSION, INTROVERSION & JOURNALING (Docs 1-6)
    # -------------------------------------------------------------
    (
        "doc_01_introvert_emotional_expression_and_journaling.txt",
        """================================================================================
CAMPUS WELLNESS & INTROVERT SUPPORT CENTER | CLINICAL MODULE 2026-EXP-01
DOCUMENT CODE: WELL-INT-2026-V2 | REVISED: FALL 2026
*** UNCONTROLLED COPY WHEN PRINTED -- FOR STUDENT PEER COUNSELING & SELF-CARE ***
================================================================================

SECTION 1: UNLOCKING UNEXPRESSED EMOTIONS FOR INTROVERTED STUDENTS

Introverted and internalizing students frequently process overwhelming emotional states internally rather than verbally sharing them with peers or authority figures. Over time, internalizing emotional distress without structured expression leads to "emotional bottling," somatic tension (headaches, gastrointestinal upset), and sudden depressive collapse.

[PAGE 1 OF 6 - CONFIDENTIAL COUNSELING HANDOUT]

1.1 The Emotion-Naming Protocol (Granularity Scale):
When feeling vague distress or emotional numbness, students should consult the Plutchik / Geneva Emotion Wheel to move from broad labels ("I feel bad") to high-granularity descriptors:
  - Anger -> Frustrated, Bitter, Resentful, Overlooked
  - Sadness -> Isolated, Exhausted, Disheartened, Homesick
  - Fear -> Inadequate, Exposed, Overstimulated, Apprehensive
  - Shame -> Mortified, Burdened, Unworthy

1.2 The "Unsent Letter" & Private Expressive Writing Exercise:
Expressive writing for 15 minutes daily about suppressed thoughts activates the ventrolateral prefrontal cortex, reducing autonomic nervous system arousal.
Steps:
  Step 1: Write continuously for 12 minutes without editing grammar, spelling, or coherence.
  Step 2: Answer the prompt: "What I wish I could say out loud right now without being judged is..."
  Step 3: Acknowledge the feeling without trying to immediately 'fix' it.
================================================================================
"""
    ),
    (
        "doc_02_social_anxiety_and_classroom_participation_panic.txt",
        """UNIVERSITY COUNSELING & PSYCHOLOGICAL SERVICES (CAPS) -- CLINICAL PROTOCOL
SUBJECT: SOCIAL ANXIETY AND CLASSROOM PARTICIPATION FEAR
EFFECTIVE DATE: AUGUST 2026 | DOCUMENT CODE: CAPS-ANX-SOC-2026

1.0 CLINICAL PRESENTATION IN COLLEGE ENVIRONMENTS
Social Anxiety Disorder (SAD) and situational public speaking panic manifest acutely during lecture participation, cold-calling by professors, and group presentations. Introverted students often report intense fear of negative evaluation, trembling voice, tachycardia, and "brain fog" when spotlighted.

[CONFIDENTIAL - CLINICAL COUNSELOR HANDBOOK]

2.0 GRADUAL EXPOSURE HIERARCHY (MICRO-PARTICIPATION LADDER):
To desensitize the amygdala to classroom visibility, introverted students should implement micro-steps:
  Step 1: Arrive 5 minutes early and sit in rows 2-4 (avoids feeling trapped in front or forgotten in back).
  Step 2: Prepare one written question or observation in your notes BEFORE class starts.
  Step 3: Nod or make brief 3-second eye contact with the professor during lecture points.
  Step 4: Speak with the professor at the end of class for 60 seconds ("I found your point on X interesting").
  Step 5: Raise hand once per week to read a prepared slide or answer an objective question.

[PAGE 2 OF 5]

3.0 DE-CATASTROPHIZING THE "SPOTLIGHT EFFECT":
Psychological research indicates peers notice less than 15% of perceived nervousness (trembling hands, brief stutter). The physiological sensation of anxiety is invisible to 85% of observers.
"""
    ),
    (
        "doc_03_dorm_life_overstimulation_and_introvert_burnout.txt",
        """RESIDENTIAL LIFE WELLNESS ALLIANCE -- DORMITORY OVERSTIMULATION & SOLITUDE RECHARGE
MANUAL CODE: RES-WELL-2026-03

1. THE INTROVERT ENERGY RECHARGE CYCLE:
Introverted temperaments deplete dopamine and mental stamina through prolonged social engagement and noisy communal living environments. Sharing a double/triple dorm room without private solitude causes chronic "Introvert Hangover" (irritability, brain exhaustion, social detachment).

[PAGE 1 OF 4]

2. STRATEGIES FOR RECLAIMING SANCTUARY IN COMMUNAL DORMS:
  - The "Green Flag / Red Flag" Headphone Rule: Establish clear visual boundaries with roommates. Wearing over-ear noise-canceling headphones signals "Recharge Mode -- Please do not initiate casual small talk unless emergency."
  - Campus Quiet Sanctuary Directory:
      * University Library 4th Floor Silent Atrium (Open until 2:00 AM)
      * Memorial Botanical Gardens & Solitude Benches (East Campus)
      * Arts Pavilion Reflection Lounge (3rd Floor Mezzanine)
  - Scheduled Solitude Breaks: Block off a non-negotiable 45-minute daily "Quiet Window" for solo walks, reading, or meditation without phone notifications.
"""
    ),
    (
        "doc_04_cbt_thought_reframing_for_introverted_students.txt",
        """CLINICAL PSYCHOLOGY RESOURCE: COGNITIVE BEHAVIORAL THERAPY (CBT) FOR QUIET ACHIEVERS
GUIDEBOOK: CAPS-CBT-QUIET-2026 | AUTHOR: UNIVERSITY PSYCHOLOGICAL SERVICES

1. COGNITIVE DISTORTIONS PREVALENT IN INTROVERTED STUDENTS:
  - Extrovert Ideal Distortion: "Because I am quiet in meetings, my professor and team must think I lack leadership ability or intelligence."
  - Mind Reading: "Everyone at the dining hall table noticed I was eating alone and thinks I am a weird loner."
  - Catastrophizing Silence: "I paused for 5 seconds before answering the question; I completely ruined my reputation in this seminar."

[PAGE 2 OF 4]

2. THE 4-STAGE REFRAMING WORKFLOW:
  Stage 1: Catch the Automatic Negative Thought (ANT).
  Stage 2: Check the Evidence: What factual proof exists? (e.g., "My grades and project contributions are strong; silence is thoughtful processing, not ignorance").
  Stage 3: Distinguish Solitude from Isolation: Solitude is a healthy, chosen restorative state; isolation is fear-based withdrawal.
  Stage 4: Formulate a Balanced Reframe:
          * Distorted: "I hate small talk, so I will never make friends in college."
          * Balanced Reframe: "I thrive in deep, 1-on-1 conversations rather than loud parties. I will connect with people through shared niche interests and study circles."
"""
    ),
    (
        "doc_05_imposter_syndrome_in_quiet_achievers.txt",
        """STUDENT SUCCESS & MENTAL HEALTH ALLIANCE -- IMPOSTER SYNDROME IN INTROVERTS
DOCUMENT: WELL-IMP-2026 | CLASSIFICATION: PSYCHOEDUCATION

1. THE "LOUD BIAS" AND QUIET IMPOSTER SYNDROME:
In university classrooms that reward rapid, assertive speaking, introspective students who prefer reflecting before answering often internalize feelings of being intellectual "frauds."

[PAGE 1 OF 3]

2. COUNTERACTING IMPOSTER THOUGHTS:
  - Value Thoughtful Precision Over Speed: High-quality analytical thinking often requires internal incubation. Speed of speech is not correlated with intellectual depth.
  - The "Evidence Folder" Technique: Maintain a private digital archive of verified accomplishments: high-scoring essays, working code repositories, professor praise, and solved problems.
  - Reframe Self-Doubt: Recognize that experiencing imposter syndrome is common among high-empathy, conscientious scholars—not a diagnostic confirmation of inadequacy.
"""
    ),
    (
        "doc_06_test_anxiety_and_performance_paralysis_management.txt",
        """STUDENT WELLNESS SERVICES -- MANAGING EXAM PANIC AND PERFORMANCE PARALYSIS
DOCUMENT CODE: WELL-ANX-TEST-2026 | CLINICAL EDITION

1. PHYSIOLOGICAL PANIC IN HIGH-STAKES EXAMS:
During midterm and final exams, high-achieving quiet students often experience acute sympathetic nervous system overload: shallow hyperventilation, cold trembling hands, racing heart, and cognitive blanking.

[PAGE 2 OF 3]

2. IMMEDIATE IN-EXAM RESET PROTOCOLS:
  - Box Breathing (4x4 Matrix): Inhale 4 counts -> Hold 4 counts -> Exhale 4 counts -> Hold empty 4 counts. Repeat 4 cycles to stimulate the vagus nerve and slow heart rate.
  - Tactile Grounding (Pencil-to-Paper Reset): Put down your pencil, plant both feet flat on the floor, push your toes down, and feel the solid ground. Tell yourself: "My adrenaline is high, but I am physically safe."
  - Brain Dump Strategy: Use the first 2 minutes of the exam to write down formulas, mnemonics, and key concepts on scratch paper to free up working memory.
"""
    ),

    # -------------------------------------------------------------
    # 2. SOCIAL ANXIETY, CONNECTION & BOUNDARIES (Docs 7-12)
    # -------------------------------------------------------------
    (
        "doc_07_loneliness_vs_solitude_for_college_introverts.txt",
        """CAMPUS MENTAL HEALTH & STUDENT INTEGRATION -- LONELINESS VS. HEALTHY SOLITUDE
BULLETIN: CMH-SOLITUDE-2026

1. UNDERSTANDING THE CRITICAL DIFFERENCE:
Solitude is the peaceful state of being alone without being lonely; it restores mental energy and fosters creativity. Loneliness is the painful discrepancy between desired social connection and actual connection.

[PAGE 1 OF 3]

2. OVERCOMING SOCIAL PARALYSIS WITHOUT FORCING EXTROVERSION:
  - The "1-on-1 Connection" Strategy: Avoid overwhelming 50-person frat parties. Focus on inviting one classmate for tea, coffee, or a quiet library study session.
  - Parallel Play & Low-Pressure Company: Study alongside a friend in silence. You get the comfort of social presence without the exhausting burden of continuous conversation.
  - Join Interest-Specific Groups: Seek clubs with structured activities (e.g., Coding Club, Board Games, Creative Writing, Astronomy) where interaction is focused around an activity rather than open-ended small talk.
"""
    ),
    (
        "doc_08_group_project_anxiety_and_introvert_advocacy.txt",
        """CENTER FOR ACADEMIC & EMOTIONAL RESILIENCE -- NAVIGATING GROUP PROJECT ANXIETY
GUIDELINE: CAER-GRP-2026

1. CHALLENGES FOR INTROVERTED STUDENTS IN GROUP WORK:
Dominant personalities often take over discussions, leaving thoughtful introverted students feeling steamrolled, ignored, or stuck doing uncredited heavy lifting behind the scenes.

[PAGE 2 OF 4]

2. ASSERTIVE COMMUNICATION FRAMEWORKS:
  - Asynchronous Contribution: "I'd like to take responsibility for writing the core technical documentation and literature review by Wednesday evening."
  - The "Pause & Reflect" Interjection: "I have a thought on what Sarah just said. If we pause for a moment, I think we can simplify the architecture by doing X."
  - Pre-Meeting Agenda Review: Look at the meeting agenda beforehand and write down 2 bullet points you intend to share.
"""
    ),
    (
        "doc_09_academic_burnout_and_chronic_exhaustion_recovery.txt",
        """STUDENT HEALTH INITIATIVE -- ACADEMIC BURNOUT AND CHRONIC EXHAUSTION RECOVERY
MODULE: BURNOUT-REC-2026 | OFFICE OF WELLNESS

1. THE THREE PHASES OF BURNOUT:
  Phase 1: Emotional Exhaustion (feeling drained upon waking, dreading assignments).
  Phase 2: Depersonalization & Cynicism (feeling detached from learning, resentment).
  Phase 3: Loss of Personal Accomplishment (feeling nothing you do matters).

[PAGE 1 OF 3]

2. SYSTEMATIC RECOVERY PROTOCOL:
  - Energy Accounting: Introverts have a daily "battery" of 100 units. High-stimulation socializing drains 40 units; studying drains 30 units; quiet solitude restores 30 units. Budget your energy deliberately.
  - Digital Curfew: Turn off all notifications, LMS alerts, and group chats after 9:30 PM.
  - Compassionate Pacing: Break assignments into 20-minute micro-intervals followed by 5 minutes of mindful resting (closing eyes, water, gentle stretching).
"""
    ),
    (
        "doc_10_freshman_transition_and_campus_homesickness.txt",
        """FIRST-YEAR COUNSELING SERIES -- COPING WITH FRESHMAN OVERWHELM & HOMESICKNESS
DOCUMENT: FYE-HOME-2026

1. TRANSITION SHOCK IN HIGH-STIMULATION CAMPUSES:
Moving from a familiar quiet bedroom at home to a chaotic dormitory campus with 20,000 strangers creates profound sensory and emotional disorientation.

[PAGE 2 OF 3]

2. PRACTICAL SELF-CARE ANCHORS:
  - Build Micro-Routines: Create 3 predictable daily rituals that belong only to you (e.g., making morning tea in your favorite mug, 15 minutes of evening journaling, listening to a favorite podcast).
  - Normalize the Emotion: Feeling homesick is a healthy reflection of caring for your roots, not an indicator that you cannot thrive in college.
  - Scheduled Home Calls: Set fixed weekly call times with family rather than constantly texting 24/7, which prolongs attachment distress.
"""
    ),
    (
        "doc_11_emotional_dysregulation_and_grounding_tipp_skills.txt",
        """DIALECTICAL BEHAVIOR THERAPY (DBT) CLINICAL SKILLS: TIPP PROTOCOL FOR CRISIS
HANDBOOK: CAPS-DBT-TIPP-2026 | CLINICAL WELLNESS

1. WHAT TO DO WHEN EMOTIONS REACH 80%+ INTENSITY:
When emotional distress overwhelms cognitive reasoning, use somatic DBT TIPP skills to physically change body chemistry within 60 seconds:

[PAGE 1 OF 4 - DBT CRISIS SKILLS]

2. THE TIPP SKILLS BREAKDOWN:
  - T - Temperature: Splash cold water on your face or hold an ice cube in your hand. This triggers the Mammalian Dive Reflex, immediately dropping heart rate by 10-25%.
  - I - Intense Exercise: Do 60 seconds of jumping jacks, wall sits, or brisk pacing to discharge adrenaline and cortisol.
  - P - Paced Breathing: Inhale for 4 seconds, exhale for 7 seconds. Ensure your exhale is longer than your inhale to activate the parasympathetic brake.
  - P - Paired Muscle Relaxation: Tense your shoulders, fists, and jaw for 5 seconds, then consciously release while breathing out.
"""
    ),
    (
        "doc_12_perfectionism_and_fear_of_failure_coping.txt",
        """COUNSELING & PSYCHOLOGICAL INSIGHTS -- OVERCOMING MALADAPTIVE PERFECTIONISM
DOC: CAPS-PERF-2026 | REVISED EDITION

1. THE TOXICITY OF "ALL-OR-NOTHING" STANDARDS:
Introverted, conscientious students often battle maladaptive perfectionism: the belief that anything less than a 100% score or flawless presentation is an unacceptable failure. This leads to chronic procrastination and paralyzing anxiety.

[PAGE 1 OF 3]

2. THERAPEUTIC SHIFTS (SELF-COMPASSION PROTOCOL):
  - "Good Enough" is Good Enough: Adopt the 85% rule on non-critical tasks. A completed assignment submitted on time is infinitely better than an unfinished "perfect" draft.
  - The Best Friend Test: When you catch yourself being viciously self-critical, ask: "Would I say these harsh words to a grieving best friend?"
  - Celebrate Iteration: Science, engineering, and writing are iterative disciplines where mistakes are necessary data points for growth.
"""
    ),

    # -------------------------------------------------------------
    # 3. CLINICAL INTAKE, SLEEP & SOMATIC HEALING (Docs 13-18)
    # -------------------------------------------------------------
    (
        "doc_13_sleep_hygiene_and_late_night_overthinking.txt",
        """BEHAVIORAL SLEEP MEDICINE -- CALMING RACING THOUGHTS AT BEDTIME
WELLNESS PAMPHLET: SLEEP-OVERTHINK-2026

1. THE "MIDNIGHT REPLAY" SYNDROME:
When introverts lie down in darkness without external distractions, the brain often starts hyper-analyzing awkward daytime interactions, upcoming deadlines, and worst-case scenarios.

[PAGE 1 OF 2]

2. BEDTIME COGNITIVE OFFLOADING:
  - The "Worry Journal" Beside the Bed: If a racing thought repeats 3 times, turn on a dim lamp and write it down on paper: "I have recorded this; I will handle it at 10:00 AM tomorrow."
  - 20-Minute Sleep Rule: If you cannot fall asleep after 20 minutes, get out of bed. Sit in a comfortable chair under dim light and read a calming book until drowsy. Never stay in bed tossing and turning.
  - Progressive Muscle Relaxation (PMR): Systematically scan your body from toes to forehead, relaxing each muscle group on the exhale.
"""
    ),
    (
        "doc_14_adhd_neurodiversity_and_sensory_overload.txt",
        """STUDENT DISABILITY & NEURODIVERSITY CENTER -- SENSORY OVERLOAD AND FOCUS GUIDE
POLICY CODE: SDAS-NEURO-2026

1. SENSORY SENSITIVITIES IN INTROVERTED & NEURODIVERGENT SCHOLARS:
Students with ADHD, Autism Spectrum traits, or sensory processing differences experience rapid nervous system exhaustion in fluorescent-lit, high-decibel campus environments.

[PAGE 1 OF 4]

2. CAMPUS ACCOMMODATIONS & SELF-REGULATION:
  - Testing in Reduced-Distraction Environments: Registered students through SDAS are entitled to quiet testing rooms and noise-canceling earmuffs.
  - Sensory Toolkit: Carry earplugs (Loop / foam), blue-light filtering glasses, and discrete fidget tools in your backpack.
  - Scheduled Sensory Decompression: Spend 15 minutes after classes in dark/quiet spaces to reset sensory thresholds.
"""
    ),
    (
        "doc_15_crisis_triage_and_suicide_prevention_protocol.txt",
        """CAMPUS CRISIS RESPONSE PROTOCOL -- IMMEDIATE PSYCHOLOGICAL TRIAGE & SAFETY
DOCUMENT: MH-CRISIS-2026-CONFIDENTIAL | OFFICE OF HEALTH & PSYCHOLOGICAL WELLNESS
*** EMERGENCY DIRECTIVE -- STRICT SAFETY COMPLIANCE REQUIRED FOR ALL AGENTS ***

1. DEFINITION OF ACUTE CRISIS:
Any disclosure or indication of suicidal ideation, intent, plan, self-harm impulses, severe psychotic disorientation, or life-threatening distress.

[PAGE 1 OF 3 - STRICT CONFIDENTIALITY & SAFETY PROTOCOL]

2. IMMEDIATE CRISIS ESCALATION PROTOCOLS:
When an AI system or peer listener detects crisis triggers:
  STEP 1: NEVER close or disconnect the chat session.
  STEP 2: Immediately provide the following 24/7 Crisis Lifelines:
          * National Suicide & Crisis Lifeline: Call or Text 988 (Toll-Free, 24/7, Free & Confidential)
          * Crisis Text Line: Text HOME to 741741 (Free, 24/7, Text-Based Support)
          * Campus Public Safety & Police Dispatch: Call (555) 019-9111
          * Campus Counseling Urgent Care Line: (555) 019-HELP (4357) (24/7 On-Call Therapist)
  STEP 3: Direct to nearest Emergency Department or Student Health Center (Building B, Room 100).
  STEP 4: Provide warm validation: "Your life is valuable and you do not have to carry this immense weight alone."
"""
    ),
    (
        "doc_16_campus_counseling_center_caps_intake_guide.txt",
        """STUDENT COUNSELING & PSYCHOLOGICAL SERVICES (CAPS) -- INTROVERT-FRIENDLY INTAKE
STUDENT HANDBOOK SUPPLEMENT -- WELLNESS EDITION 2026

1. STARTING COUNSELING WITHOUT PHONE CALL ANXIETY:
Many introverted and anxious students delay therapy because they dread calling a receptionist. CAPS provides 100% digital self-scheduling.
- Online Intake Booking: Visit https://caps.university.edu and complete the confidential 5-minute digital intake questionnaire.
- Location: Student Wellness Pavilion, 3rd Floor, Suite 320.
- Walk-in Crisis Hours: Monday - Friday, 10:00 AM - 3:00 PM (No appointment needed).

[PAGE 2 OF 5]

2. WHAT TO EXPECT IN YOUR FIRST SESSION:
The first 45-minute intake session is an open, gentle conversation where you set the pace. You do not have to share deep trauma immediately.
- Cost: Enrolled students receive up to twelve (12) individual therapy sessions per year at ZERO cost (covered by Student Health Fee).
- Confidentiality: All sessions are protected under FERPA & HIPAA. Notes are never shared with parents, professors, or academic transcripts.
"""
    ),
    (
        "doc_17_grief_bereavement_and_silent_sorrow.txt",
        """OFFICE OF THE DEAN OF STUDENTS -- COMPASSIONATE GRIEF AND BEREAVEMENT SUPPORT
MEMO: DOS-GRIEF-2026 | WELLNESS GUIDELINES

1. PROCESSING GRIEF IN SILENCE:
Introverts often mourn losses quietly, leading friends to mistakenly assume they are "doing fine." Suppressed grief can manifest months later as profound fatigue, brain fog, and lack of motivation.

[PAGE 1 OF 3]

2. GRIEF RESOURCES ON CAMPUS:
  - Excused Bereavement Absence: Up to 5 consecutive class days for immediate family loss with Dean of Students notice.
  - Weekly "Healing in Solitude" Grief Circle: A quiet, supportive group where students can listen or speak at their own comfort level (Thursdays at 4:00 PM in CAPS Suite 320).
  - Compassionate Extensions: Advisors can coordinate assignment extensions during acute bereavement.
"""
    ),
    (
        "doc_18_substance_use_and_harm_reduction_resources.txt",
        """HEALTH & WELLNESS SERVICES -- HARM REDUCTION AND SOCIAL ANXIETY
DOCUMENT: HWS-HARM-2026

1. SELF-MEDICATING SOCIAL ANXIETY WITH ALCOHOL OR CANNABIS:
Introverted students frequently use alcohol or cannabis as "social lubricants" to endure loud parties or suppress loneliness. This creates dependency and exacerbates baseline anxiety ("hangxiety").

[PAGE 1 OF 3]

2. SAFE SUPPORT & MEDICAL AMNESTY:
  - Medical Amnesty Policy: If you seek medical help for an intoxicated friend, neither of you will face disciplinary conduct charges.
  - Free Overdose Prevention: Free Narcan and fentanyl test strips available with no questions asked at the Student Health Pharmacy.
  - Collegiate Recovery Community (CRP): Safe, sober peer support groups meeting weekly in Annex Hall Room 12.
"""
    ),

    # -------------------------------------------------------------
    # 4. EMOTIONAL RESILIENCE, ASSERTIVENESS & SELF-DISCOVERY (Docs 19-28)
    # -------------------------------------------------------------
    (
        "doc_19_assertiveness_training_and_saying_no.txt",
        """COUNSELING & RESILIENCE SERIES -- INTROVERT ASSERTIVENESS & BOUNDARY SETTING
GUIDELINES: CAPS-ASSERT-2026

1. THE GUILT OF SAYING "NO":
Quiet, empathetic students often become people-pleasers, agreeing to cover group shifts, edit peers' essays, or attend exhausting events out of fear of causing conflict.

[PAGE 2 OF 3]

2. GENTLE BUT FIRM REFUSAL SCRIPTS:
  - Declining Social Invitations: "Thank you so much for inviting me! I'm completely out of social battery tonight and need a quiet evening to recharge, but I appreciate you thinking of me."
  - Declining Extra Academic Favors: "I would love to help, but with my current midterm deadlines, I don't have the capacity to give this the attention it deserves."
  - Remember: "No" is a complete sentence. You do not owe a detailed 10-point justification for protecting your mental well-being.
"""
    ),
    (
        "doc_20_mindfulness_and_54321_somatic_grounding.txt",
        """SOMATIC MINDFULNESS CLINIC -- 5-4-3-2-1 SENSORY GROUNDING HANDOUT
DOCUMENT: CAPS-MIND-54321-2026

1. DOWNREGULATING AMYGDALA OVERACTIVATION:
When feeling emotionally flooded, disconnected, or having a panic spike, the 5-4-3-2-1 sensory grounding technique anchors you firmly in the present physical reality.

[PAGE 1 OF 3]

2. STEP-BY-STEP EXERCISE:
  - Look for 5 Things You Can See (e.g., grain on the wooden desk, dust motes in the sunlight, your sneakers).
  - Acknowledge 4 Things You Can Physically Touch (e.g., cotton of your shirt, cold metal ring, edge of your notebook).
  - Listen for 3 Distinct Sounds (e.g., hum of the air conditioner, distant footsteps, your own breathing).
  - Smell 2 Scents (e.g., fresh coffee, rain on the pavement, hand sanitizer).
  - Say 1 Validating Truth to Yourself: "I am feeling anxious right now, but I am in a safe space and this feeling will pass."
"""
    ),
    (
        "doc_21_title_ix_and_trauma_support_pathways.txt",
        """OFFICE OF INSTITUTIONAL EQUITY & TITLE IX -- CONFIDENTIAL TRAUMA SUPPORT
POLICY CODE: OIE-TITLEIX-2026

1. TRAUMA INFORMED CARE FOR SURVIVORS:
Experiencing harassment, relationship violence, or trauma can cause survivors to withdraw into severe isolation and emotional muteness.

[PAGE 1 OF 4]

2. 100% CONFIDENTIAL ADVOCACY RESOURCES:
  - Campus Victim Advocacy Line: (555) 019-SAFE (24/7 Confidential Crisis Support).
  - Confidential CAPS Counselors and Health Center Staff: Disclosures to therapists will NEVER initiate a police or university conduct report without your explicit written consent.
  - Supportive Measures: Emergency dorm relocation, academic extensions, and Mutual No-Contact Orders available immediately.
"""
    ),
    (
        "doc_22_peer_support_networks_and_quiet_wellness_lounges.txt",
        """STUDENT AFFAIRS WELLNESS ALLIANCE -- LOW-PRESSURE PEER SUPPORT & QUIET SPACES
BULLETIN: SA-PEER-QUIET-2026

1. "THE OASIS" QUIET RELAXATION LOUNGE:
- Location: Student Union, Room 204.
- Features: Dim ambient lighting, zero-noise policy, weighted blankets, aromatherapy diffusers, and herbal tea station.
- Hours: Monday through Thursday, 12:00 PM - 8:00 PM.

[PAGE 2 OF 3]

2. NIGHTLINE QUIET LISTENING WARM-LINE:
A confidential peer-run warmline for students who just want someone to listen without judgment or unsolicited advice.
- Friday & Saturday, 8:00 PM - 2:00 AM.
- Call: (555) 019-NITE (6483) or Chat Online at https://nightline.university.edu.
"""
    ),
    (
        "doc_23_rejection_sensitivity_dysphoria_rsd_in_students.txt",
        """PSYCHOEDUCATIONAL HANDOUT: REJECTION SENSITIVITY AND EMOTIONAL INTENSITY
GUIDE: CAPS-RSD-2026

1. WHAT IS REJECTION SENSITIVITY DYSPHORIA (RSD)?
RSD is an intense emotional reaction of vulnerability and distress triggered by perceived criticism, a professor's brief critique, or a peer not responding to a text. It is especially common in neurodivergent and introverted students.

[PAGE 1 OF 3]

2. COPING WITH PERCEIVED REJECTION:
  - The "24-Hour Rule": Never send an emotional rebuttal or make drastic decisions (like dropping a class) during an acute RSD flare-up. Wait 24 hours until emotional intensity subsides.
  - Distinguish Tone from Intent: A professor's blunt email ("See me about your thesis") usually reflects lack of time, not personal hatred or disappointment.
  - Practice Self-Validation: "My feelings of being hurt are real, but the story my brain is creating about being hated may not be factual."
"""
    ),
    (
        "doc_24_family_pressure_and_introvert_career_anxiety.txt",
        """CAREER & COUNSELING COLLABORATIVE -- INTROVERTS, FAMILY PRESSURE & CAREER DREAMS
DOCUMENT: CDELC-INT-2026

1. NAVIGATING PARENTAL PRESSURE TO BE "MORE OUTGOING":
Many students face cultural or family pressure equating career success with being loud, aggressive, and constantly networking. This generates deep shame regarding quiet personalities.

[PAGE 2 OF 3]

2. EMBRACING QUIET LEADERSHIP:
  - The Power of Deep Work: Modern industry highly values deep technical mastery, active listening, and thoughtful system architecture.
  - Targeted Networking: Introverts excel in 1-on-1 coffee chats and personalized LinkedIn inquiries rather than noisy networking mixers.
  - Value Alignment: A career that honors your need for focused, quiet deep work will sustain your long-term mental health.
"""
    ),
    (
        "doc_25_compassion_fatigue_and_empath_student_wellness.txt",
        """COUNSELING INSIGHTS -- COMPASSION FATIGUE IN HIGHLY EMPATHETIC INTROVERTS
DOC: CAPS-EMPATH-2026

1. THE "EMOTIONAL SPONGE" PHENOMENON:
Introverted, empathetic students often act as the "unpaid therapist" for their friends and roommates, absorbing everyone's trauma while having nowhere to unload their own feelings.

[PAGE 1 OF 2]

2. PROTECTING YOUR EMOTIONAL ENERGY:
  - Emotional Boundaries: "I care about you deeply and want to support you, but I am emotionally exhausted right now and cannot give this the space it needs. Can we talk about this tomorrow afternoon?"
  - Encourage Professional Care: Gently guide overwhelmed friends to CAPS rather than trying to fix their crises alone.
  - Daily Energetic Reset: Wash your hands with warm water or take a shower at the end of the day, visualizing washing away absorbed emotions.
"""
    ),
    (
        "doc_26_navigating_campus_networking_and_career_fairs.txt",
        """CAREER DEVELOPMENT CENTER -- INTROVERT'S SURVIVAL GUIDE TO CAREER FAIRS
MANUAL: CDC-INT-GUIDE-2026

1. SURVIVING THE DECIBEL OVERLOAD OF CAREER FAIRS:
Crowded gymnasium career fairs with fluorescent lights and hundreds of loud recruiters trigger instant sensory paralysis in introverted job seekers.

[PAGE 2 OF 4]

2. TACTICAL INTROVERT PLAYBOOK:
  - Target 3 Companies Maximum: Research 3 specific employers in advance rather than wandering aimlessly through 50 booths.
  - Prepare a 30-Second "Elevator Pitch": "Hi, I'm Alex. I specialize in backend data pipelines and love solving complex asynchronous systems. I read about your recent project on X and wanted to learn more."
  - Planned Decompression: Schedule 15 minutes of quiet time outside the hall after every 2 recruiter conversations.
"""
    ),
    (
        "doc_27_journaling_prompts_for_accessing_deep_feelings.txt",
        """CREATIVE EXPRESSION & HEALING WORKSHOP -- GUIDED PROMPTS FOR ACCESSING EMOTIONS
CLINICAL HANDOUT: CAPS-JOURNAL-2026

1. WHY STRUCTURED PROMPTS HELP QUIET STUDENTS:
When you feel emotionally blocked or detached, open-ended journaling can feel intimidating. Targeted sentence stems gently guide your subconscious mind to articulate hidden feelings.

[PAGE 1 OF 3]

2. 10 DEEP REFLECTION PROMPTS:
  1. "Right now, my body feels tight in my [shoulders/chest/jaw] because I am carrying..."
  2. "The truth about how exhausted I feel is..."
  3. "If I wasn't afraid of disappointing anyone, I would immediately stop..."
  4. "Something I am grieving that no one else knows about is..."
  5. "I feel most peaceful and safe when I am..."
  6. "A boundary I desperately need to set this week is..."
  7. "What I really need to hear from someone right now is..."
  8. "The feeling I have been avoiding feeling all week is..."
  9. "I am proud of myself for quietly surviving..."
  10. "One small act of self-kindness I can give myself tonight is..."
"""
    ),
    (
        "doc_28_emergency_mental_health_contacts_and_warmline_directory.txt",
        """STUDENT HEALTH & WELLNESS -- 24/7 MENTAL HEALTH & TEXT-BASED CRISIS DIRECTORY
PUBLIC NOTICE: CAPS-DIR-2026-FINAL

1. 24/7 TEXT AND PHONE-BASED CRISIS SUPPORT:
Introverted students who dread talking on the phone can connect with trained crisis counselors via free, confidential text channels:

[PAGE 1 OF 2 - EMERGENCY & WELLNESS DIRECTORY]

- National Suicide & Crisis Lifeline: Call or Text 988 (Available 24/7/365, Free, Confidential)
- Crisis Text Line: Text HOME to 741741 (24/7 Free Text-Based Support)
- The Trevor Project (LGBTQ+ Crisis Line): Text START to 678-678 or Call 1-866-488-7386
- Veterans / Military Student Crisis Line: Dial 988 then Press 1, or Text 838255
- Campus Emergency Police & Public Safety: Call (555) 019-9111 (Ext. 911)
- Campus Counseling Urgent Line: (555) 019-HELP (4357) (24/7 On-Call Counselor)
- Student Wellness Pavilion Walk-in Clinic: Building 3, Room 320 (Mon-Fri 8:30 AM - 5:00 PM)

2. REMEMBER:
Reaching out for help is not a weakness; it is the ultimate act of courage and self-respect.
"""
    )
]

for filename, content in documents:
    filepath = DATA_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated raw document: {filename} ({len(content)} chars)")

print(f"\nSuccessfully generated all {len(documents)} mental health & introvert wellness documents in {DATA_DIR}!")
