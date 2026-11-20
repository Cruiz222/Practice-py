def handle_customer(message, customer_id):
    context = search_shop_doc(message)

    history = get_message(customer_id)

    decision = (
        prompt="you are a shopPAy assistant, always answer from context, never invent prices. If credit > 5000, ask human",
        message=messsage,
        context=context,
        history=history,
        tools=[check_payment(), check_store(), book_delivery()]
    )

    if decision.action == book_delivery() and price > 5000:
        return "I need to ask Mama first"
        contact_mama()

    if decision.contains_bvn_or_pin(message):
        return "I cannot handle BVN or pin here"

    if decision.tools == check_payment():
        result = check_payment(customer_id)
        return f"Payment of {result} has been successfully confirmed"

    log_event(who=customer_id, what=message, ai_answer=decision.text)

    return decision.text            