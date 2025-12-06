# Feature Specification: Textbook Generation

This document specifies the requirements for the AI-generated textbook project.

## 1. Overview

Create a comprehensive textbook on "Physical AI & Humanoid Robotics Course" using AI, Docusaurus, and deploy it to GitHub Pages. Include an integrated RAG chatbot, user authentication with personalization, and Urdu translation.

## 2. Core Deliverables (MVP)

### 2.1. AI/Spec-Driven Book Creation
- **Objective:** Generate a complete textbook using AI.
- **Technology:** Docusaurus for frontend, GitHub Pages for deployment.
- **Content:** 6 structured chapters with clean, professional content.
- **UI:** Responsive, fast page loads (<2s), mobile-friendly.

### 2.2. Integrated RAG Chatbot
- **Objective:** Embed a chatbot within the book to answer content-related questions.
- **Technology:** OpenAI Agents/ChatKit SDKs, FastAPI backend, Neon Serverless Postgres, Qdrant Cloud Free Tier.
- **Capabilities:** Semantic search, source citations, zero hallucination, rate limiting.
- **Feature:** Answer questions based on user-selected text.

## 3. Bonus Features (Future Phases)

### 3.1. Reusable Intelligence
- **Objective:** Create Claude Code Subagents and Agent Skills.
- **Benefit:** Streamline development tasks.

### 3.2. Signup/Signin with Personalization
- **Objective:** Implement user authentication.
- **Technology:** Better-Auth.com.
- **Feature:** Collect user's software/hardware background during signup.

### 3.3. Content Personalization
- **Objective:** Allow logged-in users to personalize chapter content.
- **Mechanism:** Button at chapter start, AI-driven content adaptation.

### 3.4. Urdu Translation
- **Objective:** Allow logged-in users to translate chapter content to Urdu.
- **Mechanism:** Button at chapter start, AI/API-driven translation.

## 4. Architectural Overview

- **Frontend:** Docusaurus (React, TypeScript), deployed on GitHub Pages.
- **Backend:** FastAPI (Python) for RAG, personalization, translation APIs.
- **Databases:** Neon PostgreSQL (metadata, user data), Qdrant (vector embeddings).
- **AI:** Claude Code (for book generation, subagents/skills), OpenAI (for RAG, personalization).

## 5. Non-Functional Requirements

- **Performance:** Frontend FCP <1.5s, TTI <3s. Backend API p95 <2s, p50 <1s.
- **Scalability:** Leverage serverless and free-tier services.
- **Security:** Standard web security practices, secure user data handling.
- **Maintainability:** Modular architecture, clear code standards.

## 6. Definitions

- **Physical AI:** AI systems interacting with the physical world.
- **Humanoid Robotics:** Robots mimicking human form and movement.
- **RAG:** Retrieval-Augmented Generation.
- **Docusaurus:** Static site generator for documentation.
- **FastAPI:** Modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Neon:** Serverless PostgreSQL database.
- **Qdrant:** Vector similarity search engine.

## 7. Open Questions/Ambiguities

- Specifics of user background questions for personalization.
- Choice of third-party translation API for Urdu.

