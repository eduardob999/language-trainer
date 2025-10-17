# Security claims for Language Trainer

This short document lists simple, easy-to-follow security claims and recommendations for contributors.

- Secrets: Do not store API keys, passwords, tokens, or other secrets in repository files such as `config.json`, `.env`, or CSV logs. Use environment variables or a secrets manager and inject them at runtime.

- Logs: Do not write full secrets, credentials, or personally identifiable information (PII) to CSV logs under `source/data/csv`. Keep log messages short and sanitized.

- File permissions: When creating files that may contain sensitive data, set restrictive permissions (e.g., 0o600) where appropriate. Use `os.chmod()` after writing files if needed.

- Input validation: Validate and sanitize external inputs (CLI args, uploaded files, network responses) before using them. Never pass unchecked input to shell commands or to functions that perform file operations.

- CI/CD secrets: Store secrets in the CI provider's secret store (e.g., GitHub Actions secrets) and avoid printing them to build logs.

- Error handling: Avoid printing full stack traces or internal state to standard output in production. Use `log_error` to record sanitized error messages and store detailed traces in a secure error store if necessary.

- Dependencies: Keep third-party dependencies minimal and pin versions in a dev manifest. Monitor dependency advisories and update when security fixes are available.

If you want, I can:
- Add short Security sections to each `public/doc/*.md` file individually (I attempted to patch them but there was a tooling error). If you'd like that exact placement, tell me and I'll retry the in-place edits.
- Add inline comments in `source/code/utils.py` where file writes and logs occur to remind developers about permissions and sanitization.

Last updated: 2025-10-17
