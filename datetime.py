from datetime import datetime, timedelta, timezone

now = datetime.now(timezone.utc)

deadline = now + timedelta(minutes=60)

serialize = deadline.isoformat()

restored = deadline.fromisoformat()

naive = datetime(2026, 10, 15, 10, 0)

aware = datetime(2026, 10, 15, 10, 0, tzinfo=timezone.utc)


print(now)
print(deadline)
print(serialize)
print(restored)