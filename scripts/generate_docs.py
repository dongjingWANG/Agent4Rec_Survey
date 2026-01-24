#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate documentation pages from data files
This script creates docs/papers.md and docs/tables.md from YAML and CSV data
"""
import sys
import os
import yaml
import csv
from pathlib import Path

# Configure Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"


def load_papers_from_yaml(yaml_file):
    """Load papers from YAML file"""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        papers = yaml.safe_load(f)
    return papers if papers else []


def generate_paper_badge(paper):
    """Generate badge links for a paper"""
    badges = []
    links = paper.get('links', {})
    
    if links.get('arxiv'):
        badges.append(f"[![arXiv](https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white)]({links['arxiv']})")
    if links.get('doi'):
        badges.append(f"[![DOI](https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white)]({links['doi']})")
    if links.get('github'):
        badges.append(f"[![GitHub](https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white)]({links['github']})")
    if links.get('huggingface'):
        badges.append(f"[![HuggingFace](https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white)]({links['huggingface']})")
    if links.get('website'):
        badges.append(f"[![Website](https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white)]({links['website']})")
    
    return ' '.join(badges)


def generate_papers_page():
    """Generate docs/papers.md from YAML data"""
    print("📝 Generating papers page...")
    
    # Paper categories
    categories = {
        'general': '📈 General Recommendations',
        'domain_specific': '🔍 Domain-Specific Recommendations',
        'interactive': '📚 Interactive Recommendations',
        'evaluation': '🎮 System Evaluation',
        'single_agent': '🤖 Single-Agent Systems',
        'multi_agent': '👥 Multi-Agent Systems'
    }
    
    content = []
    content.append("# Paper List\n")
    content.append("This page contains all papers from our survey, organized by category.\n")
    
    total_papers = 0
    
    for category_id, category_name in categories.items():
        yaml_file = DATA_DIR / f"papers_{category_id}.yaml"
        
        if not yaml_file.exists():
            continue
        
        papers = load_papers_from_yaml(yaml_file)
        if not papers:
            continue
        
        total_papers += len(papers)
        
        content.append(f"\n## {category_name}\n")
        content.append(f"*{len(papers)} papers*\n")
        
        for paper in papers:
            short_name = paper.get('short_name', 'Unknown')
            title = paper.get('title', 'Untitled')
            venue = paper.get('venue', 'N/A')
            year = paper.get('year', 'N/A')
            
            badges = generate_paper_badge(paper)
            
            content.append(f"\n### {short_name}\n")
            content.append(f"**{title}**\n")
            content.append(f"\n*{venue} ({year})*\n")
            if badges:
                content.append(f"\n{badges}\n")
    
    content.append(f"\n---\n")
    content.append(f"\n**Total Papers**: {total_papers}\n")
    
    # Write to docs/papers.md
    papers_md = DOCS_DIR / "papers.md"
    papers_md.write_text('\n'.join(content), encoding='utf-8')
    print(f"  ✓ Generated docs/papers.md ({total_papers} papers)")


def csv_to_markdown_table(csv_file):
    """Convert CSV to Markdown table"""
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    
    if not rows:
        return ""
    
    # Build table
    lines = []
    
    # Header
    header_line = '| ' + ' | '.join(f"**{h}**" for h in headers) + ' |'
    lines.append(header_line)
    
    # Separator
    separator = '| ' + ' | '.join(['---'] * len(headers)) + ' |'
    lines.append(separator)
    
    # Rows
    for row in rows:
        row_line = '| ' + ' | '.join(row) + ' |'
        lines.append(row_line)
    
    return '\n'.join(lines)


def generate_tables_page():
    """Generate docs/tables.md from CSV data"""
    print("📝 Generating tables page...")
    
    tables_info = {
        'table1.csv': {
            'title': 'Survey Comparison',
            'description': 'Comparison between this work and existing surveys.'
        },
        'table2.csv': {
            'title': 'Agent as Rec (WHERE)',
            'description': 'Papers where agents serve as the primary recommendation entity.'
        },
        'table3.csv': {
            'title': 'Agent for Rec (WHERE)',
            'description': 'Papers where agents interact with the system to enhance performance.'
        },
        'table4.csv': {
            'title': 'Agent in Rec (WHERE)',
            'description': 'Papers where agents are embedded in specific process stages.'
        },
        'table5.csv': {
            'title': 'HOW Dimension - Module Usage',
            'description': 'Analysis of optimization modules: Profile, Memory, Planning, and Action.'
        }
    }
    
    content = []
    content.append("# Tables & Statistics\n")
    content.append("This page contains statistical tables from our survey.\n")
    
    tables_dir = DATA_DIR / "tables"
    table_count = 0
    
    for filename, info in tables_info.items():
        csv_file = tables_dir / filename
        
        if not csv_file.exists():
            continue
        
        table_count += 1
        
        content.append(f"\n## {info['title']}\n")
        content.append(f"*{info['description']}*\n")
        
        table_md = csv_to_markdown_table(csv_file)
        if table_md:
            content.append(f"\n{table_md}\n")
    
    content.append(f"\n---\n")
    content.append(f"\n**Total Tables**: {table_count}\n")
    
    # Write to docs/tables.md
    tables_md = DOCS_DIR / "tables.md"
    tables_md.write_text('\n'.join(content), encoding='utf-8')
    print(f"  ✓ Generated docs/tables.md ({table_count} tables)")


def update_mkdocs_nav():
    """Update mkdocs.yml navigation to include new pages"""
    print("📝 Updating mkdocs.yml navigation...")
    
    mkdocs_yml = ROOT / "mkdocs.yml"
    
    if not mkdocs_yml.exists():
        print("  ⚠️ mkdocs.yml not found")
        return
    
    with open(mkdocs_yml, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if nav section needs updating
    if 'papers.md' in content and 'tables.md' in content:
        print("  ✓ Navigation already up to date")
        return
    
    # Update nav section
    new_nav = """nav:
  - Home: index.md
  - Papers: papers.md
  - Tables: tables.md
  - About: about.md
"""
    
    # Replace nav section
    import re
    pattern = r'nav:.*?(?=\n\S|\Z)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_nav.strip(), content, flags=re.DOTALL)
        
        with open(mkdocs_yml, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("  ✓ Updated mkdocs.yml navigation")
    else:
        print("  ⚠️ Could not find nav section in mkdocs.yml")


def main():
    """Main function"""
    print("=" * 70)
    print("  Generating Documentation Pages")
    print("=" * 70)
    print()
    
    # Ensure docs directory exists
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Generate papers page
    try:
        generate_papers_page()
    except Exception as e:
        print(f"  ❌ Error generating papers page: {e}")
    
    print()
    
    # Generate tables page
    try:
        generate_tables_page()
    except Exception as e:
        print(f"  ❌ Error generating tables page: {e}")
    
    print()
    
    # Update mkdocs navigation
    try:
        update_mkdocs_nav()
    except Exception as e:
        print(f"  ❌ Error updating navigation: {e}")
    
    print()
    print("=" * 70)
    print("  ✅ Documentation generation complete!")
    print("=" * 70)
    print()
    print("💡 Next steps:")
    print("   1. Preview: mkdocs serve")
    print("   2. Build: mkdocs build")
    print()


if __name__ == "__main__":
    success = main()
    sys.exit(0)
