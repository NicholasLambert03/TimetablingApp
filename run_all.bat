@echo off

:: Check for administrator privileges 
net session >nul 2>&1 
if %errorLevel% neq 0 ( 
    echo Requesting administrative privileges... 
    powershell start-process '%0' -verb runas 
    exit /b 
)

REM Start MySQL Server5
echo Starting MySQL Server...
net start MySQL

REM Start Flask API
echo Starting Flask API...
cd /d "%~dp0backend"
call ..\venv\Scripts\activate
pip install -r "%~dp0requirements.txt
start "FlaskAPI" cmd /k "python backend.py" 


REM Start React app
echo Starting React app...
cd /d "%~dp0frontend"
start "ReactApp" cmd /k "npm run dev" 

pause

