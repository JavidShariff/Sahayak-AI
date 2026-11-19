
# ADR-002: Backend Language and Framework Selection

- **Status:** Accepted
- **Date:** 2026-11-20

## Context

Sahayak AI requires a backend for business operations and a separate runtime for AI-related functionality.

We need technologies that support reliable APIs, asynchronous processing, AI integrations, and future scalability.

## Decision

We will use two primary backend technologies.

### Core API
- Language: TypeScript
- Runtime: Node.js
- Framework: Express.js

Responsibilities:
- Authentication and authorization
- Tenant management
- Business operations
- Appointment management
- Leads and billing
- Usage tracking

### Agent Service
- Language: Python
- Framework: FastAPI

Responsibilities:
- AI agent execution
- LLM integration
- Tool calling
- Retrieval-Augmented Generation (RAG)
- Conversation memory
- AI guardrails and evaluation

## Consequences

### Positive
- TypeScript supports structured application development.
- Python provides a strong ecosystem for AI development.
- Each backend has clearly defined responsibilities.
- Both technologies can be developed and deployed independently.

### Trade-offs
- We must maintain two language ecosystems.
- Communication between services requires well-defined API contracts.
- Testing and monitoring must cover both runtimes.

## Future Considerations

Shared API contracts and explicit service boundaries will help maintain compatibility as the system evolves.
