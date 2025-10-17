# Language Trainer — `source/code` overview

This document gives a concise, high-level overview of the code inside `source/code`.
It is written for contributors and maintainers who are new to the project. Language is simple and general because the project is a work in progress.

## Purpose

The `source/code` package contains the application entry point, helper utilities, and extension points for the Language Trainer app. Runtime data such as simple logs are stored under `source/code/data/csv`.

## Layout (what each file/folder is for)

Top-level files (inside `source/code`)

- `__init__.py`
  - Marks the directory as a Python package. Usually empty or used to export package-level names.

- `main.py`
  - The main entry point for the application. Responsible for bootstrapping the app, coordinating modules, and starting workflows.

- `utils.py`
  - Shared helper functions used across the package (parsing, small transformations, I/O helpers, etc.).

Subpackages

- `core/`
  - `__init__.py` — Intended for core application logic and services that form the central behavior of the app.

- `modules/`
  - `__init__.py` — Intended for optional features, plugins, or extensions.

Data

- `data/csv/`
  - `log.csv` — General activity or event log written by the app.
  - `error_log.csv` — Errors or exceptions captured during runs.

## How to run (examples)

From the repository root you can typically run the app like this:

```bash
python source/code/main.py
```

Or, if you prefer running as a module:

```bash
python -m source.code.main
```

Notes:
- Python 3.8+ is recommended.
- If `main.py` requires CLI arguments or environment variables, check the file for usage instructions and provide them accordingly.

## Logs and files

The CSV files under `source/code/data/csv` are plain text and can be opened with a spreadsheet tool or inspected in the shell with `head`, `tail`, or `less`.

If logs are not created, confirm write permissions for the `source/code/data/csv` folder.

## Guidelines for contributors

- Add core features to `core/` and optional features to `modules/`.
- Export public APIs through `__init__.py` for easier imports.
- Keep functions small and focused; add docstrings to public functions and classes.
- Put I/O and side effects behind thin wrappers so logic stays easy to test.

Suggested feature flow

1. Create a new file for the feature in `core/` or `modules/`.
2. Add tests for the main behavior where possible.
3. Export the feature from the package `__init__.py` if it should be widely importable.
4. Wire it into `main.py` and ensure important events/errors are logged to `log.csv` / `error_log.csv`.

## Troubleshooting

- Imports failing? Ensure you run scripts from the repository root or set `PYTHONPATH` accordingly.
- App doesn't start? Look for missing dependencies or required configuration in `config.json` or env vars.
- Logs missing? Check write permissions and whether the app is catching and suppressing exceptions.

## Next steps (optional)

- Add a short API section in this doc that lists public functions and classes from `main.py` and `utils.py` (I can generate this if you allow me to read those files).
- Add minimal unit tests for utilities in `utils.py` and run them with `pytest`.
- Expand docs for any non-trivial modules inside `core/` or `modules/`.

## API (public functions)

The following public functions are defined in `source/code/main.py` and `source/code/utils.py`. These are stable, small helpers and the CLI entry point.

From `source/code/main.py`:

- `get_config()` -> dict
  - Load configuration from a `config.json` file found in parent directories (searches up to 5 levels). Returns a default config if none found.

- `main()` -> int
  - CLI entry point. Parses arguments and runs simple placeholder commands (`start`, `train`, `test`, `stats`). Returns an exit code (0 on success).

From `source/code/utils.py`:

- `load_json(filepath)`
  - Load and return JSON data from `filepath`.

- `save_json(data, filepath)`
  - Save `data` as JSON to `filepath`. Creates parent directories if needed.

- `load_csv(filepath)`
  - Read a CSV file and return a list of dictionaries (one per row).

- `append_csv(data, filepath, fieldnames=None)`
  - Append a dictionary `data` as a row to the CSV at `filepath`. Writes the header if the file does not exist.

- `log_event(message, log_type='info', log_file='source/data/csv/log.csv')`
  - Convenience helper to write a timestamped event row to the CSV log file.

- `log_error(error_message, error_file='source/data/csv/error_log.csv')`
  - Convenience helper to write timestamped errors to the error CSV file.

- `ensure_dir(directory)`
  - Create `directory` and parent directories if they do not exist.

- `get_project_root()` -> Path
  - Return the project root path by navigating up from `source/code`.

- `get_data_path(subdir='')` -> Path
  - Return the path to `source/data` or a subdirectory inside it.

Last updated: 2025-10-17

## Security considerations

This section lists simple, practical security claims and recommendations relevant to the `source/code` package. The language is intentionally simple to help contributors follow safe defaults.

- Sensitive data: Do not store passwords, API keys, tokens, or other secrets in plain text files under the repository (`config.json`, `.env`, or CSV logs). Use environment variables or a secrets manager when possible.

- Configuration files: Treat `config.json` as non-secret configuration. If you need secret values, load them from environment variables or an external vault at runtime and do not commit them.

- Access control and file I/O: When creating or writing files (logs, JSON, CSV), verify the target directory exists and validate permissions. Use `os.makedirs(..., exist_ok=True)` as done in `utils.save_json` and `append_csv`, but avoid writing sensitive data to world-readable locations.

- Log contents: Logs under `source/code/data/csv` should avoid including personally identifiable information (PII) or secrets. When logging errors, prefer summarized messages over full stack traces; record stack traces in a secure error store if needed.

- Input validation: Validate and sanitize any external input (CLI args, file contents, network input) before using it. Never pass unchecked input into shell commands or into code that performs file system operations without validation.

- Error handling: Do not leak sensitive internals to standard output in production. Use error logging (`log_error`) to record problems and control what is printed to the console based on a `--verbose` flag.

- Dependencies: Keep third-party dependencies minimal and pin versions in a dev manifest (e.g., `requirements-dev.txt` or `pyproject.toml`). Review dependency security advisories periodically.

- File permissions: When creating files that may contain sensitive records, set restrictive permissions where appropriate (e.g., 0o600). Python's `open()` doesn't set permissions directly — consider using `os.chmod()` after file creation.

- Safe defaults: Prefer least-privilege defaults: write logs and data to a dedicated `data/` directory inside the project (as currently done) rather than system directories.

- Secrets in CI: When adding CI workflows, keep secrets in the provider's encrypted secret store (e.g., GitHub Actions secrets) and never echo them in logs.

- Auditing and retention: Decide how long logs are retained and who can access them. Remove or redact PII from logs on export or when requested.

If you'd like, I can:

1. Add short inline security notes to `source/code/utils.py` where logs and file writes occur.
2. Create a `SECURITY.md` with higher-level policy and reporting guidelines.
3. Add a `requirements-dev.txt` and pin `pytest` so tests run reproducibly in CI.

# Source: `source/code` — Code Overview

This document gives a simple, high-level overview of the files and folders in `source/code`. It is intended for contributors and maintainers who are new to the project. The language is kept simple and general because the project is a work-in-progress.

## Purpose

The `source/code` package contains the core application logic, helper utilities, and extension points for the Language Trainer app. Data files used by the app (logs) are stored in `source/code/data/csv`.

## Project layout

Top-level (inside `source/code`)
- `__init__.py`  
  - Marks `source/code` as a Python package. Typically left small or empty.
- `main.py`  
  - The main entry point for the application. Responsible for bootstrapping the app, loading configuration, or coordinating modules. Run this to start or exercise the program logic.
- `utils.py`  
  - Helper and utility functions shared across the package (e.g., parsing, formatting, small helpers).

Subpackages
- `core/`
  - `__init__.py`  
    - Intended to contain core features and essential application logic. Put central services, classes, or domain logic here.
- `modules/`
  - `__init__.py`  
    - Intended to hold optional features, extensions, or pluggable modules that augment the app.

Data files
- `data/csv/`
  - `error_log.csv`  
    - CSV file used to record application errors or exceptions encountered during runtime.
  - `log.csv`  
    - CSV used for general logs (activity, events, or simple audit records).

## Quick usage notes

Requirements
- Python 3.8+ is recommended. Use a virtual environment.

Run the app (example)
- From the repository root run:
  - `python source/code/main.py`
  - Or, if the package is configured to run as a module:
    - `python -m source.code.main`

If `main.py` requires command-line arguments or specific environment variables, consult the source or add them to the above commands.

Log files
- The app writes logs to `source/code/data/csv/log.csv` and `error_log.csv`. These are plain CSV files and can be opened with any spreadsheet program or inspected with `cat`, `less`, or `csv` utilities.

## Developer guidelines

Adding a new module
1. Put new feature code inside `modules/` (for optional features) or `core/` (for central functionality).
2. Export public API from the module `__init__.py` so other parts of the app can import it simply.
3. Add minimal tests when possible (see next section).

Style and conventions
- Keep functions small and focused.
- Document public functions with short docstrings.
- Prefer pure functions for logic that can be unit tested.

## Recommended quick tests (manual)

- Start the app:
  - `python source/code/main.py`  
  - Confirm it runs without crashing and that `log.csv` is updated as expected.
- Force an error path (if available) and confirm `error_log.csv` records the problem.

## Minimal suggestions and next steps
- Add a short `public/doc/code.md` (this file) to make the project easier to onboard.
- Add docstrings to `main.py` and `utils.py` describing inputs and outputs for important functions.
- Add a tiny test file (e.g., `tests/test_utils.py`) exercising one helper in `utils.py`.
- If the app is intended to be installed as a package, add a `pyproject.toml` or clarify `setup.py` usage in the top-level README.

## Contact & contribution
For questions about implementation details or intended behavior, check file-level comments or contact the repository owner/maintainer.
