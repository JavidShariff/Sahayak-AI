
# ADR-003: Database and Storage Selection

- **Status:** Accepted
- **Date:** 2026-11-20

## Context

Sahayak AI handles different types of data, including business records, appointments, conversations, documents, embeddings, and background job state.

A single database may not be the best fit for every workload.

## Decision

We will use the following storage technologies.

### PostgreSQL
For relational and transactional data:
- Businesses and tenants
- Users and memberships
- Appointments
- Services and staff
- Subscriptions and billing
- Leads and audit records

### MongoDB
For flexible document-oriented data:
- Conversations and messages
- Agent execution records
- Knowledge-base documents and chunks
- Evaluation cases

### Redis
For temporary and high-speed data:
- Caching
- Queue support
- Rate limiting
- Distributed locks

### Chroma
For local development and experimentation with vector search.

### MongoDB Vector Search
Planned production vector search solution, subject to infrastructure and performance validation.

### Amazon S3
For file storage:
- Uploaded documents
- Exports
- Generated files

## Consequences

### Positive
- Each storage system serves a specific workload.
- PostgreSQL provides relational integrity for transactional operations.
- MongoDB supports flexible document structures.
- Redis supports low-latency operations.
- Vector search supports knowledge retrieval.

### Trade-offs
- Multiple storage systems increase operational complexity.
- Data consistency across systems needs careful design.
- Backups, monitoring, security, and retention must cover every storage system.

## Future Considerations

We will validate database choices through implementation, integration tests, performance testing, and operational requirements before production deployment.
