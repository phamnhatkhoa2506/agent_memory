# Agent Memory System

A long-term memory system for AI agents using Redis and Google Generative AI.

## Prerequisites

### 1. Redis with RedisSearch Module

You need Redis with the RedisSearch module installed. You can:

**Option A: Use Docker (Recommended)**
```bash
docker run -d --name redis-stack -p 6379:6379 redis/redis-stack:latest
```

**Option B: Install Redis with RedisSearch locally**
- Download Redis with RedisSearch from: https://redis.io/docs/stack/
- Or use Redis Cloud which includes RedisSearch

### 2. Google AI API Key

You need a Google AI API key to use Gemini models:

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an API key
3. Set it as an environment variable

## Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Set up environment variables:**
Create a `.env` file in the root directory:
```env
REDIS_URL=redis://localhost:6379
GOOGLE_API_KEY=your_google_ai_api_key_here
```

3. **Run the application:**
```bash
python main.py
```

## Troubleshooting

### Redis Module Error
If you see `unknown command 'MODULE'`, make sure you're using Redis with RedisSearch support.

### Google AI Authentication Error
If you see authentication errors, make sure:
- Your `GOOGLE_API_KEY` is set correctly in the `.env` file
- The API key is valid and has access to Gemini models 