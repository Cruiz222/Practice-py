# THE TOOLS - Python functions AI can call, but cannot invent
# Notice: NO refund_money(), NO transfer_money() in the list

TOOLS = {
    "check_stock": check_stock,       # Safe: read-only
    "check_payment": check_payment,   # Safe: read-only
    "book_delivery": book_delivery,   # Risky: needs guardrail
    "send_whatsapp": send_whatsapp    # Risky: needs guardrail
}

def agent_loop(customer_message):
    # 1. AI THINKS - With RAG context + tools list
    decision = llm_call(
        prompt="You are ShopPay helper. Use tools to verify. Never guess. If amount > N5k credit, escalate.",
        message=customer_message,
        context=search_shop_docs(customer_message),
        tools=list(TOOLS.keys()) # AI sees tool names + descriptions
    )
    # decision = {"thought": "Need to check stock", "tool": "check_stock", "args": {"bags": 100}}
    
    # 2. GUARDRAIL - Check BEFORE running tool
    if decision["tool"] == "book_delivery" and not payment_confirmed:
        return "Cannot book delivery until payment confirmed" # Fail closed
    
    if decision["tool"] not in TOOLS:
        return "I cannot do that tool" # AI tried to invent a tool - block it
    
    # 3. PYTHON EXECUTES - AI does NOT execute, Python does
    result = TOOLS[decision["tool"]](**decision["args"])
    # result = "Stock = 120 bags"
    
    # 4. AI OBSERVES - Give result back to AI to decide next step
    final = llm_call(
        prompt="Based on tool result, what is next step?",
        tool_result=result
    )
    # 5. LOG EVERYTHING
    log_event(tool=decision["tool"], args=decision["args"], result=result)
    return final