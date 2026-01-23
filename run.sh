#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 is not installed${NC}"
    echo "Please install Python 3.7+ from https://www.python.org/"
    exit 1
fi

# Create virtual environment if not exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ Failed to create virtual environment${NC}"
        exit 1
    fi
fi

# Activate virtual environment
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to activate virtual environment${NC}"
    exit 1
fi

# Install dependencies if needed
if [ ! -f "venv/bin/pip" ]; then
    echo "Installing dependencies..."
    python -m pip install --upgrade pip
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
    else
        pip install pyyaml
    fi
fi

# Main menu loop
while true; do
    clear
    echo "========================================"
    echo "  Agent4Rec Survey - Quick Start"
    echo "========================================"
    echo ""
    echo "[1] Add Paper"
    echo "[2] Add/Update Table"
    echo "[3] Batch Import"
    echo "[4] Sync & Render"
    echo "[5] Preview (if mkdocs installed)"
    echo "[0] Exit"
    echo ""
    read -p "Select option: " choice

    case $choice in
        1)
            python scripts/add_paper.py
            read -p "Press Enter to continue..."
            ;;
        2)
            python scripts/add_table.py
            read -p "Press Enter to continue..."
            ;;
        3)
            if [ -f "templates/papers_template.csv" ]; then
                python scripts/batch_import.py templates/papers_template.csv
            else
                echo -e "${RED}❌ Template file not found: templates/papers_template.csv${NC}"
            fi
            read -p "Press Enter to continue..."
            ;;
        4)
            echo ""
            echo "▶ Rendering papers..."
            python scripts/render_papers.py
            echo ""
            echo "▶ Syncing README..."
            python scripts/sync_readme.py
            echo ""
            echo -e "${GREEN}✅ Done!${NC}"
            read -p "Press Enter to continue..."
            ;;
        5)
            if command -v mkdocs &> /dev/null; then
                echo "Starting local server..."
                echo "Open http://127.0.0.1:8000 in your browser"
                mkdocs serve
            else
                echo -e "${RED}❌ mkdocs not installed${NC}"
                echo "Install with: pip install mkdocs mkdocs-material"
            fi
            read -p "Press Enter to continue..."
            ;;
        0)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo -e "${RED}❌ Invalid choice${NC}"
            read -p "Press Enter to continue..."
            ;;
    esac
done
