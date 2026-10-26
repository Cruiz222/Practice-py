def request_transfer(maker_token, amount, to_account):
    maker = verify_token(maker_token)

    if maker.role != "maker":
        deny()

    return save_as_pending(maker_id, amount, to_account)


def approve_transfer(checker_token, request_id):
    checker = verify_token(checker_token)

    if checker.role != checker:
        deny()

    req = get_request(request_id)

    if req.maker_id == checker_id:
        deny()

    do_transfer(req)                