@echo off
echo ========================================
echo Animal Auto Pilot - Build Script
echo ========================================
echo.

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python not found!
    pause
    exit /b 1
)

echo.
echo Installing cx_Freeze (if not installed)...
python -m pip install cx_Freeze
if %errorlevel% neq 0 (
    echo WARNING: Could not install cx_Freeze
    echo Please install manually: python -m pip install cx_Freeze
    pause
    exit /b 1
)

echo.
echo Building executable...
python setup.py build
if %errorlevel% neq 0 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo Executable is in the 'build' folder
echo ========================================
pause
