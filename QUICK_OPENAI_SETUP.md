# Quick OpenAI Setup Guide

## 🚀 Get Your Chatbot Working with OpenAI in 3 Steps

### Step 1: Get Your OpenAI API Key

1. Go to: **https://platform.openai.com/api-keys**
2. Sign up or log in
3. Click **"Create new secret key"**
4. Copy your key (starts with `sk-...`)
   - ⚠️ **Save it now** - you won't see it again!

### Step 2: Set Your API Key

**Option A: Environment Variable (Recommended)**

**Windows PowerShell:**
```powershell
$env:OPENAI_API_KEY="sk-your-actual-key-here"
python app.py
```

**Windows Command Prompt:**
```cmd
set OPENAI_API_KEY=sk-your-actual-key-here
python app.py
```

**Linux/Mac:**
```bash
export OPENAI_API_KEY="sk-your-actual-key-here"
python app.py
```

**Option B: Direct in Code (Quick Test)**

Edit `app.py` line 62:
```python
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'sk-your-actual-key-here')
```

⚠️ **Don't commit this to Git!** Use environment variables for production.

### Step 3: Test It!

1. Start your Flask app:
   ```bash
   python app.py
   ```

2. Open your website and click the chat icon

3. Try typing: **"good"** or **"how are you?"**

4. You should get an AI-powered response! 🎉

## ✅ Verification

If OpenAI is working, you'll get:
- Natural, conversational responses
- Context-aware answers
- Different responses each time (due to temperature)

If you see fallback messages, check:
- ✅ API key is correct (starts with `sk-`)
- ✅ No extra spaces in the key
- ✅ Environment variable is set (if using that method)
- ✅ You have OpenAI credits (new accounts get $5 free)

## 💰 Cost

- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- Average chat: ~500-1000 tokens
- **Cost per conversation**: ~$0.001-0.002 (less than 1 cent!)

## 🔒 Security

- ✅ Never commit API keys to Git
- ✅ Use environment variables in production
- ✅ Set usage limits in OpenAI dashboard
- ✅ Monitor your usage at: https://platform.openai.com/usage

## 🆘 Troubleshooting

**Error: "Invalid API Key"**
- Check key starts with `sk-`
- No extra spaces
- Key is correct

**Error: "Rate limit exceeded"**
- Wait a few minutes
- Check your OpenAI plan limits

**Still getting fallback responses?**
- Check console for error messages
- Verify API key is set correctly
- Make sure you have OpenAI credits

## Need Help?

Check OpenAI status: https://status.openai.com/
