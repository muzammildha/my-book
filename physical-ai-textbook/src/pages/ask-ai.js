import React from 'react';
import Layout from '@theme/Layout';

function AskAi() {
  return (
    <Layout title="Ask AI about the Book" description="Ask questions about the Physical AI & Humanoid Robotics textbook.">
      <main className="container margin-vert--lg">
        <h1>Ask AI about the Book</h1>
import Chatbot from '@site/src/components/Chatbot';
        <p>This is where the RAG chatbot will be integrated.</p>
        <Chatbot />
      </main>
    </Layout>
  );
}

export default AskAi;
