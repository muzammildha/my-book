# Data Model: Textbook Generation Project

This document describes the data models used across the AI-generated textbook project.

## 1. User Profile

**Purpose:** Stores information about authenticated users for personalization.

```typescript
interface UserProfile {
  id: string;                 // Unique user ID from Better-Auth.com
  software_background: string; // e.g., 'beginner', 'intermediate', 'expert', 'developer'
  hardware_background: string; // e.g., 'none', 'maker', 'robotics_engineer'
  created_at: Date;           // Timestamp of user creation
}
```

**Storage:** Neon Serverless PostgreSQL `users` table.

## 2. Chapter Content

**Purpose:** Stores the original and potentially personalized/translated content of each chapter.

```typescript
interface ChapterContent {
  id: string;                 // Unique ID (e.g., filename slug)
  title: string;              // Chapter title
  content: string;            // Current rendered content (could be personalized/translated)
  original_content: string;   // Original AI-generated content
  metadata: Record<string, any>; // Additional chapter metadata
  created_at: Date;           // Timestamp of chapter creation
}
```

**Storage:** Neon Serverless PostgreSQL `chapters` table.

## 3. Content Chunk

**Purpose:** Stores small, semantically meaningful chunks of chapter content for RAG.

```typescript
interface ContentChunk {
  id: string;                 // Unique ID for the chunk (UUID)
  chapter_id: string;         // Foreign key to ChapterContent
  content: string;            // The text content of the chunk
  embedding: number[];        // Vector embedding (e.g., 384 dimensions)
  metadata: Record<string, any>; // Chunk-specific metadata (e.g., page number)
  created_at: Date;           // Timestamp of chunk creation
}
```

**Storage:** Qdrant Cloud Free Tier (vector store), with `chapter_id` and `content` mirrored in Neon Serverless PostgreSQL `chunks` table for reference/retrieval.

## 4. Personalized Content

**Purpose:** Stores personalized versions of chapter content for specific users.

```typescript
interface PersonalizedContent {
  id: number;                 // Primary key (serial)
  user_id: string;            // Foreign key to UserProfile
  chapter_id: string;         // Foreign key to ChapterContent
  personalized_text: string;  // The personalized version of the chapter text
  background_used: string;    // Description of background used for personalization (e.g., 'beginner')
  created_at: Date;           // Timestamp of personalization
}
```

**Storage:** Neon Serverless PostgreSQL `personalized_content` table.

## 5. Translated Content

**Purpose:** Stores translated versions of chapter content for specific users.

```typescript
interface TranslatedContent {
  id: number;                 // Primary key (serial)
  user_id: string;            // Foreign key to UserProfile
  chapter_id: string;         // Foreign key to ChapterContent
  translated_text: string;    // The translated version of the chapter text
  target_language: string;    // Target language code (e.g., 'ur' for Urdu)
  created_at: Date;           // Timestamp of translation
}
```

**Storage:** Neon Serverless PostgreSQL `translated_content` table.
