#!/usr/bin/env python3
"""
Setup script for language-trainer package.
Configuration is read from config.json.
"""

import json
import os
from setuptools import setup, find_packages


def load_config():
    """Load configuration from config.json."""
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    return config['setup']


def read_readme():
    """Read README.md for long description."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""


def main():
    """Main setup function."""
    # Load configuration from config.json
    config = load_config()
    
    # Read long description from README if specified
    if 'long_description_file' in config:
        long_description = read_readme()
    else:
        long_description = config.get('description', '')
    
    # Remove non-setup.py fields
    setup_config = {k: v for k, v in config.items() 
                    if k not in ['long_description_file']}
    
    # Add long description
    setup_config['long_description'] = long_description
    
    # Use find_packages if packages not specified
    if 'packages' not in setup_config:
        setup_config['packages'] = find_packages(where='source/code')
    
    # Call setup with configuration
    setup(**setup_config)


if __name__ == '__main__':
    main()
