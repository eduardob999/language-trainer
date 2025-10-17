#!/usr/bin/env python3
"""
Example script demonstrating the language-trainer utilities.
"""

import sys
import os

# Add source code to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'source', 'code'))

from utils import log_event, log_error, get_project_root, get_data_path


def main():
    """Demonstrate utility functions."""
    print("=" * 60)
    print("Language Trainer - Example Script")
    print("=" * 60)
    print()
    
    # Show project paths
    print("Project Information:")
    print(f"  Root: {get_project_root()}")
    print(f"  Data path: {get_data_path()}")
    print(f"  CSV path: {get_data_path('csv')}")
    print(f"  JSON path: {get_data_path('json')}")
    print()
    
    # Demonstrate logging
    print("Logging demonstration...")
    log_event("Example script started", "info")
    log_event("This is a sample log entry", "info")
    
    print("  ✓ Logged events to source/data/csv/log.csv")
    print()
    
    print("Example script completed successfully!")


if __name__ == "__main__":
    main()
