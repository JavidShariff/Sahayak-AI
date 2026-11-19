
# ADR-001: Adopt a Modular Monolith Architecture

- **Status:** Accepted
- **Date:** 2026-11-20

## Context

Sahayak AI is an early-stage SaaS product. We need an architecture that supports rapid development, clear separation of responsibilities, and future scalability without introducing unnecessary operational complexity.

## Decision

We will begin with a modular monolith architecture.

The applications, backend services, workers, and shared packages will live in a single Git repository.

Each component will have clearly defined responsibilities and can run as a separate process where required.

## Consequences

### Positive
- Easier development and code sharing.
- Simpler initial deployment and infrastructure management.
- Clear separation between application components.
- Components can evolve independently.

### Trade-offs
- Requires clear module boundaries.
- Shared repository changes need coordination.
- Some components may eventually need independent deployment or extraction.

## Future Considerations

We will consider microservices only when actual scaling, deployment, or organizational requirements justify the additional complexity.
