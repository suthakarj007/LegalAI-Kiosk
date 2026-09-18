# AI Safety and Responsible Use

## Design principles

### Grounding
Responses should be generated only after retrieving relevant approved material.

### No hallucinated legal facts
The system must not invent:
- sections of law
- fees
- deadlines
- forms
- government offices
- rights or remedies

### Confidence
Every response should carry an internal confidence signal. Low confidence should trigger clarification or human review.

### Risk
High-risk categories should be escalated. Examples include:
- immediate threats to safety
- serious criminal allegations
- domestic violence or abuse
- child-related safeguarding concerns
- complex court matters
- cases where the retrieved sources conflict

### Human oversight
The prototype is a navigation and information service. It is not a replacement for qualified legal professionals.

### Privacy
Do not retain unnecessary personal information. Do not use real citizen information in this public prototype repository.
