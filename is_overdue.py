from datetime import datetime, timezone, timedelta

def is_overdue(due_at, now=None):
    
    if due_at.tzinfo is None or due_at.utcoffset() is None:
        raise ValueError("due at must be time zone aware")

    if now.tzinfo is None or now.utcoffset() is None:
        raise ValueError("now must be time zone aware")

    if now is None:
        now = datetime(timezone.utc)

    if now > due_at:
        return True

    return          




from datetime import datetime, timezone, timedelta

deadline = datetime(
    2026, 10, 15, 11, 0,
    tzinfo=timezone.utc
)

assert is_overdue(
    deadline,
    deadline - timedelta(seconds=1)
) is False

assert is_overdue(deadline, deadline) is False

assert is_overdue(
    deadline,
    deadline + timedelta(seconds=1)
) is True

print("All deadline boundary tests passed!")    