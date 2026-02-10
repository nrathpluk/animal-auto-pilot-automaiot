@echo off
echo ========================================
echo Building with CONSOLE WINDOW
echo ========================================
echo.

echo Cleaning old build...
if exist build rmdir /s /q build

echo.
echo Building executable with console...
python setup.py build

echo.
echo ========================================
echo Build completed!
echo The .exe will show a console window
echo Find it in: build\exe.win-amd64-3.14\
echo ========================================
pause
