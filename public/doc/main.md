# Main CLI (`main.py`)

Location: `source/code/main.py`

Purpose

The `main.py` file implements the command-line entry point for the Language Trainer application. It parses command-line arguments, reads configuration from `config.json`, and dispatches a small set of top-level commands.

Key functions

- `get_config()` — Searches parent directories for `config.json` and returns parsed JSON. If no configuration is found, a default config object is returned.
- `main()` — Builds an `argparse` CLI with the following options:
  - `--version` — Show application version
  - `command` (positional) — One of: `start`, `train`, `test`, `stats`
  - `-l / --language` — Target language for training
  - `-v / --verbose` — Verbose output flag

Behavior

When invoked, the CLI prints a small banner with the application name and version (loaded from `config.json` when present). For supported commands it prints placeholder actions; the concrete training/test/statistics implementations are currently pending.

Usage examples

Run help:

    python -m source.code.main

Start a session for Spanish (example):

    python -m source.code.main start -l es

Notes for contributors

- `get_config()` searches up to 5 parent directories for `config.json` then falls back to a small default. If you want environment-specific config, consider supporting an environment variable pointing directly to the configuration file.
- The command handlers are currently placeholders. Add orchestration to integrate modules from `core` and `modules`, and use `utils` for persistent data.
