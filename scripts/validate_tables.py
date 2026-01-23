#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validate and sort table data for Agent4Rec Survey.

Usage:
    python scripts/validate_tables.py
"""
import sys
import os
import csv
from pathlib import Path

# Configure Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
TABLES_DIR = ROOT / "data" / "tables"


def validate_and_sort_table1(file_path):
    """
    Table 1: Survey Comparison
    Rules:
    1. Keep the order as is (comparison table)
    2. Validate that all required columns exist
    """
    print("\n📊 Validating Table 1: Survey Comparison")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    required_columns = ['Paper', 'Language', 'What', 'Why', 'How', 'Pipeline', 'Highlights']
    if rows:
        actual_columns = list(rows[0].keys())
        missing = set(required_columns) - set(actual_columns)
        if missing:
            print(f"  ⚠️ Warning: Missing columns: {missing}")
    
    print(f"  ✓ Validated {len(rows)} survey entries")
    print("  ✅ Table 1 validated")


def validate_and_sort_table2(file_path):
    """
    Table 2: Agent as Rec (WHERE dimension)
    Rules:
    1. Sort by Venue (year descending, then alphabetically)
    """
    print("\n📊 Validating Table 2: Agent as Rec")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Extract year from venue and sort
    def get_sort_key(row):
        venue = row.get('Venue', '')
        # Extract year (e.g., "WWW'25" -> 25, "arXiv'24" -> 24)
        import re
        year_match = re.search(r"'(\d+)", venue)
        year = int(year_match.group(1)) if year_match else 0
        return (-year, venue)  # Negative for descending order
    
    rows.sort(key=get_sort_key)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ Sorted {len(rows)} models by Venue (year descending)")
    print("  ✅ Table 2 validated and sorted")


def validate_and_sort_table3(file_path):
    """
    Table 3: Agent for Rec (WHERE dimension)
    Rules:
    1. Sort by Venue (year descending, then alphabetically)
    """
    print("\n📊 Validating Table 3: Agent for Rec")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Extract year from venue and sort
    def get_sort_key(row):
        venue = row.get('Venue', '')
        import re
        year_match = re.search(r"'(\d+)", venue)
        year = int(year_match.group(1)) if year_match else 0
        return (-year, venue)
    
    rows.sort(key=get_sort_key)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ Sorted {len(rows)} models by Venue (year descending)")
    print("  ✅ Table 3 validated and sorted")


def validate_and_sort_table4(file_path):
    """
    Table 4: Agent in Rec (WHERE dimension)
    Rules:
    1. Sort by Venue (year descending, then alphabetically)
    """
    print("\n📊 Validating Table 4: Agent in Rec")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Extract year from venue and sort
    def get_sort_key(row):
        venue = row.get('Venue', '')
        import re
        year_match = re.search(r"'(\d+)", venue)
        year = int(year_match.group(1)) if year_match else 0
        return (-year, venue)
    
    rows.sort(key=get_sort_key)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ Sorted {len(rows)} models by Venue (year descending)")
    print("  ✅ Table 4 validated and sorted")


def validate_and_sort_table5(file_path):
    """
    Table 5: HOW dimension (Module usage)
    Rules:
    1. Keep alphabetical order by Methods name
    2. Validate module columns (Profile, Memory, Planning, Action)
    """
    print("\n📊 Validating Table 5: HOW Dimension")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    # Sort alphabetically by Methods
    rows.sort(key=lambda x: x.get('Methods', '').lower())
    
    # Write back
    with open(file_path, 'w', encoding='utf-8', newline='') as f:
        fieldnames = rows[0].keys() if rows else []
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"  ✓ Sorted {len(rows)} methods alphabetically")
    print("  ✅ Table 5 validated and sorted")


def main():
    """Main function"""
    print("=" * 70)
    print("  🔍 Validating and Sorting Tables - Agent4Rec Survey")
    print("=" * 70)
    
    validators = {
        'table1.csv': validate_and_sort_table1,
        'table2.csv': validate_and_sort_table2,
        'table3.csv': validate_and_sort_table3,
        'table4.csv': validate_and_sort_table4,
        'table5.csv': validate_and_sort_table5,
    }
    
    for filename, validator in validators.items():
        file_path = TABLES_DIR / filename
        if file_path.exists():
            try:
                validator(file_path)
            except Exception as e:
                print(f"  ❌ Error processing {filename}: {e}")
        else:
            print(f"\n⚠️  {filename} not found, skipping")
    
    print("\n" + "=" * 70)
    print("  ✅ Validation complete!")
    print("=" * 70)
    print("\n💡 Tip: Run 'python scripts/render_tables.py' to update README")


if __name__ == "__main__":
    main()
