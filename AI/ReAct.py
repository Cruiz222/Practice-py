TOOLS = {
    "check_stock": check_stock,
    "check_payment": check_payment,
    "book_delivery": book_delivery,
    "send_whatsapp": send_whatsapp
}

def agent_loop(customer_message):
    decision = (
        prompt="you are a shoppay assistant. use tools to verif. Never guess. if amount > 5k, escalate",
        context=context,
        message=customer_message,
        tools=list(TOOLS.keys())
    )

    if decision[tools] == "book_delivery" and not payment_confirmed:
        return "Cannot deliver book without payment confirmation"

    if decision[tools] not in TOOLS:
        return "cannot perform that action"

    result = TOOLS[decision[tool]](decision["args"])

    final llm_call(
        prompt="Based on result, that is the next step?",
        tool_result=result
    )       

    log_event(tool=decision["tool"], args=decision["args"], result=result)