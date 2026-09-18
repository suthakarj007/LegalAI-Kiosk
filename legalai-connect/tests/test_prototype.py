import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ai" / "risk-classification"))

from classify import classify

def test_guided():
    assert classify("Where do I start with a missing animal report?") == "guided"

def test_human_review():
    assert classify("I need help with a court matter") == "human_review"

def test_emergency():
    assert classify("Someone is threatening me right now") == "emergency"

if __name__ == "__main__":
    test_guided()
    test_human_review()
    test_emergency()
    print("All prototype tests passed.")
