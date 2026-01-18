<h1 align="center">🚀 LinkedIn Content Assistant using GenAI</h1>

<p align="center">
  <i>Write better LinkedIn posts. Rewrite smarter. Sound human — not AI.</i>
</p>

<p align="center">
  Empowering professionals to generate and refine LinkedIn content using real creator styles, few-shot prompting, and GenAI.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GenAI-LangChain-blue" />
  <img src="https://img.shields.io/badge/LLM-Groq%20%7C%20LLaMA-green" />
  <img src="https://img.shields.io/badge/UI-Streamlit-red" />
  <img src="https://img.shields.io/badge/Focus-Real%20World%20Usecase-orange" />
</p>

---

## 🧠 Why This Project?

Most people don’t struggle on LinkedIn because they lack ideas.  
They struggle because they don’t know **how to structure, phrase, and present** their thoughts confidently.

This project bridges that gap.

Instead of generating generic AI content, this assistant:
- Learns from **real LinkedIn creators**
- Uses **high-performing posts as guidance**
- Produces content that feels *clear, grounded, and human*

---

## ✨ Features

### 📝 Generate LinkedIn Posts
Create posts by selecting:
- **Topic (Tag)** – Motivation, Mental Health, Career, etc.
- **Length** – Short / Medium / Long
- **Language** – English or Hinglish
- **Creator Style** – Inspired by real creators’ writing patterns

Generated posts:
- Follow natural paragraph breaks
- Match tone and pacing
- Avoid robotic AI phrasing

---

### ✍️ Rewrite My Post (High-Value Feature)
Paste your own LinkedIn draft and:
- Rewrite it in a chosen creator’s style
- Preserve the **original message**
- Improve clarity, flow, and engagement
- Control length and language

This is especially useful for:
- Job seekers
- Founders
- Creators posting consistently
- Professionals improving visibility

---

## 🧩 How It Works (High Level)

1. **Creator Datasets**
   - Real LinkedIn posts stored as structured JSON
   - Each post includes:
     - Text
     - Engagement score
     - Line count
     - Language
     - Tags

2. **Preprocessing**
   - Length classification (Short / Medium / Long)
   - Tag normalization
   - Engagement analysis

3. **Few-Shot Prompting**
   - Only **high-quality examples** are used
   - Example selection logic:
     - Engagement ≥ dataset median **OR**
     - Tag matches selected topic

4. **LLM Generation**
   - Dynamically constructed prompts
   - No preambles, no filler text
   - Output optimized for LinkedIn readability

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Groq (LLaMA-based models)**
- **Streamlit**
- **Pandas**
- **Few-shot Prompting**
- **Prompt Engineering**

---

## 🎯 What Makes This Different?

✔ Uses **real creator data**, not synthetic samples  
✔ Implements **few-shot prompting properly**  
✔ Filters examples using **engagement intelligence**  
✔ Solves a **real LinkedIn content problem**  
✔ Built with production-style modular design  

This is not a toy GenAI app — it’s a **practical writing assistant**.

---

## 🚀 Future Enhancements

- **LinkedIn Profile URL Ingestion**  
  Users will be able to paste a LinkedIn profile URL directly into the app.  
  The backend will automatically:
  - Scrape recent posts from the profile  
  - Clean and normalize the content  
  - Enrich it with metadata (tags, tone, length, engagement signals)  
  - Convert it into a structured JSON dataset  

- **Automatic Style Adaptation**  
  Once posts are ingested, the system will:
  - Learn the creator’s writing patterns
  - Use them for few-shot prompting
  - Generate new posts that closely match the creator’s tone, structure, and pacing

- **Dynamic Creator Profiles**  
  Instead of hardcoded creators, the app will support:
  - On-the-fly creator addition
  - Temporary or persistent creator profiles
  - Personalized content generation per user

- **Advanced Post Controls**  
  Planned enhancements include:
  - Tone sliders (reflective, motivational, direct)
  - Audience targeting (students, professionals, founders)
  - Engagement-optimized rewrites based on historical performance

These features will transform the project from a static generator into a **dynamic, creator-aware LinkedIn content engine**.


---

## 🙌 Final Note

This project represents my hands-on learning with **GenAI, LangChain, and LLM systems**, focused on **real-world usefulness rather than hype**.

If you’ve ever stared at LinkedIn thinking  
*“How do I say this better?”* — this tool is built for that moment.
