#!/bin/bash
# Example bash script for language-trainer development

echo "=========================================="
echo "Language Trainer - Development Helper"
echo "=========================================="
echo ""

# Navigate to project root
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/../.." && pwd )"
cd "$PROJECT_ROOT"

echo "Project root: $PROJECT_ROOT"
echo ""

# Show project structure
echo "Project structure:"
tree -L 2 -I '.git|__pycache__|*.egg-info|dist|language_trainer'
echo ""

# Show available commands
echo "Available language-trainer commands:"
echo "  language-trainer --version    - Show version"
echo "  language-trainer --help       - Show help"
echo "  language-trainer start -l <lang> - Start training session"
echo "  language-trainer train -l <lang> - Training mode"
echo "  language-trainer test -l <lang>  - Test knowledge"
echo "  language-trainer stats        - Show statistics"
echo ""

echo "Example: language-trainer start -l spanish"
