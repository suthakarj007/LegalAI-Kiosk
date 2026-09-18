import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "sample-legal-content"

def load_sources():
    rows = []
    for p in DATA.glob("*.json"):
        rows.extend(json.loads(p.read_text(encoding="utf-8")))
    return rows

def retrieve(query: str):
    q = query.lower()
    sources = load_sources()
    scored = []
    for row in sources:
        hay = (row["title"] + " " + row["topic"] + " " + row["text"]).lower()
        score = sum(1 for word in q.split() if len(word) > 2 and word in hay)
        if score:
            scored.append((score, row))
    return [r for _, r in sorted(scored, key=lambda x: x[0], reverse=True)]
