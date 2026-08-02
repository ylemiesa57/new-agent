# ⚡ Quick Start - 3 Steps

## For Students

### Step 1: Install
```bash
cd interface
npm install
```

### Step 2: Run
```bash
npm run dev
```

This starts both services together:
- Backend on http://localhost:3001
- Frontend on http://localhost:3000

### Step 3: Register Your Agent
1. Open http://localhost:3000
2. Click "Add Agent"
3. Fill in your agent's username, name, and Railway URL (from Day 3), plus an optional description
4. Click "Register Agent"
5. Select your agent from the registry and start chatting! 🤖

---

## Get Your Railway URL

From your Day 3 folder:
```bash
cd ../day-3
railway domain
```

Copy the URL that looks like:
```
https://your-agent.up.railway.app
```

Paste it into the "Deployment URL" field when registering your agent (no trailing `/query`, and no trailing slash).

---

## What You'll See

1. **Agent Registry**
   - See every agent your classmates have registered
   - Click "Add Agent" to register your own
   - Click any agent card to open a chat with it

2. **Chat Interface**
   - Type your question
   - Press Enter (or click Send)
   - See your agent's response with timing!

---

## Example Questions

Try asking:
- "What is 50 * 50?" (tests calculator)
- "What do you know about me?" (tests memory)
- "Tell me about Python" (general knowledge)

---

## Deploy Your Own (Optional)

Want to host the registry for your class instead of just running it locally?

### Deploy to Railway (Free)
```bash
cd interface
railway init
railway up
railway domain
```

This deploys the combined frontend + backend as one service. See `README.md` for the full deploy walkthrough (Railway is what this interface is actually built and configured for, not Vercel — the backend and frontend need to run together, not as separate static/serverless deploys).

---

## Troubleshooting

**Can't connect?**
- ✅ Check your agent is deployed on Railway
- ✅ Test with: `curl https://your-url.up.railway.app/health`
- ✅ Make sure the Deployment URL doesn't end with `/`

**CORS error?**
- ✅ Already fixed in Day 3 code!

**Need help?**
- Check the console (F12 → Console)
- Read the full README.md
- Ask your instructor!

---

**That's it! Happy chatting! 🎉**
