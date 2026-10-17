from datetime import datetime, timezone

ticket = {
    "id": "T001",
    "status": "open",
    "sla_cycle": 2,
    "escalated_cycle": 2,
    "due_at": datetime(
        2026, 10, 16, 10, 0,
        tzinfo=timezone.utc
    )
}

events = []


def escalate_ticket(ticket, events, now=None):
    
    if now is None:
        now = datetime.now(timezone.utc)

    if now < ticket["due_at"]:
        raise ValueError("ticket must be overdue")

    if ticket["status"] == "resolved":
        raise ValueError("ticket must not be resolved")

    if ticket["escalated_cycle"] == ticket["sla_cycle"]:
       return False

    events.append({
        "action": "ESCALATE",
        "escalation_cycle": ticket["escalation_cycle"]
        "sla_cycle": ticket["sla_cycle"]
    })

    ticket["escalated_cycle"] = ticket["sla_cycle"]
    
    return True