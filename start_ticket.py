def start_ticket(ticket, events):
    if ticket["status"] != "open":
        raise ValueError("ticket must be open")

    if ticket.get("assigned_to") is None:
        raise ValueError("this ticket must be assigned")

    ticket["status"] = "in_progress"

    events.append({
        "action": "START",
        "ticket": ticket["id"]
    })        

    return ticket