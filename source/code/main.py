#!/usr/bin/env python3
"""
Main entry point for the language-trainer CLI application.
"""

import sys
import argparse
import json
import os
from pathlib import Path


def get_config():
    """Load configuration from config.json."""
    # Try to find config.json in parent directories
    current_dir = Path(__file__).parent
    for _ in range(5):  # Search up to 5 levels
        config_path = current_dir / 'config.json'
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        current_dir = current_dir.parent
    
    # Fallback to default config
    return {
        "app": {
            "name": "Language Trainer",
            "version": "0.1.0"
        }
    }


def main():
    """Main CLI entry point."""
    config = get_config()
    app_config = config.get('app', {})
    
    parser = argparse.ArgumentParser(
        description=f"{app_config.get('name', 'Language Trainer')} - A CLI application for language learning",
        prog='language-trainer'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f"%(prog)s {app_config.get('version', '0.1.0')}"
    )
    
    parser.add_argument(
        'command',
        nargs='?',
        choices=['start', 'train', 'test', 'stats'],
        help='Command to execute'
    )
    
    parser.add_argument(
        '-l', '--language',
        help='Target language for training'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Display welcome message
    print(f"{'=' * 60}")
    print(f"  {app_config.get('name', 'Language Trainer')}")
    print(f"  Version: {app_config.get('version', '0.1.0')}")
    print(f"{'=' * 60}")
    print()
    
    if args.command:
        print(f"Executing command: {args.command}")
        if args.language:
            print(f"Target language: {args.language}")
        
        # Command execution logic
        if args.command == 'start':
            print("Starting language training session...")
            print("(Feature implementation pending)")
        elif args.command == 'train':
            print("Training mode...")
            print("(Feature implementation pending)")
        elif args.command == 'test':
            print("Testing your knowledge...")
            print("(Feature implementation pending)")
        elif args.command == 'stats':
            print("Displaying statistics...")
            print("(Feature implementation pending)")
    else:
        parser.print_help()
        return 0
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
