import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def setup_database():
    if not DATABASE_URL:
        print("DATABASE_URL not found in .env. Please configure your database connection.")
        return

    conn = None
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()

        # Create users table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id VARCHAR(255) PRIMARY KEY,
                software_background TEXT,
                hardware_background TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Create chapters table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS chapters (
                id VARCHAR(255) PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                original_content TEXT, -- Store original content for personalization/translation
                metadata JSONB DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Create chunks table (for RAG)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS chunks (
                id VARCHAR(255) PRIMARY KEY,
                chapter_id VARCHAR(255) REFERENCES chapters(id),
                content TEXT NOT NULL,
                embedding VECTOR(384), -- Qdrant uses 384-dim embeddings for all-MiniLM-L6-v2
                metadata JSONB DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Create personalized_content table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS personalized_content (
                id SERIAL PRIMARY KEY,
                user_id VARCHAR(255) REFERENCES users(id),
                chapter_id VARCHAR(255) REFERENCES chapters(id),
                personalized_text TEXT NOT NULL,
                background_used TEXT, -- e.g., 'beginner', 'expert', or actual background string
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (user_id, chapter_id, background_used)
            );
        """)

        # Create translated_content table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS translated_content (
                id SERIAL PRIMARY KEY,
                user_id VARCHAR(255) REFERENCES users(id),
                chapter_id VARCHAR(255) REFERENCES chapters(id),
                translated_text TEXT NOT NULL,
                target_language VARCHAR(10) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE (user_id, chapter_id, target_language)
            );
        """)

        conn.commit()
        print("Database tables created successfully (or already exist).")

    except Exception as e:
        print(f"Error setting up database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    setup_database()
