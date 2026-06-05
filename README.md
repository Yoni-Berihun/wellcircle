# WellaTribe

**Your tribe, your wellness. Right where you chat.**

A Telegram Mini App connecting individuals and corporate teams to verified wellness providers across Ethiopia. WellaTribe solves a two-sided market problem: consumers lack a single discovery and accountability layer for wellness services, while providers have no efficient digital channel to reach them.

---

## 🎯 Mission

Close the gap between wanting to be healthy and actually doing it. WellaTribe embeds accountability and discovery directly inside Telegram, where Ethiopian users already spend hours daily, making wellness social, measurable, and accessible.

---

## 🚀 What We're Building

**For Consumers:**
- Discover verified wellness providers (gyms, yoga studios, nutritionists, therapists) in Addis Ababa
- Join Community Spaces with friends and colleagues for accountability
- Check in, earn Legacy Points, and watch your progress in real time
- Book services and pay via Telebirr or M-Pesa—all inside Telegram

**For Providers:**
- Access a pre-built community channel on the most popular messaging platform in Ethiopia
- Watch real-time metrics: member count, bookings, engagement
- Convert your existing Telegram community into a revenue-generating channel
- Prove ROI without hiring a marketing agency

---

## 💡 Core Features (MVP)

| Feature | Status | Why It Matters |
|---------|--------|-----------------|
| **Community Spaces + Live Feed** | ✅ MUST SHIP | The core demo loop—users join, see live activity, feel accountability |
| **Provider Marketplace Browse** | ✅ MUST SHIP | Inventory visibility; drive discovery of real partners |
| **One-tap Booking Flow** | ✅ MUST SHIP | Demo CTA—shows conversion path |
| **Telebirr Payment Integration** | ✅ MUST SHIP | Proves real money; Telebirr is the dominant ETB payment rail |
| **M-Pesa Payment (Daraja STK Push)** | ✅ MUST SHIP | Cross-border proof of concept |
| **Legacy Points Engine** | ✅ MUST SHIP | Gamification—drives repeat check-ins and retention |
| **Provider Dashboard** | ✅ MUST SHIP | ROI proof for partners—live member count, bookings, revenue |
| **Telegram Auth** | ✅ MUST SHIP | Required for Mini App; zero friction |

#### Coming Soon (Post-Hackathon)
- Legacy Points Decay Logic  
- Full Booking + Payment End-to-End  
- B2B / Corporate Wellness UI  
- Full Rewards Marketplace  
- Group Savings Pools & Auto-split  

---

## 🛠️ Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Frontend** | React + Vite | Fast builds; seamless Telegram SDK integration |
| **Backend** | Python FastAPI | Async support; team comfort; ideal for polling endpoints |
| **Database** | PostgreSQL (Supabase) | Real-time capable; free tier; instant setup |
| **Auth** | Telegram initData HMAC | No passwords; zero friction; native Mini App |
| **Payments** | Telebirr + M-Pesa Daraja | Primary: Telebirr (highest ETB adoption); Secondary: M-Pesa (cross-border) |
| **Scheduler** | APScheduler (in-process) | Points decay jobs; no Redis needed for MVP |
| **Hosting** | Railway (backend) + Vercel (frontend) | Free tier; deploy in < 10 min |
| **No-Code** | Softr or Glide | B2B placeholder screens |

---

## 👥 Target Audience

### Primary (Demo Day)
- **Wellness Providers** in Ethiopia seeking digital customer acquisition and retention tools
- Confirmed partnership: Real Addis Ababa gyms, yoga studios, nutritionists

### Secondary (Post-Launch)
- **Individual Users** 18–45 in Addis Ababa seeking wellness accountability and community
- **Corporate HR Managers** running team wellness programs
- **Telegram Users in Ethiopia** already accustomed to group coordination via Telegram

---

## 📐 Problem Statement

### Consumer Painpoints
1. **Provider Fragmentation** — Hundreds of wellness SMEs in Addis Ababa operate on Telegram DMs or word-of-mouth; no central discovery
2. **Group Coordination Chaos** — Manual Telebirr splits collapse into confusion; no accountability tracking
3. **Consistency Failure** — High awareness of healthy habits; low follow-through due to lack of social friction

### Provider Painpoints
1. **Zero Discovery Infrastructure** — No CRM, booking system, or pipeline beyond word-of-mouth
2. **No B2B Access** — Cannot tap corporate wellness budgets at scale
3. **No Data** — Cannot measure engagement, retention, or community health

### Core Insight
**The gap is not between knowing and wanting — it is between wanting and doing.**

---

## 🎬 Demo Script (5 Minutes)

### Act 1: The Problem (30s)
Open side-by-side: chaotic WhatsApp group vs. WellaTribe. "This is how your customers find you today. Here is what we built instead."

### Act 2: Consumer Experience (90s)
- Open Telegram → bot link → WellaTribe (no download)
- Explore → show real partner photos, services, ETB pricing
- Browse Community Spaces → join with one tap
- Check in → toast: +10 Legacy Points + live feed event

### Act 3: The Money (60s)
- Book Now → select service → select time → pay via Telebirr
- Confirm phone → Telebirr OTP/redirect triggers
- Payment confirms → booking card appears

### Act 4: Provider ROI (90s)
- Switch to Provider Dashboard
- Show KPI cards: community members, new joins today, bookings
- Show bookings table with the just-made booking
- **"Every customer join, right here in real time. No marketing agency. No Instagram spend."**

### Act 5: Vision Close (30s)
Flash Phase 2/3 roadmap slides. End on tagline: *Your tribe, your wellness. Right where they chat.*

---

## 🏗️ Hackathon Build Timeline (1-Day Sprint)

| Hours | Backend | Frontend | No-Code |
|-------|---------|----------|---------|
| **1–2** | FastAPI scaffold + Supabase + Telegram auth | Telegram shell + nav + theme vars | Softr/Glide setup |
| **3–4** | Providers API + Communities API + seed data | Home + Explore + Provider detail | B2B content seed |
| **5–6** | Community join/check-in/feed endpoints | Community list + detail + live feed | Polish screens |
| **7–8** | Telebirr + M-Pesa + booking endpoints | Booking flow + payment screens | Hand off mockups |
| **9–10** | Provider dashboard stats + payment callbacks | Provider dashboard full build | — |
| **11–12** | Points decay + bug fixes + tests | Profile + polish + tests | — |
| **Final 30 min** | Deploy to Railway + smoke test | Deploy to Vercel + bot config + smoke test | — |

**Key Principle:** Backend unblocks frontend by Hour 4. After that, integration only.

---

## ✅ Success Criteria (Definition of Done)

### Hackathon Day
- ✅ Real user can open WellaTribe from Telegram bot link  
- ✅ User can join community and see member count increment  
- ✅ User can check in and see Legacy Points update  
- ✅ User can initiate Telebirr payment and complete OTP/redirect  
- ✅ Provider can view dashboard and see live member joins  

### 90-Day Targets
- **Provider Listings:** 10+ verified Addis Ababa partners  
- **Monthly Active Users:** 500 MAU  
- **Community Join Rate:** 60% of users join 1+ community  
- **Daily Check-in Rate:** 25% DAU  
- **Telebirr Bookings:** 50+ paid bookings/month  
- **Provider Dashboard Sessions:** 3+ sessions/provider/week  

---

## 🗂️ Data Models (PostgreSQL)

- **users** — Telegram-authenticated profiles, points balance, check-in history
- **providers** — Verified wellness providers (gyms, yoga, nutrition, spa, therapy)
- **communities** — Topic or provider-linked groups; member counts; live feeds
- **bookings** — Service reservations; payment method & status; Telebirr/M-Pesa refs
- **community_feed_events** — Activity stream (joins, check-ins, bookings) for real-time polling

---

## 🚫 Out of Scope (Post-Hackathon)

- Tribe Vault / group wallet / auto-split payments
- Full Legacy Points redemption marketplace
- Corporate Benefits Portal
- Rotating Wellness Savings Pool
- Targeted ad network
- Push notifications
- Provider self-onboarding (manual seed for hackathon)

---

## 🌍 Market Context

**Location:** Ethiopia / Addis Ababa  
**Currency:** Ethiopian Birr (ETB)  
**Platform:** Telegram (dominant messaging app in Ethiopia)  
**Hackathon:** 1-day sprint with frontend + backend teams  
**Demo Audience:** Wellness provider partners seeking concrete ROI evidence  

---

## 📖 Project Identity

| Element | Meaning |
|---------|---------|
| **WellaTribe** | "Wella" (Well + wellness) + Amharic resonance; "Tribe" (community-first positioning, mirrors Telegram's group culture) |
| **Tagline** | *Your tribe, your wellness. Right where you chat.* |
| **Demo Persona** | Meron, 28-year-old HR manager in Addis Ababa discovering yoga + joining corporate wellness community |

---

## 📞 Getting Started

### Prerequisites
- Node.js (v18+) for frontend
- Python 3.9+ for backend
- Telegram Bot API key (@BotFather)
- Supabase account (free tier)
- Telebirr & M-Pesa sandbox credentials

### Installation (Coming Soon)

Detailed setup instructions for local development will be added as the project structure evolves.

---

## 📞 Questions?

For more information about the project vision, feature roadmap, or partnership opportunities, refer to the full PRD document or reach out to the team.

---

**WellaTribe v1.0 | Hackathon Build | Confidential**