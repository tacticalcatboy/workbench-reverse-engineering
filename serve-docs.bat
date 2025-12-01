@echo off
cd /d "%~dp0"

:: Find and kill any process using port 8000 (default mkdocs port)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr ":8000.*LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

:: Small delay to ensure port is released
timeout /t 1 /nobreak >nul

:: Start mkdocs serve
python -m mkdocs serve
