# LegalAI Connect — Architecture

## High-level flow

```text
Citizen
   |
   v
Kiosk UI
   |
   v
Tamil speech / text layer
   |
   v
Intent + risk classification
   |
   v
Verified legal knowledge retrieval
   |
   v
Controlled response generation
   |
   +----> Low confidence / high risk ----> Human legal team
   |
   v
Tamil guidance + optional print
```

## Components

### 1. Kiosk

A locked-down public interface with:
- touchscreen
- microphone
- headphones
- optional printer
- privacy-oriented physical enclosure

### 2. Language layer

Production candidates include BHASHINI and evaluated Indic-language ASR/TTS models. The language layer should be benchmarked specifically for Tamil accents and noisy public environments.

### 3. Intent and risk

The system identifies:
- problem category
- key entities
- urgency
- confidence
- whether the request is supported

A low-confidence or high-risk classification should prevent an overly confident answer.

### 4. Knowledge retrieval

Production retrieval should use versioned, approved sources. Each source record should contain:
- source authority
- title
- URL/document identifier
- effective date
- review date
- jurisdiction
- topic
- version

### 5. Response generation

The model receives only the retrieved context and explicit response rules. It should:
- explain rather than speculate
- distinguish information from advice
- identify missing facts
- avoid fabricated fees/deadlines
- provide source references
- escalate when required

### 6. Human escalation

A case record contains a generated case ID and only the minimum information required for follow-up. The district legal-support workflow can then assign, review and close the case.

## Production boundary

The LLM must not be the legal source of truth. The source repository and human review process are the authority layer.
