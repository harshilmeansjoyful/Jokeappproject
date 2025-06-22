from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
from pydantic import BaseModel

app = FastAPI(title="Random Joke API", version="1.0.0")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # React dev servers
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hardcoded jokes collection
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't eggs tell jokes? They'd crack each other up!",
    "I invented a new word: Plagiarism!",
    "Why did the scarecrow win an award? He was outstanding in his field!",
    "What do you call a fake noodle? An impasta!",
    "Why did the coffee file a police report? It got mugged!",
    "How do you organize a space party? You planet!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "What did the ocean say to the beach? Nothing, it just waved!",
    "Why did the bicycle fall over? Because it was two tired!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the math book look so sad? Because it had too many problems!",
    "What's orange and sounds like a parrot? A carrot!",
    "Why don't programmers like nature? It has too many bugs!",
    "How do you make a tissue dance? Put a little boogie in it!",
    "What do you call a dinosaur that crashes his car? Tyrannosaurus Wrecks!",
    "Why did the cookie go to the doctor? Because it felt crumbly!",
    "What do you call a sleeping bull? A bulldozer!",
    "Why don't some couples go to the gym? Because some relationships don't work out!"
]

# Response model
class JokeResponse(BaseModel):
    joke: str
    id: int

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Random Joke API is running!", "total_jokes": len(JOKES)}

@app.get("/joke", response_model=JokeResponse)
async def get_random_joke():
    """Get a random joke"""
    joke_id = random.randint(0, len(JOKES) - 1)
    return JokeResponse(joke=JOKES[joke_id], id=joke_id)

@app.get("/jokes/count")
async def get_joke_count():
    """Get total number of available jokes"""
    return {"total_jokes": len(JOKES)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)