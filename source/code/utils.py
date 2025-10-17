#!/usr/bin/env python3
"""Minimal safe utilities for language-trainer.

This module provides simple, defensive helpers for JSON/CSV I/O and
small logging helpers that sanitize messages before writing them to
CSV files. The goal is to avoid storing secrets or very large values
in repository logs.
"""

from pathlib import Path
import json
import csv
import os
from datetime import datetime


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    try:
        os.chmod(p, 0o600)
    except Exception:
        pass


def load_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def append_csv(row, path, fieldnames=None):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    exists = p.exists()
    if fieldnames is None:
        fieldnames = list(row.keys())
    with open(p, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if not exists:
            w.writeheader()
        w.writerow(row)
    try:
        os.chmod(p, 0o600)
    except Exception:
        pass


def _sanitize(msg, max_len=1000):
    if msg is None:
        return ''
    s = str(msg)
    s = s.replace('\n', ' ').replace('\r', ' ')
    if len(s) > max_len:
        return s[:max_len] + '...'
    return s


def log_event(message, log_file='source/data/csv/log.csv'):
    entry = {'timestamp': datetime.utcnow().isoformat() + 'Z', 'message': _sanitize(message)}
    append_csv(entry, log_file, fieldnames=['timestamp', 'message'])


def log_error(message, error_file='source/data/csv/error_log.csv'):
    entry = {'timestamp': datetime.utcnow().isoformat() + 'Z', 'error': _sanitize(message)}
    append_csv(entry, error_file, fieldnames=['timestamp', 'error'])


def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def get_project_root():
    return Path(__file__).resolve().parent.parent.parent


def get_data_path(subdir=''):
    root = get_project_root()
    data = root / 'source' / 'data'
    return data / subdir if subdir else data
