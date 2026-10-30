def transfer(amount. idempotency_key):
    if already_processed(idempotency_key):
        return previous_result()

    try:
        result = call_bank(amoun timeout=2)
    except:
        log("bank failed", key=idempotency_key)

    for attempts in [1,2,3]:
        try:
            result = call_bank(amount, timeout=2)
            break
        except:
            sleep(attempts + random())                