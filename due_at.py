from datetime import datetime, timezone, timedelta

def calculate_deadline(start_at, minutes):
    
    if not isinstance(start_at, datetime):
        raise ValueError("start at must be a datetime")

    if start_at.tzinfo is None or start_at.utcoffset() is None:
        raise ValueError("start at Must be timezone aware")    

    if Type(minutes) != int:
        raise TypeError("Minutes must be an interger")

    start_at.astimezone(timezone.utc)

    return start_at + timedelta(minutes=minutes) 




from datetime import datetime, timezone, timedelta

start = datetime(2026, 10, 15, 10, 0, tzinfo=timezone.utc)

assert calculate_deadline(start, 60) == datetime(
    2026, 10, 15, 11, 0, tzinfo=timezone.utc
)

# Reject naive datetime
try:
    calculate_deadline(datetime(2026, 10, 15, 10, 0), 60)
except ValueError:
    print("Naive datetime correctly rejected")

# Reject boolean
try:
    calculate_deadline(start, True)
except TypeError:
    print("Boolean correctly rejected")

# Reject negative duration
try:
    calculate_deadline(start, -10)
except ValueError:
    print("Negative duration correctly rejected")

print("Lesson A tests completed")    