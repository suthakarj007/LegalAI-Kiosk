import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "ai" / "risk-classification")
)

from classify import classify


def test_guided():
    assert classify(
        "I am facing a family problem and need to know what I should do first."
    ) == "guided"


def test_human_review():
    assert classify(
        "My husband is pressuring me to get money from my father and says he will force me out of the house. I need legal help."
    ) == "human_review"


def test_emergency():
    assert classify(
        "My husband is threatening me right now and I am afraid for my safety."
    ) == "emergency"


if __name__ == "__main__":
    test_guided()
    test_human_review()
    test_emergency()
    print("All prototype tests passed.")
