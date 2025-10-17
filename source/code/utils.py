#!/usr/bin/env python3
"""
Utility functions for the language-trainer application.
"""

import os
import json
import csv
from pathlib import Path
from datetime import datetime


def load_json(filepath):
    """
    Load JSON data from a file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Parsed JSON data
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, filepath):
    """
    Save data to a JSON file.
    
    Args:
        data: Data to save
        filepath: Path to save the JSON file
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_csv(filepath):
    """
    Load CSV data from a file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        List of dictionaries representing CSV rows
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)


def append_csv(data, filepath, fieldnames=None):
    """
    Append data to a CSV file.
    
    Args:
        data: Dictionary of data to append
        filepath: Path to the CSV file
        fieldnames: List of field names (optional, inferred from data if not provided)
    """
    file_exists = os.path.isfile(filepath)
    
    if fieldnames is None:
        fieldnames = list(data.keys())
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(data)


def log_event(message, log_type='info', log_file='source/data/csv/log.csv'):
    """
    Log an event to the CSV log file.
    
    Args:
        message: Log message
        log_type: Type of log (info, warning, error)
        log_file: Path to the log file
    """
    timestamp = datetime.now().isoformat()
    log_entry = {
        'timestamp': timestamp,
        'type': log_type,
        'message': message
    }
    append_csv(log_entry, log_file, fieldnames=['timestamp', 'type', 'message'])


def log_error(error_message, error_file='source/data/csv/error_log.csv'):
    """
    Log an error to the error log file.
    
    Args:
        error_message: Error message
        error_file: Path to the error log file
    """
    timestamp = datetime.now().isoformat()
    error_entry = {
        'timestamp': timestamp,
        'error': error_message
    }
    append_csv(error_entry, error_file, fieldnames=['timestamp', 'error'])


def ensure_dir(directory):
    """
    Ensure a directory exists, create it if it doesn't.
    
    Args:
        directory: Path to the directory
    """
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_project_root():
    """
    Get the project root directory.
    
    Returns:
        Path to the project root
    """
    current_file = Path(__file__).resolve()
    # Navigate up from source/code to project root
    return current_file.parent.parent.parent


def get_data_path(subdir=''):
    """
    Get the path to the data directory.
    
    Args:
        subdir: Subdirectory within data (e.g., 'json', 'csv')
        
    Returns:
        Path to the data directory
    """
    root = get_project_root()
    if subdir:
        return root / 'source' / 'data' / subdir
    return root / 'source' / 'data'
