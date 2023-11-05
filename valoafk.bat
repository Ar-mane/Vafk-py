@echo off

rem Define the path to the Python interpreter
set python_executable=python

rem Check if the required packages are installed
%python_executable% -m pip show package_name > nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    %python_executable% -m pip install -r requirements.txt
) else (
    echo Required packages are already installed.
)

rem Run the "valoafk.py" script
%python_executable% valoafk.py

pause
