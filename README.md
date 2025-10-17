# language-trainer

Multiple language trainer - A CLI application for language learning

## Description

Language Trainer is a command-line application designed to help users learn and practice multiple languages. It provides an interactive interface for vocabulary training, grammar exercises, and progress tracking.

## Installation

### From source

```bash
git clone https://github.com/eduardob999/language-trainer.git
cd language-trainer
pip install -e .
```

### From PyPI (when published)

```bash
pip install language-trainer
```

## Usage

After installation, you can use the `language-trainer` command:

```bash
# Show help
language-trainer --help

# Show version
language-trainer --version

# Start a training session
language-trainer start -l spanish

# Train vocabulary
language-trainer train -l french

# Test your knowledge
language-trainer test -l german

# View statistics
language-trainer stats
```

## Project Structure

```
/public
    /media          # Public media files
    /doc           # Documentation files
/source
    /code          # Main source code
        main.py    # CLI entry point
        utils.py   # Utility functions
        /core      # Core modules
        /modules   # Extension modules
    /data          # Application data
        /json      # JSON data files
        /csv       # CSV log files
/script
    /bash          # Bash scripts
    /py            # Python scripts
    /prompt        # Prompt templates
/backup            # Backup directory
/temp              # Temporary files
```

## Configuration

The application uses `config.json` for configuration. All setup.py parameters are read from this file.

Environment variables can be set in the `.env` file (copy from `.env` template).

## Development

### Running from source

```bash
python source/code/main.py --help
```

### Building

```bash
python setup.py sdist bdist_wheel
```

## License

MIT License

## Author

Eduardo Bogado
