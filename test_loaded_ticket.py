import json
import tempfile
from pathlib import Path


current_data = {
    "T001": {"status": "open"}
}

with tempfile.TemporaryDirectory() as directory:
    path = Path(directory) / "tickets.json"

    # Test 1: Corrupted JSON
    path.write_text('{"T002": ', encoding="utf-8")

    result = safe_load_json(path, current_data)

    assert result == current_data
    print("Test 1 passed: Corrupted JSON preserved existing data")

    # Test 2: Valid JSON
    path.write_text(
        json.dumps({"T002": {"status": "resolved"}}),
        encoding="utf-8"
    )

    result = safe_load_json(path, current_data)

    assert result == {
        "T002": {"status": "resolved"}
    }

    print("Test 2 passed: Valid JSON loaded")

    # Test 3: Wrong JSON structure
    path.write_text('["T001", "T002"]', encoding="utf-8")

    result = safe_load_json(path, current_data)

    assert result == current_data

    print("Test 3 passed: Invalid structure rejected")

print("All Lesson D tests passed!")