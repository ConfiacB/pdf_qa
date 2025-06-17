def get_api_key():
    """User input to get OpenAI API Key"""
    api_key = input("\n> Enter your API Key: ").strip()

    if not api_key:
        print("❌ Error: No API Key provided.")
        raise SystemExit

    return api_key
