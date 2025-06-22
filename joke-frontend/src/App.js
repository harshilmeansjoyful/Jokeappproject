import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [joke, setJoke] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const fetchJoke = async () => {
    setLoading(true);
    setError('');
    
    try {
      const response = await fetch('http://localhost:8000/joke');
      if (!response.ok) {
        throw new Error('Failed to fetch joke');
      }
      const data = await response.json();
      setJoke(data.joke);
    } catch (err) {
      setError('Failed to load joke. Make sure the backend is running!');
      console.error('Error fetching joke:', err);
    } finally {
      setLoading(false);
    }
  };

  // Fetch initial joke when component mounts
  useEffect(() => {
    fetchJoke();
  }, []);

  return (
    <div className="app">
      <div className="container">
        
        {/* Header */}
        <div className="header">
          <h1>🎭 Random Joke Generator</h1>
          <p>Get a fresh dose of humor with every click!</p>
        </div>

        {/* Joke Display Area */}
        <div className="joke-container">
          {loading ? (
            <div className="loading">
              <div className="spinner"></div>
              <span>Loading a joke for you...</span>
            </div>
          ) : error ? (
            <div className="error">
              <p className="error-message">😅 {error}</p>
              <p className="error-hint">
                Make sure your FastAPI backend is running on localhost:8000
              </p>
            </div>
          ) : (
            <p className="joke-text">"{joke}"</p>
          )}
        </div>

        {/* Action Buttons */}
        <div className="buttons">
          <button
            onClick={fetchJoke}
            disabled={loading}
            className="btn btn-primary"
          >
            {loading ? 'Loading...' : '🎲 Get New Joke'}
          </button>
          
          <button
            onClick={() => window.location.reload()}
            className="btn btn-secondary"
          >
            🔄 Refresh Page
          </button>
        </div>

        {/* Footer */}
        <div className="footer">
          <p>Powered by FastAPI + React</p>
          <p>Backend running on localhost:8000</p>
        </div>
      </div>
    </div>
  );
}

export default App;