# API Contracts: RAG Chatbot Backend

This document specifies the API contracts for the FastAPI backend services.

## 1. Chat Endpoint

**Endpoint:** `/chat`
**Method:** `POST`
**Description:** Processes user queries and selected text to provide AI-generated answers with citations.

### Request Body: `ChatRequest`

```typescript
interface ChatRequest {
  query: string;            // The user's question
  selected_text?: string;   // Optional: text selected by the user for context
}
```

### Response Body: `ChatResponse`

```typescript
interface ChatResponse {
  answer: string;           // The AI-generated answer
  sources: string[];        // List of chapter/section titles as sources
}
```

### Error Responses:
- **400 Bad Request:** Invalid input or missing query.
- **500 Internal Server Error:** Backend processing failure.

## 2. Personalization Endpoint

**Endpoint:** `/personalize`
**Method:** `POST`
**Description:** Adapts chapter content based on user background.

### Request Body: `PersonalizationRequest`

```typescript
interface PersonalizationRequest {
  chapter_content: string;  // The original content of the chapter
  user_background: {
    software_background: string; // e.g., 'beginner', 'developer'
    hardware_background: string; // e.g., 'none', 'maker'
  }; // User's background information
}
```

### Response Body: `PersonalizationResponse`

```typescript
interface PersonalizationResponse {
  personalized_content: string; // The adapted chapter content
}
```

### Error Responses:
- **400 Bad Request:** Invalid input or missing parameters.
- **401 Unauthorized:** User not authenticated.
- **500 Internal Server Error:** Backend processing failure.

## 3. Translation Endpoint

**Endpoint:** `/translate`
**Method:** `POST`
**Description:** Translates chapter content to a specified target language.

### Request Body: `TranslationRequest`

```typescript
interface TranslationRequest {
  chapter_content: string;  // The original content of the chapter
  target_language: string;  // The language code to translate to (e.g., 'ur' for Urdu)
}
```

### Response Body: `TranslationResponse`

```typescript
interface TranslationResponse {
  translated_content: string; // The translated chapter content
}
```

### Error Responses:
- **400 Bad Request:** Unsupported target language or invalid input.
- **401 Unauthorized:** User not authenticated.
- **500 Internal Server Error:** Backend processing failure.
