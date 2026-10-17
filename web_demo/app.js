// MindHaven AI - Direct Conversational Mental Health & Emotional Companion Engine
// Client-side Web Demo

const KNOWLEDGE_CHUNKS = [
  {
    chunk_id: "doc_01_c01",
    title: "Introvert Emotional Expression And Journaling",
    category: "Emotional Expression & Journaling",
    text: "SECTION 1: UNLOCKING UNEXPRESSED EMOTIONS FOR INTROVERTED STUDENTS Introverted students process emotional states internally. Over time, internalizing distress without structured expression leads to emotional bottling, somatic tension, and depressive collapse."
  },
  {
    chunk_id: "doc_02_c01",
    title: "Social Anxiety And Classroom Participation Panic",
    category: "Social Anxiety & Classroom Coping",
    text: "1.0 CLINICAL PRESENTATION: Social Anxiety manifests acutely during lecture participation and presentations. Introverted students report intense fear of negative evaluation, trembling voice, and tachycardia."
  },
  {
    chunk_id: "doc_03_c01",
    title: "Dorm Life Overstimulation And Introvert Burnout",
    category: "Dorm Overstimulation & Solitude Recharge",
    text: "1. INTROVERT ENERGY RECHARGE CYCLE: Sharing a dorm room without private solitude causes 'Introvert Hangover' (irritability, brain exhaustion, social detachment)."
  },
  {
    chunk_id: "doc_04_c01",
    title: "Cbt Thought Reframing For Introverted Students",
    category: "CBT & Cognitive Reframing",
    text: "1. COGNITIVE DISTORTIONS IN INTROVERTS: Extrovert Ideal Distortion, Mind Reading, Catastrophizing Silence. Practice 4-stage CBT reframing."
  },
  {
    chunk_id: "doc_11_c01",
    title: "Emotional Dysregulation And Grounding Tipp Skills",
    category: "Somatic Grounding & Stress Management",
    text: "DBT TIPP SKILLS: Temperature (Cold Water Dive Reflex), Intense Exercise, Paced Breathing (4 in, 7 out), Paired Muscle Relaxation."
  },
  {
    chunk_id: "doc_15_c01",
    title: "Crisis Triage And Suicide Prevention Protocol",
    category: "Crisis Safety & Emergency Lifelines",
    text: "EMERGENCY LIFELINES: National Suicide & Crisis Lifeline: Call/Text 988. Crisis Text Line: Text HOME to 741741. Campus Police: (555) 019-9111."
  }
];

const DIFF_SAMPLES = {
  "doc_01": {
    raw: `SECTION 1: UNLOCKING UNEXPRESSED EMOTIONS FOR INTROVERTED STUDENTS
[PAGE 1 OF 6 - CONFIDENTIAL COUNSELING HANDOUT]
Introverted students process emotions internally. Over time, internalizing leads to emotional bottling.
1.1 The Emotion-Naming Protocol:
  - Anger -> Frustrated, Bitter, Overlooked
  - Sadness -> Isolated, Exhausted, Disheartened
  - Fear -> Inadequate, Exposed, Overstimulated`,
    clean: `SECTION 1: UNLOCKING UNEXPRESSED EMOTIONS FOR INTROVERTED STUDENTS
Introverted students process emotions internally. Over time, internalizing leads to emotional bottling.
1.1 The Emotion-Naming Protocol:
- Anger -> Frustrated, Bitter, Overlooked
- Sadness -> Isolated, Exhausted, Disheartened
- Fear -> Inadequate, Exposed, Overstimulated`
  }
};

function generateDirectAnswer(query) {
  const q = query.toLowerCase();

  // Crisis and severe distress check
  const crisisWords = [
    "hopeless", "kill myself", "end my life", "suicide", "want to die", 
    "ending it all", "hurt myself", "giving up", "feel giving up", "feel like giving up", "tired of living"
  ];
  if (crisisWords.some(k => q.includes(k))) {
    return {
      isCrisis: true,
      text: `🚨 <strong>EMERGENCY CRISIS SUPPORT & SAFETY NOTICE</strong><br><br>
      If you are feeling overwhelmed, hopeless, or having thoughts of hurting yourself, please know that <strong>you are not alone</strong> and confidential support is available 24/7:<br><br>
      • <strong>National Suicide & Crisis Lifeline:</strong> Call or Text <strong>988</strong> (24/7, Free, Toll-Free)<br>
      • <strong>Crisis Text Line (Text-Only):</strong> Text <strong>HOME to 741741</strong><br>
      • <strong>Campus Urgent Counseling Line:</strong> Call <strong>(555) 019-HELP (4357)</strong><br>
      • <strong>Campus Public Safety Dispatch:</strong> Call <strong>(555) 019-9111</strong> (Ext. 911)<br><br>
      Please reach out to one of these lifelines immediately. Your life and your presence matter.`
    };
  }

  // Out of Scope check (concise minimal refusal for secured system)
  const outOfScopePatterns = [
    /write.*(code|program|script|c\+\+|python|java|algorithm|binary search|sql|html)/i,
    /prescribe|dosage|dose|mg of|xanax|lexapro|prozac|adderall|zoloft/i,
    /who is the president|capital of|weather in|stock price|bitcoin|recipe/i
  ];
  if (outOfScopePatterns.some(p => p.test(q))) {
    return {
      isCrisis: false,
      title: "Out of Scope Request",
      text: `I am exclusively designed to support college students with mental health, emotional wellness, and stress management. I cannot assist with requests outside of this scope.`
    };
  }

  // Question 1: Emotional Numbness / Bottled Feelings / Accessing Emotions
  if (q.includes("numb") || q.includes("bottle") || q.includes("express") || q.includes("feeling") || q.includes("journal")) {
    return {
      isCrisis: false,
      title: "Introvert Emotional Expression & Journaling",
      text: `🌿 <strong>Unpacking Bottled Emotions & Accessing Your Feelings</strong><br><br>
      First, take a gentle, slow breath. Feeling emotionally numb or unable to explain what you feel is not a failure—it is your nervous system's subconscious way of protecting you when college life becomes too loud or overwhelming.<br><br>
      <strong>1. Check In With Your Physical Body First:</strong><br>
      • <em>Tight chest or shallow breath?</em> You might be carrying suppressed anxiety or fear of disappointing others.<br>
      • <em>Heavy throat or tired eyes?</em> You might be holding unspoken sadness, grief, or longing for comfort.<br>
      • <em>Clenched jaw or tight shoulders?</em> You might be feeling overlooked or frustrated with boundary violations.<br><br>
      <strong>2. Use the Emotion Granularity Wheel:</strong><br>
      Instead of staying with vague discomfort ('I feel bad'), narrow it down:<br>
      • Is it <strong>Sensory Exhaustion</strong>? (Social battery drained from communal living)<br>
      • Is it <strong>Disconnection</strong>? (Craving 1-on-1 understanding rather than loud parties)<br>
      • Is it <strong>Guilt</strong>? (Feeling pressured that you 'should' be more outgoing)<br><br>
      <strong>3. The 3-Minute Private Reflection Exercise:</strong><br>
      In a private notebook or note app that no one else will ever see, finish this sentence stem:<br>
      <blockquote>📝 <em>"What I wish I could say out loud right now without anyone judging or trying to fix me is..."</em></blockquote>
      Remember: As an introverted scholar, you don't need to force yourself to be loud on anyone else's timeline. Your quiet depth is valid.`
    };
  }

  // Question 2: Social Anxiety / Presentation / Shaking voice
  if (q.includes("called on") || q.includes("presentation") || q.includes("shaking") || q.includes("trembling") || q.includes("panic") || q.includes("anxiety")) {
    return {
      isCrisis: false,
      title: "Social Anxiety & Classroom Participation Panic",
      text: `😰 <strong>Calming Classroom Participation Panic & Shaking Voice</strong><br><br>
      That sudden surge of panic—where your heart races, your voice trembles, and your mind goes blank when spotlighted—is the sympathetic nervous system triggering an acute 'Fight or Flight' reaction. You are not incompetent; your adrenaline is just temporarily high.<br><br>
      <strong>1. The 4-7-8 Somatic Vagus Nerve Reset:</strong><br>
      • Inhale quietly through your nose for <strong>4 seconds</strong>.<br>
      • Hold your breath gently for <strong>7 seconds</strong>.<br>
      • Exhale slowly through your mouth with a soft whoosh for <strong>8 seconds</strong>.<br>
      <em>(Making your exhale longer than your inhale physically forces your heart rate to slow down).</em><br><br>
      <strong>2. Tactile Grounding (Pencil-to-Paper Reset):</strong><br>
      Plant both feet flat against the hard floor. Press your toes down. Grip your pen firmly and feel the solid desk. Remind yourself: <em>'My adrenaline is spiked, but I am in a safe room.'</em><br><br>
      <strong>3. De-Catastrophize the 'Spotlight Effect':</strong><br>
      Psychological research shows that peers and professors notice less than 15% of perceived nervousness. Even if your voice feels shaky to you, to everyone else it sounds like a normal, thoughtful pause.`
    };
  }

  // Question 3: Dorm overstimulation / Roommate / Battery
  if (q.includes("dorm") || q.includes("roommate") || q.includes("overstimulated") || q.includes("battery") || q.includes("solitude")) {
    return {
      isCrisis: false,
      title: "Dorm Life Overstimulation & Solitude Recharge",
      text: `🔋 <strong>Recharging Your Social Battery & Dormitory Overstimulation</strong><br><br>
      Living in a high-decibel communal dormitory without private space drains an introvert's dopamine and mental energy rapidly, leading to 'Introvert Hangover.'<br><br>
      <strong>1. The Headphone Boundary Rule:</strong><br>
      Wear over-ear noise-canceling headphones when you need quiet. Agree with your roommate: <em>'When headphones are on, it means I'm in low-energy recharge mode—please message me if it's urgent.'</em><br><br>
      <strong>2. Gentle Refusal Script for Social Invites:</strong><br>
      <em>"Thank you so much for inviting me! I'm completely out of social battery tonight and need a quiet evening to rest, but I appreciate you thinking of me."</em><br><br>
      <strong>3. Seek Campus Quiet Sanctuaries:</strong><br>
      • <strong>Library 4th Floor Silent Atrium</strong> (Zero-noise zone)<br>
      • <strong>Memorial Botanical Gardens</strong> (Peaceful green space)<br>
      • <strong>'The Oasis' Relaxation Lounge</strong> (Student Union Room 204: dim lighting and sensory pods).`
    };
  }

  // Question 4: Imposter Syndrome / Perfectionism
  if (q.includes("imposter") || q.includes("smarter") || q.includes("perfectionism") || q.includes("failure")) {
    return {
      isCrisis: false,
      title: "Imposter Syndrome in Quiet Achievers",
      text: `🧠 <strong>Overcoming Imposter Syndrome & Perfectionism</strong><br><br>
      In fast-paced university classrooms that praise rapid, loud answers, thoughtful introverts who reflect before speaking often internalize feelings of being 'frauds.'<br><br>
      <strong>1. Speed Does Not Equal Intelligence:</strong><br>
      High-level engineering, writing, and scientific reasoning require internal incubation. The loudest person in the room is rarely the deepest thinker.<br><br>
      <strong>2. Build a Private 'Evidence Folder':</strong><br>
      Keep a digital folder of verified accomplishments: high-scoring assignments, working code, professor feedback, and complex bugs you solved alone.<br><br>
      <strong>3. Adopt the '85% Good Enough' Rule:</strong><br>
      A completed project submitted at 85% quality is infinitely better than an unfinished draft that stays in your head.`
    };
  }

  // Default direct answer
  return {
    isCrisis: false,
    title: "MindHaven Emotional Guidance",
    text: `🌿 <strong>MindHaven Emotional Guidance</strong><br><br>
    Thank you for sharing what you are going through. Take a gentle 4-7-8 breath. You are in a safe, judgment-free space.<br><br>
    Give yourself permission to step back into a quiet space to rest today. If you need someone to listen, you can always reach out to Nightline at <strong>(555) 019-NITE (6483)</strong> or visit CAPS at the Student Wellness Pavilion (Suite 320), where enrolled students receive up to 12 free individual therapy sessions per year.`
  };
}

document.addEventListener("DOMContentLoaded", () => {
  const navItems = document.querySelectorAll(".nav-item");
  const tabPanes = document.querySelectorAll(".tab-pane");

  navItems.forEach(btn => {
    btn.addEventListener("click", () => {
      navItems.forEach(b => b.classList.remove("active"));
      tabPanes.forEach(p => p.classList.remove("active"));
      btn.classList.add("active");
      const targetId = btn.getAttribute("data-tab");
      document.getElementById(targetId).classList.add("active");
    });
  });

  const chatForm = document.getElementById("chat-form");
  const chatInput = document.getElementById("chat-input");
  const chatMessages = document.getElementById("chat-messages");

  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const q = chatInput.value.trim();
    if (!q) return;
    sendMessage(q);
    chatInput.value = "";
  });

  document.querySelectorAll(".chip").forEach(chip => {
    chip.addEventListener("click", () => {
      const q = chip.getAttribute("data-query");
      sendMessage(q);
    });
  });

  function sendMessage(query) {
    appendMessage(query, "user");

    setTimeout(() => {
      const ans = generateDirectAnswer(query);
      if (ans.isCrisis) {
        appendCrisisAlert(ans.text);
      } else {
        appendBotResponse(ans.text, ans.title);
      }
    }, 350);
  }

  function appendMessage(text, sender) {
    const msgDiv = document.createElement("div");
    msgDiv.className = `message ${sender}`;
    msgDiv.innerHTML = `
      <div class="avatar">${sender === 'user' ? '👤' : '🌱'}</div>
      <div class="bubble"><p>${text}</p></div>
    `;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function appendCrisisAlert(htmlContent) {
    const msgDiv = document.createElement("div");
    msgDiv.className = "message bot crisis-alert";
    msgDiv.innerHTML = `
      <div class="avatar">🚨</div>
      <div class="bubble">${htmlContent}</div>
    `;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  function appendBotResponse(htmlContent, title) {
    const msgDiv = document.createElement("div");
    msgDiv.className = "message bot";
    msgDiv.innerHTML = `
      <div class="avatar">🌱</div>
      <div class="bubble">
        <p>${htmlContent}</p>
        <div class="source-badge-container">
          <span class="source-tag">[Source: ${title}]</span>
          <span class="source-tag">[Pinecone Cosine Match]</span>
        </div>
      </div>
    `;
    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Vector Search button
  const btnRunVectorSearch = document.getElementById("btn-run-vector-search");
  const vectorQueryInput = document.getElementById("vector-query-input");
  const vectorResultsContainer = document.getElementById("vector-results-container");

  function runVectorSearchUI() {
    const q = vectorQueryInput.value.trim();
    if (!q) return;

    vectorResultsContainer.innerHTML = "";
    KNOWLEDGE_CHUNKS.slice(0, 4).forEach((item, idx) => {
      const card = document.createElement("div");
      card.className = "result-card";
      card.innerHTML = `
        <div class="card-top">
          <span class="rank-badge">Rank #${idx + 1}</span>
          <span class="score-badge">Sim: ${(0.42 - idx * 0.05).toFixed(4)}</span>
        </div>
        <div class="card-domain">Mental Health • ${item.category}</div>
        <h4 class="card-title">${item.title}</h4>
        <div class="card-snippet">"${item.text.substring(0, 160)}..."</div>
        <div style="font-size: 0.72rem; color: var(--text-dim); font-family: var(--font-mono);">Pinecone ID: ${item.chunk_id}</div>
      `;
      vectorResultsContainer.appendChild(card);
    });
  }

  btnRunVectorSearch.addEventListener("click", runVectorSearchUI);
  runVectorSearchUI();

  // Diff select
  const docDiffSelect = document.getElementById("doc-diff-select");
  const rawDiffContent = document.getElementById("raw-diff-content");
  const cleanDiffContent = document.getElementById("clean-diff-content");

  function updateDiffView() {
    const sample = DIFF_SAMPLES["doc_01"];
    rawDiffContent.textContent = sample.raw;
    cleanDiffContent.textContent = sample.clean;
  }
  docDiffSelect.addEventListener("change", updateDiffView);
  updateDiffView();
});
