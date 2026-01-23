#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatically sync papers from YAML data files to README.md.
For Agent4Rec Survey project.

Usage:
    python scripts/sync_readme.py
"""
import re
import sys
import os
from pathlib import Path
import yaml
from typing import List, Dict

# Set Windows console encoding
if sys.platform == 'win32':
    os.system('chcp 65001 >nul 2>&1')
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
README_PATH = ROOT / "README.md"

# shields.io badge URLs
ARXIV_BADGE = "https://img.shields.io/badge/arXiv-paper-B31B1B?logo=arxiv&logoColor=white"
DOI_BADGE = "https://img.shields.io/badge/DOI-paper-00599C?logo=doi&logoColor=white"
WEBSITE_BADGE = "https://img.shields.io/badge/Website-paper-5B9BD5?logo=googlechrome&logoColor=white"
GITHUB_BADGE = "https://img.shields.io/badge/GitHub-repo-24292F?logo=github&logoColor=white"
HF_BADGE = "https://img.shields.io/badge/HuggingFace-dataset-ff7e21?logo=huggingface&logoColor=white"

# Category definitions for Agent4Rec Survey
CATEGORIES = {
    "general": {
        "title": "📈 General Recommendations",
        "yaml": "papers_general.yaml",
        "description": "Methods for general recommendation tasks"
    },
    "domain_specific": {
        "title": "🔍 Domain-Specific Recommendations",
        "yaml": "papers_domain_specific.yaml",
        "description": "Methods for specific domains and scenarios"
    },
    "interactive": {
        "title": "📚 Interactive Recommendations",
        "yaml": "papers_interactive.yaml",
        "description": "Methods for interactive and conversational recommendations"
    },
    "evaluation": {
        "title": "🎮 System Evaluation",
        "yaml": "papers_evaluation.yaml",
        "description": "Methods for evaluating recommender systems"
    },
    "single_agent": {
        "title": "🤖 Single-Agent Systems",
        "yaml": "papers_single_agent.yaml",
        "description": "Individual autonomous agents"
    },
    "multi_agent": {
        "title": "👥 Multi-Agent Systems",
        "yaml": "papers_multi_agent.yaml",
        "description": "Collaborative multi-agent frameworks"
    }
}

# Regex to match comment blocks
PAPERS_BLOCK_RE = re.compile(
    r"<!-- START PAPERS -->(.*?)<!-- END PAPERS -->",
    re.DOTALL
)


def load_yaml(path: Path) -> List[Dict]:
    """Load YAML file and return list of entries."""
    if not path.exists():
        print(f"[WARN] {path} does not exist, skipping.", file=sys.stderr)
        return []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        return data
    except Exception as ex:
        print(f"[ERR] Failed to load {path}: {ex}", file=sys.stderr)
        return []


def badge_arxiv(url: str) -> str:
    """Generate arXiv badge."""
    if not url:
        return ""
    return f'[![arXiv]({ARXIV_BADGE})]({url})'


def badge_doi(url: str) -> str:
    """Generate DOI badge."""
    if not url:
        return ""
    return f'[![DOI]({DOI_BADGE})]({url})'


def badge_website(url: str) -> str:
    """Generate Website badge."""
    if not url:
        return ""
    return f'[![Website]({WEBSITE_BADGE})]({url})'


def badge_github(url: str) -> str:
    """Generate GitHub badge."""
    if not url:
        return ""
    return f'[![GitHub]({GITHUB_BADGE})]({url})'


def badge_huggingface(url: str) -> str:
    """Generate HuggingFace badge."""
    if not url:
        return ""
    return f'[![HuggingFace]({HF_BADGE})]({url})'


def count_unique_papers() -> int:
    """Count unique papers across all categories."""
    unique_papers = set()
    
    for category_id, category_info in CATEGORIES.items():
        yaml_file = category_info["yaml"]
        yaml_path = DATA_DIR / yaml_file
        
        entries = load_yaml(yaml_path)
        if not entries:
            continue
        
        for entry in entries:
            short_name = entry.get('short_name', '').strip()
            title = entry.get('title', '').strip()
            if short_name:
                unique_papers.add(('short_name', short_name.lower()))
            elif title:
                unique_papers.add(('title', title.lower()))
    
    return len(unique_papers)


def render_paper_item(entry: Dict) -> str:
    """Render a single paper as a list item."""
    short_name = entry.get("short_name", "").strip()
    full_title = entry.get("title", "").strip()
    year = entry.get("year", "").strip()
    links = entry.get("links", {}) or {}
    
    arxiv = links.get("arxiv", "")
    doi = links.get("doi", "")
    website = links.get("website", "")
    github = links.get("github", "")
    huggingface = links.get("huggingface", "")
    
    # Build paper entry
    if short_name == full_title:
        if year:
            item = f"- **{short_name}** ({year})"
        else:
            item = f"- **{short_name}**"
    else:
        if year:
            item = f"- **{short_name}**: {full_title} ({year})"
        else:
            item = f"- **{short_name}**: {full_title}"
    
    # Add badges
    badges = []
    if arxiv:
        badges.append(badge_arxiv(arxiv))
    if doi:
        badges.append(badge_doi(doi))
    if website:
        badges.append(badge_website(website))
    if github:
        badges.append(badge_github(github))
    if huggingface:
        badges.append(badge_huggingface(huggingface))
    
    if badges:
        item += " " + " ".join(badges)
    
    return item


def generate_papers_section() -> str:
    """Generate the complete paper list section."""
    content = ["\n## 📚 Complete Paper List\n"]
    
    # Track unique works
    unique_papers = set()
    
    for category_id, category_info in CATEGORIES.items():
        yaml_file = category_info["yaml"]
        yaml_path = DATA_DIR / yaml_file
        
        entries = load_yaml(yaml_path)
        if not entries:
            continue
        
        # Add category title and description
        content.append(f"\n### {category_info['title']}\n")
        content.append(f"*{category_info['description']}*\n")
        
        # Render paper list
        for entry in entries:
            content.append(render_paper_item(entry))
            short_name = entry.get('short_name', '').strip()
            title = entry.get('title', '').strip()
            if short_name:
                unique_papers.add(('short_name', short_name.lower()))
            elif title:
                unique_papers.add(('title', title.lower()))
        
        paper_count = len(entries)
        print(f"  ✓ {category_info['title']}: {paper_count} papers")
    
    # Add summary
    total_unique = len(unique_papers)
    summary = f"\n> **Total: {total_unique} works** across {len(CATEGORIES)} categories\n"
    content.insert(1, summary)
    
    return "\n".join(content) + "\n"


def update_readme() -> bool:
    """Update the paper list in README.md file."""
    if not README_PATH.exists():
        print(f"[ERROR] {README_PATH} does not exist!", file=sys.stderr)
        return False
    
    content = README_PATH.read_text(encoding="utf-8")
    
    # Check if papers markers exist
    if "<!-- START PAPERS -->" not in content:
        print("[ERROR] <!-- START PAPERS --> marker not found in README.md!", file=sys.stderr)
        print("Please add the following markers to README.md:")
        print("\n<!-- START PAPERS -->")
        print("<!-- END PAPERS -->")
        return False
    
    # Count unique papers
    unique_count = count_unique_papers()
    print(f"\n📊 Total unique works: {unique_count}")
    
    # Update paper count badge
    new_content = re.sub(
        r'(!\[Papers Count\]\(https://img\.shields\.io/badge/papers-)\d+(-green\?style=for-the-badge&logo=googlescholar&logoColor=white\))',
        rf'\g<1>{unique_count}\g<2>',
        content
    )
    
    # Generate new papers section
    papers_section = generate_papers_section()
    
    # Replace papers content
    new_content = PAPERS_BLOCK_RE.sub(
        f"<!-- START PAPERS -->{papers_section}<!-- END PAPERS -->",
        new_content
    )
    
    # Write back to file
    if new_content != content:
        README_PATH.write_text(new_content, encoding="utf-8")
        print("\n✓ README.md updated successfully!")
        return True
    else:
        print("\nNo changes to README.md.")
        return True


def main():
    """Main function."""
    print("=" * 70)
    print("  Syncing YAML data to README.md - Agent4Rec Survey")
    print("=" * 70)
    print()
    
    success = update_readme()
    
    print()
    print("=" * 70)
    if success:
        print("  Sync completed successfully!")
    else:
        print("  Sync failed. Please check error messages.")
    print("=" * 70)
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
