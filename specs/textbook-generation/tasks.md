# Task Breakdown: Textbook Generation Project

This document outlines the detailed tasks for implementing the AI-generated textbook project.

## Phase 1: MVP - Book Creation & Basic UI

**User Story 1:** As a student, I want to access a structured online textbook on Physical AI and Humanoid Robotics so that I can learn the foundational concepts.

### Tasks:
- **T001:** Set up Docusaurus project in `physical-ai-textbook/` directory.
  - **Acceptance Criteria:** Docusaurus is initialized with TypeScript, `package.json` and `tsconfig.json` are present, and basic Docusaurus pages render.
- **T002:** Configure `physical-ai-textbook/docusaurus.config.ts`.
  - **Acceptance Criteria:** Project title, tagline, URL, baseUrl, GitHub organization/project names, i18n locales (en, ur), and editUrl are updated. Blog preset removed. Navbar and footer links are updated.
- **T003:** Configure `physical-ai-textbook/sidebars.ts`.
  - **Acceptance Criteria:** Sidebar explicitly lists introductory chapters, modules 1-4, and capstone in correct order.
- **T004:** Create initial book content MDX files in `physical-ai-textbook/docs/`.
  - **Acceptance Criteria:** `index.mdx`, `introduction-to-physical-ai.mdx`, `basics-of-humanoid-robotics.mdx`, `module-01/index.mdx`, `module2/index.mdx`, `module3/index.mdx`, `module4/index.mdx`, `capstone-ai-robot-pipeline.mdx` exist with placeholder content. `_category_.json` files created for modules with correct labels and positions.
- **T005:** Develop initial Docusaurus custom components structure.
  - **Acceptance Criteria:** `physical-ai-textbook/src/components/` and `physical-ai-textbook/src/theme/` directories are set up for future component development.

## Phase 2: RAG Chatbot Integration

**User Story 2:** As a student, I want to ask questions about the textbook content and receive accurate answers with citations so that I can deepen my understanding.

### Tasks:
- **T006:** Set up FastAPI project in `rag_chatbot/` directory.
  - **Acceptance Criteria:** `rag_chatbot/src/main.py` is created with basic FastAPI app. `requirements.txt`, `.env.example`, `LICENSE`, `.gitignore` are present.
- **T007:** Create database schema using `rag_chatbot/scripts/setup_db.py`.
  - **Acceptance Criteria:** `users`, `chapters`, `chunks`, `personalized_content`, `translated_content` tables are created in Neon Postgres (or local equivalent).
- **T008:** Develop RAG service (`rag_chatbot/src/services/rag_service.py`).
  - **Acceptance Criteria:** `RAGService` class is implemented to interface with Qdrant and OpenAI Agents. Text chunking and embedding logic is functional.
- **T009:** Implement API endpoints (`rag_chatbot/src/api/endpoints.py`).
  - **Acceptance Criteria:** `/chat`, `/personalize`, `/translate` endpoints are defined. Mock responses are functional. Integrates `RAGService` and other future services.
- **T010:** Ingest book content into Neon Postgres and Qdrant using `rag_chatbot/scripts/index_chapters.py`.
  - **Acceptance Criteria:** All MDX chapters are chunked, embedded, and stored in Qdrant and associated metadata in Neon.
- **T011:** Create a Docusaurus React component for the Chatbot UI.
  - **Acceptance Criteria:** A basic chat interface is rendered on Docusaurus, capable of sending queries to the FastAPI `/chat` endpoint and displaying responses.
- **T012:** Implement text selection functionality in Docusaurus.
  - **Acceptance Criteria:** Users can select text, and an "Ask AI" button appears, sending the selected text to the `/chat` endpoint as `selected_text`.

## Phase 3: Authentication & Personalization

**User Story 3:** As a logged-in student, I want personalized content based on my background so that the textbook is more relevant to my learning needs.

### Tasks:
- **T013:** Integrate Better-Auth.com SDK into Docusaurus frontend.
  - **Acceptance Criteria:** Signup/Signin forms are functional. User authentication state is managed.
- **T014:** Modify signup flow to capture user background.
  - **Acceptance Criteria:** During signup, users are prompted for software/hardware background, and this data is stored in the `users` table in Neon Postgres.
- **T015:** Develop personalization service (`rag_chatbot/src/services/personalization_service.py`).
  - **Acceptance Criteria:** `PersonalizationService` adapts chapter content based on user background using an AI model.
- **T016:** Integrate personalization service with `/personalize` endpoint.
  - **Acceptance Criteria:** The `/personalize` endpoint calls the `PersonalizationService` and returns adapted content.
- **T017:** Create Docusaurus React component for "Personalize Chapter" button.
  - **Acceptance Criteria:** Button exists at chapter start. On click, it sends current chapter content and user background to `/personalize` and dynamically updates chapter view.

## Phase 4: Urdu Translation

**User Story 4:** As a logged-in student, I want to translate chapter content to Urdu so that I can read the textbook in my preferred language.

### Tasks:
- **T018:** Develop translation service (`rag_chatbot/src/services/translation_service.py`).
  - **Acceptance Criteria:** `TranslationService` translates chapter content to Urdu using an AI model or translation API.
- **T019:** Integrate translation service with `/translate` endpoint.
  - **Acceptance Criteria:** The `/translate` endpoint calls the `TranslationService` and returns Urdu content.
- **T020:** Create Docusaurus React component for "Translate to Urdu" button.
  - **Acceptance Criteria:** Button exists at chapter start. On click, it sends current chapter content to `/translate` and dynamically updates chapter view with Urdu text.

## Phase 5: Reusable Intelligence & CI/CD

**User Story 5:** As a developer, I want automated tools for content generation, deployment, and indexing so that I can efficiently manage the textbook project.

### Tasks:
- **T021:** Develop `book-writer` Claude Code Subagent.
  - **Acceptance Criteria:** Subagent can iteratively generate/update textbook content based on prompts.
- **T022:** Develop `docusaurus-configurator` Claude Code Subagent.
  - **Acceptance Criteria:** Subagent can manage Docusaurus configurations (e.g., add new chapters to sidebar).
- **T023:** Create `deploy-docusaurus` Agent Skill.
  - **Acceptance Criteria:** Skill automates `npm run build` and `npm run deploy` for GitHub Pages.
- **T024:** Create `update-rag-embeddings` Agent Skill.
  - **Acceptance Criteria:** Skill automates re-indexing book content in Qdrant after updates.
- **T025:** Configure GitHub Actions for Docusaurus deployment.
  - **Acceptance Criteria:** `frontend-deploy.yml` workflow deploys Docusaurus to GitHub Pages on pushes to `main` (or designated branch).
- **T026:** Configure GitHub Actions for FastAPI backend deployment.
  - **Acceptance Criteria:** `backend-deploy.yml` workflow deploys FastAPI to Railway/Render on pushes to `main` (or designated branch).
- **T027:** Implement code quality checks in CI/CD.
  - **Acceptance Criteria:** `test.yml` workflow runs ESLint, Prettier, Ruff, and TypeScript checks on PRs.

## Phase 6: Testing & Documentation

### Tasks:
- **T028:** Implement frontend tests (`physical-ai-textbook/`).
  - **Acceptance Criteria:** `npm test` runs successfully, covering core UI components and interactions.
- **T029:** Implement backend tests (`rag_chatbot/tests/`).
  - **Acceptance Criteria:** `pytest tests/ --cov=app` runs successfully, covering API endpoints and service logic.
- **T030:** Finalize `README.md` and other project documentation.
  - **Acceptance Criteria:** `README.md`, `DEPLOYMENT.md`, `PRODUCTION_CHECKLIST.md`, `ENVIRONMENT_VARIABLES.md` are complete and accurate.

