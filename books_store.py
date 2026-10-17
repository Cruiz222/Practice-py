book = {
    "book_id": "B001",
    "status": "available",
    "borrower": None
}

events = []


def borrow_book(book, borrower_id):
    
    if not isinstance(borrower_id, str) or not borrower_id.strip():
        raise ValueError("invalid borrower id")

    if book.get("status") != "available":
        raise ValueError("book is not available")

    before = book["status"]

    book["status"] = "borrowed"
    book["borrower"] = borrower_id

    event.append({
        "action": "BORROW",
        "before": "before",
        "after": "borrowed"
    })


    return book    


borrow_book(book, "F001")

assert book["status"] == "borrowed"
assert book["borrower"] == "F001"
assert len(events) == 1

# Save the state before an invalid operation
previous_book = book.copy()
previous_events = events.copy()

try:
    borrow_book(book, "F002")
except ValueError:
    pass

assert book == previous_book
assert events == previous_events

print("All tests passed!")