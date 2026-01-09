"""
Test script to verify OpenAI API key is working
Run this to check if your setup is correct
"""
import os
import sys

try:
    import openai
except ImportError:
    print("❌ OpenAI package not installed!")
    print("Run: pip install openai==0.28.0")
    sys.exit(1)

# Check API key
api_key = os.getenv('OPENAI_API_KEY', 'your-openai-api-key-here')

print("=" * 60)
print("OpenAI API Key Test")
print("=" * 60)
print()

if api_key == 'your-openai-api-key-here' or not api_key:
    print("❌ API Key NOT SET")
    print()
    print("Current value:", api_key if api_key else "None")
    print()
    print("To set it:")
    print("1. Get your key from: https://platform.openai.com/api-keys")
    print("2. Set environment variable:")
    print()
    print("   Windows PowerShell:")
    print('   $env:OPENAI_API_KEY="sk-your-key-here"')
    print()
    print("   Windows CMD:")
    print('   set OPENAI_API_KEY=sk-your-key-here')
    print()
    print("   Linux/Mac:")
    print('   export OPENAI_API_KEY="sk-your-key-here"')
    print()
    print("3. Or edit app.py line 62:")
    print('   OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-your-key-here")')
    sys.exit(1)

if not api_key.startswith('sk-'):
    print("❌ Invalid API Key Format")
    print(f"   Key should start with 'sk-' but starts with: {api_key[:3]}")
    sys.exit(1)

print(f"✅ API Key Found: {api_key[:10]}...{api_key[-4:]}")
print()

# Test API call
print("Testing API connection...")
try:
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say 'Hello, OpenAI is working!' if you can read this."}
        ],
        max_tokens=50
    )
    
    reply = response.choices[0].message.content.strip()
    print("✅ OpenAI API is working!")
    print(f"   Response: {reply}")
    print()
    print("🎉 Your chatbot should now use OpenAI!")
    print("   Restart your Flask app and test the chat.")
    
except openai.error.AuthenticationError:
    print("❌ Authentication Failed")
    print("   Your API key is invalid. Please check it at:")
    print("   https://platform.openai.com/api-keys")
    
except openai.error.RateLimitError:
    print("❌ Rate Limit Exceeded")
    print("   You've hit OpenAI's rate limit. Wait a few minutes.")
    
except Exception as e:
    print(f"❌ Error: {type(e).__name__}")
    print(f"   {str(e)}")
    print()
    print("Check:")
    print("  - Your internet connection")
    print("  - OpenAI service status: https://status.openai.com/")
    print("  - You have credits in your OpenAI account")
