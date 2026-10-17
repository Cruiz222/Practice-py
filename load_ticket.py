import json


def safe_load_json(path, current_data):
    
    try:
        with open(path, "r") as file:
            loaded_ticket = json.load(file)

        if not isinstance(loaded_ticket, dict):
            raise ValueError("ticket must be a dictionary")

    except (json.JSONDecodeError, OSError, ValueError):
        return current_data

    return loaded_ticket    



    