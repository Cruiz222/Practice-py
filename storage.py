import json

ticket = {
    "id": "T001",
    "status": "open",
    "priority": "high",
    "assign_to": None
}

with open("ticket.json", "w") as file:
    json.dump(ticket, file, indent=4)

with open("ticket.json", "r") as file:
    loaded = json.load(file)

print(loaded)        