@echo off
REM Define the directory and virtual environment name
set VENV_NAME=venv
set PROJECT_DIR=%cd%

REM Define the path to Python 3.12 executable
set PYTHON_PATH=C:\Users\SKumar02\AppData\Local\Microsoft\WindowsApps\python.exe

REM Check if Python 3.12 is installed at the specified path
if not exist "%PYTHON_PATH%" (
    echo Python 3.12 is not installed at the specified path: %PYTHON_PATH%
    echo Please install Python 3.12 or update the PYTHON_PATH variable in this script.
    pause
    exit /b 1
)

REM Check if virtual environment already exists
if exist "%PROJECT_DIR%\%VENV_NAME%" (
    echo Virtual environment '%VENV_NAME%' already exists.
    pause
    exit /b 1
)

REM Create the virtual environment
echo Creating virtual environment '%VENV_NAME%'...
"%PYTHON_PATH%" -m venv %VENV_NAME%

REM Activate the virtual environment
echo Activating virtual environment...
call "%PROJECT_DIR%\%VENV_NAME%\Scripts\activate.bat"

REM Upgrade pip
echo Upgrading pip...
"%PYTHON_PATH%" -m pip install --upgrade pip

REM Install required packages (if you have a requirements.txt file)
if exist "%PROJECT_DIR%\requirements.txt" (
    echo Installing packages from requirements.txt...
    pip install -r requirements.txt -r requirements-tox.txt
) else (
    echo No requirements.txt file found. Skipping package installation.
)

echo Virtual environment setup complete!
pause