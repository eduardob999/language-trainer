# Extension modules (`modules/__init__.py`)

Location: `source/code/modules/__init__.py`

Purpose

This package is intended for optional or pluggable modules that extend the core application: importing dictionaries, third-party integrations, language packs, or experimental algorithms.

Current state

The file is a placeholder at the moment. Add modules here for:

- Language pack loaders
- Import/export utilities
- Integrations with external APIs (translation, TTS)

Guidance

Keep extension modules loosely coupled from `core` and define clear interfaces so they can be enabled or disabled by the CLI or configuration.
