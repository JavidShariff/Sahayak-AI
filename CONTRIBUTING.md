# Contributing to Sahayak AI

Thank you for your interest in contributing to Sahayak AI!

## 1. Development Setup

- Read the project README before starting.
- Follow the documented environment setup instructions.
- Never commit secrets, API keys, passwords, or `.env` files.

## 2. Branching Strategy

Create a separate branch for every change. Do not work directly on `main`.

Branch naming conventions:

- `feat/` — New features
- `fix/` — Bug fixes
- `docs/` — Documentation changes
- `chore/` — Maintenance and configuration
- `refactor/` — Code improvements without changing functionality

Examples:

- `feat/appointment-booking`
- `fix/tenant-isolation`
- `docs/api-documentation`

## 3. Commit Messages

Use clear, descriptive commit messages.

Format:

`type: short description`

Examples:

- `feat: add appointment booking`
- `fix: prevent duplicate appointments`
- `docs: update API documentation`
- `chore: add project configuration`

## 4. Pull Request Guidelines

- Create a Pull Request targeting `main`.
- Explain what changed and why.
- Describe the testing performed.
- Complete the Pull Request template.
- Keep changes focused and easy to review.

## 5. Code Quality and Security

- Follow existing project conventions.
- Validate external inputs.
- Never expose secrets or sensitive customer information.
- Add or update tests when required.
- Consider tenant isolation and data privacy in every relevant change.

## 6. Questions and Improvements

For questions, bugs, or improvement ideas, use the repository's GitHub Issues.
