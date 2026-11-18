# Sahayak AI

Sahayak AI is a multi-tenant AI front-desk platform for small businesses in India, initially focusing on clinics.

## Vision

Help businesses automate customer enquiries, appointment booking, reminders, lead capture, and human handoff through conversational AI.

## Initial Capabilities

- Multilingual customer support: English, Tamil, Hindi, and Tanglish
- AI-powered enquiry handling
- Knowledge-base question answering (RAG)
- Appointment booking and management
- Lead capture and follow-ups
- Human handoff
- Business dashboard and analytics

## Architecture

The project will begin as a modular monolith with separately deployable AI and background worker services where appropriate.

## Technology Stack

- Frontend: Next.js, React, TypeScript
- Core API: Node.js, Express, TypeScript
- AI Service: Python, FastAPI
- Relational Database: PostgreSQL
- Document Database: MongoDB
- Cache and Queues: Redis
- Vector Search: Chroma for development, MongoDB Vector Search for production
- Infrastructure: Docker, AWS, Terraform, GitHub Actions

## Development Status

Currently in M1: Project Foundation and Engineering Environment.

## Important Principles

- Tenant identity must be derived and validated server-side.
- Customer data must remain isolated between businesses.
- AI-generated actions must be validated before execution.
- Sensitive information and credentials must never be committed.
- Clinical diagnosis and prescription advice are outside the system's scope.

## Project Structure

The repository structure will evolve incrementally as the project is implemented.

## Learning Approach

Sahayak AI is being built incrementally as a hands-on learning project covering backend engineering, agentic AI, cloud infrastructure, DevOps, security, and production system design.
