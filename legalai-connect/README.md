# LegalAI Connect

**Tamil-first public legal guidance kiosk — VBYLD 2026 | Hack for Social Cause**

LegalAI Connect is a prototype public-service kiosk designed to help citizens understand the **first step** for common legal and administrative problems in a language they are comfortable using.

The prototype is intentionally designed as **legal information and navigation**, not as an automated lawyer. Answers should be grounded in approved sources, uncertainty should be surfaced, and sensitive/complex cases should be escalated to a human legal-support team.

## What the prototype demonstrates

- Tamil-first citizen interaction
- Structured intake for common problems
- Retrieval-grounded legal guidance
- Risk/confidence classification
- Human escalation
- Synthetic test cases
- Source/version metadata
- Basic audit-friendly response format

## Repository structure

```text
legalai-connect/
├── frontend/kiosk-app/          # Simple kiosk UI
├── backend/LegalAIConnect.API/  # ASP.NET Core-style API prototype
├── ai/
│   ├── prompts/                # Prompt templates and guardrails
│   ├── retrieval/              # Source retrieval logic
│   └── risk-classification/     # Risk rules
├── data/
│   ├── sample-cases/            # Synthetic citizen cases
│   ├── test-questions/          # Evaluation questions
│   └── sample-legal-content/    # Demo-only source records
├── tests/                       # Prototype tests
├── docs/                        # Architecture, security and AI safety
├── LICENSE
└── .github/workflows/           # Basic CI
```

## Quick start

### Option A — run the kiosk prototype

The frontend is a dependency-light HTML/JS prototype so judges can inspect and demo it without a cloud account.

```bash
cd frontend/kiosk-app
python3 -m http.server 8080
```

Open `http://localhost:8080`.

### Option B — run the API prototype

The backend contains a minimal ASP.NET Core-style implementation and sample response flow.

Requirements:
- .NET 8 SDK
- Python 3.10+ for the evaluation scripts

```bash
cd backend/LegalAIConnect.API
dotnet run
```

## Important note about legal content

The files under `data/sample-legal-content/` are **synthetic/demo records**, not a substitute for current legal advice. A production system must retrieve and version authoritative material and have the content reviewed by qualified legal/domain experts.

## AI safety model

LegalAI Connect follows four simple rules:

1. **Ground the answer** in approved source material.
2. **Do not invent** statutes, fees, forms or deadlines.
3. **Escalate** when the case is sensitive, uncertain or outside the supported scope.
4. **Keep a source/version trail** for every generated guidance response.

See `docs/AI_SAFETY.md`.

## Demo scenario

Example citizen input:

> எனது கணவர் என் அப்பாவிடமிருந்து பணம் பெற்றுகொண்டுவா இல்லையென்றால் என்னை வீட்டைவிட்டு துரத்திவிடுவேனென்று கூறுகிறார், நான் இப்போது இதை எவ்வாரு பெரிது படுத்தாமல் சாமர்த்தியமாய் கையாழுவது?

The prototype classifies this as a possible family dispute involving financial pressure and a threat of being forced out of the home. It asks clarifying questions and produces a cautious next-step guidance response from the synthetic knowledge base. Because the situation may be sensitive or safety-related, the prototype can also trigger human escalation.

## Architecture

See `docs/ARCHITECTURE.md`.

## Testing

```bash
python3 tests/test_prototype.py
```

The test suite checks:
- intent classification
- risk classification
- source grounding
- escalation behaviour
- synthetic Tamil sample flow

## Privacy

Do not commit real citizen records, names, phone numbers, addresses, case numbers, voice recordings or documents to this public repository.

Use synthetic data for demonstrations.

## License

This project is released under the MIT License. See `LICENSE`.

Third-party models, APIs, government content and datasets may have their own terms and licenses. They are not automatically relicensed by this repository.
