@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

:select_language
cls
echo ================================================================================
echo WELCOME - BIENVENUE - WILLKOMMEN
echo ================================================================================
echo.
echo Wählen Sie Ihre Sprache: / Choose your language: / Choisissez votre langue:
echo [E] English
echo [D] Deutsch
echo [F] Français
echo ================================================================================
set /p lang="Ihre Auswahl (E/D/F): "

if /i "%lang%"=="E" goto welcome_en
if /i "%lang%"=="D" goto welcome_de
if /i "%lang%"=="F" goto welcome_fr
goto select_language

:welcome_en
cls
echo ================================================================================
echo Welcome to PC Optimus, the ultimate open-source multitool for Windows.
echo This script is designed to assist inexperienced users with the installation
echo of the necessary packages and programs.
echo ================================================================================
echo Press Enter to continue...
pause >nul
goto check_python

:welcome_de
cls
echo ================================================================================
echo Willkommen bei PC Optimus, dem ultimativen Open-Source-Multitool für Windows.
echo Dieses Skript hilft unerfahrenen Benutzern bei der Installation der nötigen
echo Pakete und Programme.
echo ================================================================================
echo Drücken Sie Enter, um fortzufahren...
pause >nul
goto check_python

:welcome_fr
cls
echo ================================================================================
echo Bienvenue chez PC Optimus, l'outil multitâche open-source ultime pour Windows.
echo Ce script est conçu pour aider les utilisateurs inexpérimentés à installer
echo les packages et programmes nécessaires.
echo ================================================================================
echo Appuyez sur Entrée pour continuer...
pause >nul
goto check_python

:check_python
cls
echo ================================================================================
echo Checking Python installation...
echo ================================================================================
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python is already installed.
    echo Press Enter to proceed with module installation...
    pause >nul
    goto install_modules
) else (
    echo Python is not installed!
    set /p install_python="Would you like to install Python now? (Y/N): "
    if /i "%install_python%"=="Y" goto install_python
    goto end
)

:install_python
cls
echo ================================================================================
echo Installing Python...
echo ================================================================================
start ms-windows-store://pdp/?productid=9ncvdn91xzqp
msg * Press Install
cls
echo ================================================================================
echo Press Enter when the installation is completed...
echo ================================================================================
pause
goto check_python

:install_modules
cls
echo ================================================================================
echo Installing required Python modules...
echo ================================================================================
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install speedtest-cli chardet psutil wmi

if %errorlevel% == 0 (
    echo ================================================================================
    echo Installation of required components completed successfully!
    echo Now start the PCOptimus.py file to use the tool.
    echo ================================================================================
) else (
    echo ================================================================================
    echo Error installing modules. Please try again.
    echo ================================================================================
)
pause
goto end

:end
exit
