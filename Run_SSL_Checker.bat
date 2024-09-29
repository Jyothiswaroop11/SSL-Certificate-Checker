@echo off
setlocal enabledelayedexpansion

set APP_PATH=
cd /d "%APP_PATH%" || exit /b 1

REM Start Flask server
start /B "" python app.py
timeout /t 2 /nobreak >nul

REM Get Flask PID
for /f "tokens=2" %%i in ('tasklist /fi "imagename eq python.exe" /fo list ^| find "PID:"') do set FLASK_PID=%%i

REM Open Chrome with a specific title
start "Flask_App_localhost_5000" chrome.exe --new-window "http://localhost:5000"
timeout /t 3 /nobreak >nul

REM Get Chrome PID
for /f "tokens=2" %%i in ('tasklist /fi "windowtitle eq Flask_App_localhost_5000*" /fo list ^| find "PID:"') do set CHROME_PID=%%i

echo Flask server is running. Chrome tab is open.
echo Close the Chrome tab to terminate the server and this prompt.
echo.

:LOOP
REM Check if Chrome is still running
tasklist /FI "PID eq %CHROME_PID%" 2>NUL | find /I /N "chrome.exe">NUL
if "%ERRORLEVEL%"=="1" goto END

REM Optional: Print Flask log (if available)
type nul | python -c "import sys; print(sys.stdin.readline().strip())" 2>nul

REM Wait for a short time before checking again
timeout /t 1 /nobreak >nul
goto LOOP

:END
REM Terminate Flask server
taskkill /F /PID %FLASK_PID% >nul 2>&1

echo.
echo Chrome tab was closed.
echo Flask server has been terminated.
echo This window will close in 3 seconds...
timeout /t 3 >nul
exit
