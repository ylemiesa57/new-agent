#!/usr/bin/env python3
"""
Helper script to list available Gemini models for your API key
"""
import os
from dotenv import load_dotenv

load_dotenv()

try:
    import google.generativeai as genai
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ GEMINI_API_KEY not found in .env file")
        exit(1)
    
    genai.configure(api_key=api_key)
    
    print("🔍 Fetching available Gemini models...\n")
    models = genai.list_models()
    
    available_models = []
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            available_models.append(model.name)
    
    if available_models:
        print("✅ Available models that support generateContent:\n")
        for model in available_models:
            # Extract just the model name (remove 'models/' prefix if present)
            model_name = model.replace('models/', '')
            print(f"  • {model_name}")
            print(f"    Full name: {model}\n")
        
        print("\n💡 To use in CrewAI, try:")
        print(f"   model=\"gemini/{available_models[0].replace('models/', '')}\"")
    else:
        print("❌ No models found with generateContent support")
        print("\nAvailable models:")
        for model in models:
            print(f"  • {model.name}")
            print(f"    Methods: {model.supported_generation_methods}\n")
            
except ImportError:
    print("❌ google-generativeai package not installed")
    print("   Install with: pip install google-generativeai")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nThis might mean:")
    print("  - Your API key is invalid")
    print("  - Your API key doesn't have access to list models")
    print("  - There's a network issue")
