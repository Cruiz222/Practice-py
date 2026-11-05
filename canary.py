def transfer(user_id):
    if flag_service.is_on(new_transfer_flow, user_id):
        return new_flow(user_id)

    else:
        return old_flow(user_id)    