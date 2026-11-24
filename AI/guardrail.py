def run_automation(customer_message):
    if contains_BVN_or_pin(customer_message):
        return "I cannot handle Bvn or pin"

     if prompt_injection(customer_message):
        log_event(type="injection_attempt", message=customer_message)
        return "I cannot help you with that"

    decision = llm_call()

    if decision["tool"] not in TOOLS:
        return "Cannot not perform that action"

    if decision["tool"] == "book_delivery" and not "payment_confirmed":
        return "Cannot book until payment is made"  

    if decision["amount"] and decision["amount"] > 5000 and decision["need_human"] == False:
        decision["need_human"] == True
        return "I need to check with mama"

    if decision["price_found"] == False and decision["price"] is not None:
        return "I need to check in with Mama"

    return decision                 