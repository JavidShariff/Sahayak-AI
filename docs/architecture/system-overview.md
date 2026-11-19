
# Sahayak AI — System Overview

## 1. Project Overview

Sahayak AI is a multilingual AI front-desk platform for small businesses, initially targeting clinics in India.

It helps businesses automate customer enquiries, appointment management, reminders, and human handoff.

## 2. High-Level Architecture

Sahayak AI follows a modular monolith architecture initially, with independently runnable services and background workers.

### Applications
- Dashboard: Next.js
- Chat Widget: React

### Backend Services
- Core API: Node.js, Express, TypeScript
- Agent Service: Python, FastAPI

### Background Workers
- Ingestion Worker: Python
- Notification Worker: Node.js

### Shared Packages
- Shared Contracts: API schemas and shared types

## 3. Data Infrastructure

- PostgreSQL: Relational and transactional data
- MongoDB: Conversations and knowledge-base documents
- Redis: Caching, queues, and temporary state
- Chroma: Development vector database
- Amazon S3: File storage

## 4. Infrastructure

- Docker and Docker Compose
- AWS
- Terraform
- GitHub Actions

## 5. Core Principles

- Multi-tenant architecture
- Tenant data isolation
- Secure authentication and authorization
- Validated AI tool execution
- Human handoff when required
- Observability and error handling
- Cost and usage monitoring

## 6. Current Development Status

Project foundation and repository structure are being established.

Implementation will proceed incrementally, with testing and documentation at each milestone.
