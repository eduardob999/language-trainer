# Security policy for Language Trainer

This document provides a short, practical security policy for the repository. It is intended for contributors and maintainers of the Language Trainer project.

## Key claims and practices

- Secrets are never committed to version control. Store API keys, passwords, and tokens in environment variables or a secrets manager.
- Configuration files like `config.json` are allowed for non-secret settings only. Any secret values must be injected at runtime from secure sources.
- Logs must not contain personally identifiable information (PII) or secrets. Only summary data should be logged to CSV files under `source/data/csv`.
- Files created by the application that may contain sensitive data are set to restrictive permissions (owner read/write) when possible (0o600).
- Dependencies should be reviewed and pinned for reproducible, auditable installs. Monitor dependency advisories.
- CI/CD secrets must be stored in the provider's secret store and never printed to logs.

## Reporting vulnerabilities

If you find a security vulnerability, please follow these steps:

1. Do not create a public issue that discloses the vulnerability.
2. Contact the repository owner/maintainer directly with details. If you don't have direct contact info, open a private issue or use the platform's private security reporting channels.
3. Provide steps to reproduce, the affected versions, and suggested mitigations.

## Suggested fixes and follow-ups

- Add `requirements-dev.txt` or `pyproject.toml` with pinned dev dependencies for reproducible testing.
- Add automated security scanning to CI (dependabot, safety, or GitHub CodeQL) to surface known vulnerabilities.
- Consider a `SECURITY_CONTACT` file or an email address for private reports.

Last updated: 2025-10-17
