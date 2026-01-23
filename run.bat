@echo off
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/
    pause
    exit /b 1
)

:: Create virtual environment if not exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
)

:: Activate virtual environment
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)

:: Install dependencies if needed
if not exist "venv\Scripts\pip.exe" (
    echo Installing dependencies...
    python -m pip install --upgrade pip
    if exist requirements.txt (
        pip install -r requirements.txt
    ) else (
        pip install pyyaml
    )
)

:menu
cls
echo ========================================
echo   Agent4Rec Survey - Quick Start
echo ========================================
echo.
echo [1] Add Paper
echo [2] Add/Update Table
echo [3] Batch Import
echo [4] Sync ^& Render
echo [5] Preview (if mkdocs installed)
echo [0] Exit
echo.
set /p choice="Select option: "

if "%choice%"=="1" (
    python scripts\add_paper.py
    pause
    goto menu
)

if "%choice%"=="2" (
    python scripts\add_table.py
    pause
    goto menu
)

if "%choice%"=="3" (
    if exist templates\papers_template.csv (
        python scripts\batch_import.py templates\papers_template.csv
    ) else (
        echo ❌ Template file not found: templates\papers_template.csv
    )
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo ▶ Rendering papers...
    python scripts\render_papers.py
    echo.
    echo ▶ Syncing README...
    python scripts\sync_readme.py
    echo.
    echo ✅ Done!
    pause
    goto menu
)

if "%choice%"=="5" (
    where mkdocs >nul 2>&1
    if errorlevel 1 (
        echo ❌ mkdocs not installed
        echo Install with: pip install mkdocs mkdocs-material
    ) else (
        echo Starting local server...
        echo Open http://127.0.0.1:8000 in your browser
        mkdocs serve
    )
    pause
    goto menu
)

if "%choice%"=="0" (
    exit /b 0
)

echo ❌ Invalid choice
pause
goto menu
