# Utilities (`utils.py`)

Location: `source/code/utils.py`

Purpose

The `utils.py` module contains small, focused helper functions used across the application for working with files, logging, and basic project paths.

Public functions and behavior

- `load_json(filepath)` — Read and parse a JSON file.
- `save_json(data, filepath)` — Write an object as JSON to `filepath`. Creates parent directories and attempts to set restrictive file permissions (owner read/write) when possible.
- `load_csv(filepath)` — Read a CSV and return a list of row dictionaries.
- `append_csv(data, filepath, fieldnames=None)` — Append a dictionary row to the CSV at `filepath`. Writes a header when the file is created and attempts to set restrictive permissions.
- `log_event(message, log_type='info', log_file='source/data/csv/log.csv')` — Append a timestamped event to the log CSV. Avoids logging secrets.
- `log_error(error_message, error_file='source/data/csv/error_log.csv')` — Append a timestamped error entry to the error CSV.
- `ensure_dir(directory)` — Create a directory (and parents) if it does not exist.
- `get_project_root()` — Return the project root Path (traverses up from `source/code` directory).
- `get_data_path(subdir='')` — Return the path to the `source/data` folder or a subdirectory inside it.

Notes and best practices

- File I/O functions attempt to set file permissions to `0o600` where supported. This is a safety-first default and can be adjusted for multi-user or web deployments.
- The CSV logging helpers are simple and write flat dictionaries. For high-throughput logging or structured logs consider using a rotating log handler or an external logging service.
- Avoid writing secrets or full stack traces to CSV logs. Use `log_error` for short, sanitized error messages.
