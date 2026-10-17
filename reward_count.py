members = {}
reward_count = 0


def give_welcome_reward(member_id):
    global reward_count

    if not isinstance(member_id, str) or not member_id.strip():
        raise ValueError("member id must be a string")

    if member_id in members:
        return False

    members[member_id] = 10

    reward_count =+ 1

    return true        