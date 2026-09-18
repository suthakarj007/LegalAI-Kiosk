def classify(text: str):
    t = text.lower()

    emergency_terms = ["threat", "violence", "danger", "immediate"]
    sensitive_terms = ["domestic violence", "child", "sexual assault", "court"]

    if any(x in t for x in emergency_terms):
        return "emergency"
    if any(x in t for x in sensitive_terms):
        return "human_review"

    return "guided"
