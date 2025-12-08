import React, { useState } from 'react';
import styles from './Chatbot.module.css'; // Assuming you'll create a CSS module for styling

function Chatbot() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('Ask me anything about the Physical AI & Humanoid Robotics textbook!');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await fetch('/api/ask', { // Vercel will route /api/ask to your FastAPI function
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: query }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error('Error fetching chatbot response:', error);
      setResponse('Sorry, something went wrong. Please try again.');
    } finally {
      setLoading(false);
    }
    setQuery('');
  };

  return (
    <div className={styles.chatbotContainer}>
      <div className={styles.responseDisplay}>{response}</div>
      <form onSubmit={handleSubmit} className={styles.queryForm}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask a question..."
          disabled={loading}
          className={styles.queryInput}
        />
        <button type="submit" disabled={loading} className={styles.submitButton}>
          {loading ? 'Thinking...' : 'Ask'}
        </button>
      </form>
    </div>
  );
}

export default Chatbot;
