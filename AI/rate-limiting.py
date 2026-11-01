def ask_ai(user_id, prompt):
    if not token_bucket_allow(user_id, tokens_needed=1, capacity=20, refill_per_hour=20):
        return "Too many, retry in 15min", 429

    if ai_daily_spend > 1000:
        log("wallet cap hit")
        return "Ai is busy, try later"

    return call_openai(prompt, timeout=3)    