#!/usr/bin/env python3
"""
Render CSV tables to Markdown format for Agent4Rec Survey README
Input: data/tables/*.csv
Output: Markdown tables embedded in README.md sections
"""
import sys
import csv
from pathlib import Path

# Set UTF-8 encoding for Windows
if sys.platform == 'win32':
    import os
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')


def csv_to_markdown_table(csv_file, table_type='default'):
    """Convert a CSV file to Markdown table format matching README style"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    # Build Markdown table
    md_lines = []
    
    # Table header - match README format exactly
    if table_type == 'table5':
        # HOW table has special formatting with "Module" suffix
        header_parts = []
        for h in headers:
            if 'Module' in h:
                # Format as: **Profile** Module
                module_name = h.replace(' Module', '')
                header_parts.append(f'**{module_name}** Module')
            elif h == 'Code':
                header_parts.append('**Code**')
            elif h == 'Model(Framework)':
                header_parts.append('**Model**(Framework)')
            elif h == 'Dataset':
                header_parts.append('**Dataset**')
            else:
                header_parts.append(f'**{h}**')
        header_line = '|    ' + '     |    '.join(header_parts) + '     |'
        
        # Separator line - match README alignment exactly
        separator_parts = []
        for h in headers:
            if h == 'Methods':
                separator_parts.append(':----------------:')
            elif 'Module' in h or h == 'Code':
                separator_parts.append(':----------------:')
            elif h == 'Model(Framework)':
                separator_parts.append(':-------------------------------------:')
            elif h == 'Dataset':
                separator_parts.append(':-------------------------------------:')
            else:
                separator_parts.append(':------:')
        separator_line = '| ' + ' | '.join(separator_parts) + ' |'
    else:
        # Other tables use standard formatting
        header_line = '| ' + ' | '.join(f'**{h}**' for h in headers) + ' |'
        
        # Create separator with proper alignment
        separator_parts = []
        for h in headers:
            if h in ['Model Name', 'Paper']:
                separator_parts.append(':-------------')
            elif h in ['Single/Multi', 'Application Scenarios', 'Venue', 'Language', 'What', 'Why', 'How', 'Where']:
                separator_parts.append(':--------')
            else:
                separator_parts.append(':-------')
        separator_line = '| ' + ' | '.join(separator_parts) + ' |'
    
    md_lines.append(header_line)
    md_lines.append(separator_line)
    
    # Table rows - match README spacing
    for row in rows:
        if table_type == 'table5':
            # HOW table has special spacing
            row_parts = []
            for i, cell in enumerate(row):
                if i == 0:  # Methods column
                    row_parts.append(f'        {cell}         ')
                elif i < 5:  # Module columns
                    row_parts.append(f'         {cell}         ')
                elif i == 5:  # Code column
                    row_parts.append(f'    {cell}     ')
                else:  # Model and Dataset columns
                    row_parts.append(f'              {cell}              ')
            row_line = '|' + '|'.join(row_parts) + '|'
        else:
            # Standard spacing
            row_line = '| ' + ' | '.join(row) + ' |'
        md_lines.append(row_line)
    
    return '\n'.join(md_lines)


def update_readme_table(readme_path, section_marker, new_table_content):
    """Update a specific table in README.md"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    in_table = False
    table_replaced = False
    skip_next_line = False
    
    for i, line in enumerate(lines):
        if skip_next_line:
            skip_next_line = False
            continue
            
        # Detect table start
        if '|' in line and not in_table:
            # Check if next line is separator
            if i + 1 < len(lines) and '|---' in lines[i + 1]:
                # Check if this is the table we're looking for
                context = '\n'.join(lines[max(0, i-15):i])
                
                if section_marker in context:
                    # Start replacing
                    in_table = True
                    new_lines.append(new_table_content)
                    table_replaced = True
                    skip_next_line = True  # Skip the separator line
                    continue
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        elif in_table:
            # Skip old table lines
            if '|' not in line or line.strip() == '':
                # End of table
                in_table = False
                new_lines.append(line)
            # else: skip this line (part of old table)
        else:
            new_lines.append(line)
    
    if table_replaced:
        with open(readme_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(new_lines))
        return True
    return False


def sync_table1_to_readme():
    """Sync table1 (Survey Comparison) to README"""
    print("📊 Syncing Table 1: Survey Comparison...")
    
    csv_file = Path('data/tables/table1.csv')
    if not csv_file.exists():
        print("  ⚠️ table1.csv not found")
        return False
    
    table_md = csv_to_markdown_table(csv_file, 'table1')
    readme_path = Path('README.md')
    
    if update_readme_table(readme_path, 'comparison between this work and existing surveys', table_md):
        print("  ✅ Table 1 synced")
        return True
    else:
        print("  ⚠️ Could not find table1 location in README")
        return False


def sync_table2_to_readme():
    """Sync table2 (Agent as Rec) to README"""
    print("📊 Syncing Table 2: Agent as Rec...")
    
    csv_file = Path('data/tables/table2.csv')
    if not csv_file.exists():
        print("  ⚠️ table2.csv not found")
        return False
    
    table_md = csv_to_markdown_table(csv_file, 'table2')
    readme_path = Path('README.md')
    
    if update_readme_table(readme_path, '#### 📊Agent as Rec', table_md):
        print("  ✅ Table 2 synced")
        return True
    else:
        print("  ⚠️ Could not find table2 location in README")
        return False


def sync_table3_to_readme():
    """Sync table3 (Agent for Rec) to README"""
    print("📊 Syncing Table 3: Agent for Rec...")
    
    csv_file = Path('data/tables/table3.csv')
    if not csv_file.exists():
        print("  ⚠️ table3.csv not found")
        return False
    
    table_md = csv_to_markdown_table(csv_file, 'table3')
    readme_path = Path('README.md')
    
    if update_readme_table(readme_path, '#### 🎯Agent for Rec', table_md):
        print("  ✅ Table 3 synced")
        return True
    else:
        print("  ⚠️ Could not find table3 location in README")
        return False


def sync_table4_to_readme():
    """Sync table4 (Agent in Rec) to README"""
    print("📊 Syncing Table 4: Agent in Rec...")
    
    csv_file = Path('data/tables/table4.csv')
    if not csv_file.exists():
        print("  ⚠️ table4.csv not found")
        return False
    
    table_md = csv_to_markdown_table(csv_file, 'table4')
    readme_path = Path('README.md')
    
    if update_readme_table(readme_path, '#### 📥 Agent in Rec', table_md):
        print("  ✅ Table 4 synced")
        return True
    else:
        print("  ⚠️ Could not find table4 location in README")
        return False


def sync_table5_to_readme():
    """Sync table5 (HOW dimension) to README"""
    print("📊 Syncing Table 5: HOW Dimension...")
    
    csv_file = Path('data/tables/table5.csv')
    if not csv_file.exists():
        print("  ⚠️ table5.csv not found")
        return False
    
    table_md = csv_to_markdown_table(csv_file, 'table5')
    readme_path = Path('README.md')
    
    if update_readme_table(readme_path, '### 📋HOW', table_md):
        print("  ✅ Table 5 synced")
        return True
    else:
        print("  ⚠️ Could not find table5 location in README")
        return False


def main():
    print("\n" + "="*70)
    print("  Rendering Tables from CSV - Agent4Rec Survey")
    print("="*70 + "\n")
    
    success_count = 0
    
    # Sync all tables
    if sync_table1_to_readme():
        success_count += 1
    if sync_table2_to_readme():
        success_count += 1
    if sync_table3_to_readme():
        success_count += 1
    if sync_table4_to_readme():
        success_count += 1
    if sync_table5_to_readme():
        success_count += 1
    
    print("\n" + "="*70)
    if success_count == 5:
        print("  ✅ All tables rendered successfully!")
    else:
        print(f"  ⚠️ {success_count}/5 tables rendered")
    print("="*70 + "\n")
    
    return success_count == 5


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
