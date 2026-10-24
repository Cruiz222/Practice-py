def transfer(token, amount, from_account, to_account):
    user = verify_token(token)

    if not user.owns(from_account):
        deny()

    with db.transaction:
        if not has_balance(from_account, amount):
            deny()

        do_deduct(from_account, amount)

    audit.log(user, amount, from_account, to_account)        

