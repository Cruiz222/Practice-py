def transfer(amount, idempotency_key):
    if already_processed(idempotency_key):
        return previous_result()

    save(amount, key=idempotency_key, status="PENDING")    

    queue.push("sms_send", key=idempotency_key) 
    queue.push("settle_bank", key=idempotency_key)

    return "Transfer Recieved, Procesing"



def worker():
    job = queue.pop()
    if job.already_done(job.key):
        skip
    try:
        send_sms(job.key)
    except:
        queue.job_retry_later(job)        