# The AI Roadmap for Detours
*Prabh's Vision: Full-Stack AI-Powered Fleet SaaS — Ontario Transport Industry*
*Created: 2026-03-29*

---

## The Foundation (Already Built)

| Component | Status |
|-----------|--------|
| Live GPS fleet tracking | Done |
| Driver inspection + POD records | Done |
| Dispatch, invoicing, payroll | Done |
| Multi-tenant (owner + driver roles) | Done |
| Supabase + Vercel + React | Done |

---

## Phase 1 — NLP & Embeddings (Current Learning)
*Timeline: Now*

| Skill Being Learned | App Feature It Unlocks |
|--------------------|----------------------|
| Word Embeddings / NLP | Smart job search, driver notes analysis |
| Sentence Transformers | Match drivers to jobs by skills/location semantically |
| Text Classification | Auto-categorize incidents, flag safety reports |

### Milestone Files
- `vocabulary.py` — One-hot encoding basics ✅
- `word2vec.py` — Pretrained GloVe embeddings ✅
- `full-pipeline.py` — NLP preprocessing pipeline ✅
- `train_word2vec.py` — Train Word2Vec from scratch ← **In Progress**
- `sentence_embeddings.py` — Sentence-level embeddings ← **Next**

---

## Phase 2 — Predictive ML & Anomaly Detection
*Timeline: 3–6 Months*

| Skill | App Feature |
|-------|-------------|
| Time series / forecasting | Predict busy routes, driver demand by day/hour |
| Anomaly detection | Flag unusual driver speed, route deviation alerts |
| RAG pipeline | "Ask your fleet" — owner queries their own data in plain English |
| Clustering (K-Means) | Group similar jobs, identify route patterns |
| Regression models | Estimate job duration based on distance + driver history |

### Key Datasets Available in Detours
- GPS location history (lat/lng, speed, heading, timestamps)
- Job completion records (pickup, delivery, duration)
- Driver inspection results (pass/fail patterns)
- Invoice history (customer, amount, frequency)
- Payroll / settlement records

---

## Phase 3 — Full AI-Powered SaaS
*Timeline: 6–12 Months*

### AI Dispatch Agent
> Automatically assigns the best driver to a job based on:
> - Current GPS location (closest available driver)
> - Driver availability and hours of service
> - Past performance score
> - Vehicle type requirements
> - Real-time traffic conditions

**Tech:** Claude API + function calling + Supabase real-time

---

### Compliance Copilot (Ontario MTO)
> Monitors Ontario MTO rules and keeps fleet compliant automatically:
> - CVOR record monitoring
> - Daily pre-trip inspection reminders
> - Hours of service tracking and alerts
> - License/insurance expiry warnings (30/7/1 day alerts)
> - Auto-fills inspection report fields

**Tech:** Fine-tuned classifier on MTO regulations + RAG over rulebook

---

### Revenue Forecasting
> Predicts monthly revenue and cash flow based on:
> - Historical job volume by week/month
> - Seasonal patterns in Ontario (winter slowdowns, construction season peaks)
> - Customer booking frequency

**Tech:** Time series model (Prophet or LSTM)

---

### Driver Risk Scoring
> ML model scores each driver's safety profile:
> - GPS speed anomalies
> - Harsh braking/acceleration patterns
> - Inspection failure history
> - Late delivery rate

**Tech:** Gradient Boosting (XGBoost) on historical driver data

---

### "Ask Your Fleet" — Claude API Chatbot
> Owner types in plain English:
> - *"Who had the most late deliveries this month?"*
> - *"Which truck needs maintenance next?"*
> - *"What was my revenue last quarter vs this quarter?"*
> - *"Which driver has the best safety record?"*
>
> Claude queries Supabase and returns a clear, conversational answer.

**Tech:** Claude API + tool use + Supabase function calls

---

### Smart Job Matching
> When a new job comes in, the system suggests the best driver:
> - Semantic matching on job description vs driver skills
> - Location proximity scoring
> - Availability check

**Tech:** Sentence Transformers (`all-MiniLM-L6-v2`) + cosine similarity

---

## Ontario Transport Industry Opportunity

| Pain Point | Current State | Detours AI Solution |
|------------|--------------|---------------------|
| MTO compliance | Manual, paper-based | Auto-monitoring + alerts |
| Driver dispatch | Phone calls / manual | AI auto-assignment |
| CVOR management | Spreadsheets | Real-time risk dashboard |
| Hours of service | Paper logs | Automated tracking |
| Fleet maintenance | Reactive | Predictive scheduling |
| Revenue forecasting | Guesswork | ML-powered predictions |

> **Target Market:** Small fleets (5–50 trucks) in Ontario — completely underserved by existing software.
> No major SaaS player owns this space. Detours can own it.

---

## Learning → Building Connection

```
Word Embeddings     →  Driver-to-job semantic matching
Sentence Transformers → "Ask your fleet" search
Text Classification  →  Incident categorization
Time Series          →  Revenue & demand forecasting
Anomaly Detection    →  Driver safety alerts
RAG Pipeline         →  Claude API chatbot over fleet data
Claude API           →  Compliance Copilot + Dispatch Agent
```

---

## The Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React + TypeScript |
| Backend | Supabase (PostgreSQL + Auth + Realtime) |
| Deployment | Vercel |
| AI/ML Models | Python (scikit-learn, PyTorch, gensim) |
| AI Agent Layer | Claude API (Anthropic) |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector Search | Supabase pgvector extension |
| Monitoring | Sentry + custom audit log table |

---

## Immediate Next Step

1. Complete `train_word2vec.py` — understand how embeddings are trained
2. Build `sentence_embeddings.py` — sentence-level understanding
3. Build **first AI feature in Detours**: driver-to-job semantic matching prototype
4. Integrate Claude API into Detours for the "Ask your fleet" chatbot

> **This is the moment your ML learning and your SaaS collide.**

---

*Prabh Sharan | Detours Fleet SaaS | Ontario, Canada*
*GitHub: Prabh101726 | Repo: Claude-Data-and-Learning*
