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
echo Checking dependencies...
python -c "import yaml" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    python -m pip install --upgrade pip
    if exist requirements.txt (
        pip install -r requirements.txt
    ) else (
        pip install pyyaml mkdocs mkdocs-material pymdown-extensions
    )
    echo ✅ Dependencies installed
)

:menu
cls
echo ========================================
echo   Agent4Rec Survey - Quick Start
echo ========================================
echo.
echo [1] Add Paper
echo [2] Add Table
echo [3] Batch Import
echo [4] Sync ^& Build
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
    echo.
    set /p csv_file="CSV file path (or press Enter for template): "
    if "!csv_file!"=="" (
        set csv_file=templates\papers_template.csv
    )
    if exist "!csv_file!" (
        python scripts\batch_import.py "!csv_file!"
    ) else (
        echo ❌ File not found: !csv_file!
    )
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo [1/4] Rendering papers...
    python scripts\render_papers.py
    if errorlevel 1 goto error
    echo [2/4] Syncing README...
    python scripts\sync_readme.py
    if errorlevel 1 goto error
    echo [3/4] Generating documentation pages...
    python scripts\generate_docs.py
    if errorlevel 1 goto error
    echo [4/4] Building website...
    where mkdocs >nul 2>&1
    if errorlevel 1 (
        echo ⚠️ mkdocs not installed, skipping build
        echo Install with: pip install mkdocs mkdocs-material
    ) else (
        mkdocs build
    )
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

:error
echo.
echo ❌ Failed
pause
goto menu
