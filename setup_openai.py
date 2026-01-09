"""
Quick script to help set up OpenAI API key
Run this to test your OpenAI configuration
"""
import os
import sys

def setup_openai():
    print("=" * 50)
    print("OpenAI API Key Setup for MindEase Chatbot")
    print("=" * 50)
    print()
    
    # Check current configuration
    current_key = os.getenv('OPENAI_API_KEY', 'Not set')
    
    if current_key != 'Not set' and current_key.startswith('sk-'):
        print("✅ OpenAI API Key is already set!")
        print(f"   Key: {current_key[:10]}...{current_key[-4:]}")
        print()
        print("You can now use the chatbot with OpenAI!")
        return True
    else:
        print("⚠️  OpenAI API Key is not configured")
        print()
        print("To set it up:")
        print()
        print("1. Get your API key from: https://platform.openai.com/api-keys")
        print()
        print("2. Set it using one of these methods:")
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
        print("3. Or edit app.py line 62 and set it directly:")
        print('   OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-your-key-here")')
        print()
        
        # Ask if user wants to set it now
        response = input("Do you want to set it now? (y/n): ").strip().lower()
        if response == 'y':
            api_key = input("Enter your OpenAI API key (starts with sk-): ").strip()
            if api_key.startswith('sk-'):
                print()
                print("✅ Key received! To use it:")
                print()
                print("Windows PowerShell:")
                print(f'   $env:OPENAI_API_KEY="{api_key}"')
                print()
                print("Windows CMD:")
                print(f'   set OPENAI_API_KEY={api_key}')
                print()
                print("Linux/Mac:")
                print(f'   export OPENAI_API_KEY="{api_key}"')
                print()
                print("Then restart your Flask app!")
            else:
                print("❌ Invalid API key format. Should start with 'sk-'")
        return False

if __name__ == "__main__":
    setup_openai()
