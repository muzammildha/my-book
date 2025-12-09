import React, { useState, useEffect, useRef } from 'react';

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [threadId, setThreadId] = useState(null); // Store thread_id for continuity
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  // Load threadId from localStorage on component mount
  useEffect(() => {
    const storedThreadId = localStorage.getItem('chatbotThreadId');
    if (storedThreadId) {
      setThreadId(storedThreadId);
    }
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newUserMessage = { role: 'user', content: input };
    setMessages((prevMessages) => [...prevMessages, newUserMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch('/api/chat', { // Your FastAPI URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ thread_id: threadId, user_message: input }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setThreadId(data.thread_id); // Update threadId for subsequent messages
      localStorage.setItem('chatbotThreadId', data.thread_id); // Persist threadId

      const newAssistantMessages = data.assistant_messages.map(content => ({ role: 'assistant', content }));
      setMessages((prevMessages) => [...prevMessages, ...newAssistantMessages]);

    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prevMessages) => [...prevMessages, { role: 'system', content: 'Error: Could not get a response.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', height: '400px', display: 'flex', flexDirection: 'column' }}>
      <div style={{ flexGrow: 1, overflowY: 'auto', marginBottom: '10px' }}>
        {messages.map((msg, index) => (
          <div key={index} style={{ textAlign: msg.role === 'user' ? 'right' : 'left', margin: '5px 0' }}>
            <strong>{msg.role === 'user' ? 'You' : 'Assistant'}:</strong> {msg.content}
          </div>
        ))}
        {loading && <p>Assistant is typing...</p>}
        <div ref={messagesEndRef} />
      </div>
      <div style={{ display: 'flex' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => { if (e.key === 'Enter') sendMessage(); }}
          placeholder="Type your message..."
          style={{ flexGrow: 1, padding: '8px' }}
          disabled={loading}
        />
        <button onClick={sendMessage} disabled={loading} style={{ marginLeft: '10px', padding: '8px 15px' }}>
          Send
        </button>
      </div>
    </div>
  );
}

export default Chatbot;
