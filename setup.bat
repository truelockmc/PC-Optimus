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
goto check_python_en

:welcome_de
cls
echo ================================================================================
echo Willkommen bei PC Optimus, dem ultimativen Open-Source-Multitool für Windows.
echo Dieses Skript hilft unerfahrenen Benutzern bei der Installation der nötigen
echo Pakete und Programme.
echo ================================================================================
echo Drücken Sie Enter, um fortzufahren...
pause >nul
goto check_python_de

:welcome_fr
cls
echo ================================================================================
echo Bienvenue chez PC Optimus, l'outil multitâche open-source ultime pour Windows.
echo Ce script est conçu pour aider les utilisateurs inexpérimentés à installer
echo les packages et programmes nécessaires.
echo ================================================================================
echo Appuyez sur Entrée pour continuer...
pause >nul
goto check_python_fr

:check_python_en
cls
echo ================================================================================
echo Checking Python installation...
echo ================================================================================
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python is already installed.
    echo Press Enter to proceed with module installation...
    pause >nul
    goto install_modules_en
) else (
    echo Python is not installed!
    set /p install_python="Would you like to install Python now? (Y/N): "
    if /i "%install_python%"=="Y" goto check_winget_en
    goto end
)

:check_python_de
cls
echo ================================================================================
echo Überprüfe Python-Installation...
echo ================================================================================
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python ist bereits installiert.
    echo Drücke Enter um fortzufahren und die notwendigen Module zu installieren...
    pause >nul
    goto install_modules_de
) else (
    echo Python ist nicht installiert!
    set /p install_python="Möchten Sie Python jetzt installieren? (J/N): "
    if /i "%install_python%"=="J" goto check_winget_de
    goto end
)

:check_python_fr
cls
echo ================================================================================
echo Vérification de l'installation de Python...
echo ================================================================================
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Python est déjà installé.
    echo Appuyez sur Entrée pour continuer avec l'installation des modules...
    pause >nul
    goto install_modules_fr
) else (
    echo Python n'est pas installé!
    set /p install_python="Voulez-vous installer Python maintenant? (O/N): "
    if /i "%install_python%"=="O" goto check_winget_fr
    goto end
)

:check_winget_en
cls
echo ================================================================================
echo Checking if winget is installed...
echo ================================================================================
winget --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ================================================================================
    echo Winget is not installed. Please install it manually from:
    echo https://aka.ms/getwinget and restart the script.
    echo ================================================================================
    pause
    goto end
)
goto install_python_en

:check_winget_de
cls
echo ================================================================================
echo Überprüfe ob winget installiert ist...
echo ================================================================================
winget --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ================================================================================
    echo Winget ist nicht installiert. Bitte installieren Sie es manuell von:
    echo https://aka.ms/getwinget und starten Sie das Skript erneut.
    echo ================================================================================
    pause
    goto end
)
goto install_python_de

:check_winget_fr
cls
echo ================================================================================
echo Vérification si winget est installé...
echo ================================================================================
winget --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ================================================================================
    echo Winget n'est pas installé. Veuillez l'installer manuellement à partir de :
    echo https://aka.ms/getwinget et redémarrez le script.
    echo ================================================================================
    pause
    goto end
)
goto install_python_fr

:install_python_en
cls
echo ================================================================================
echo Installing Python...
echo ================================================================================
winget install Python.Python.3
if %errorlevel% neq 0 (
    echo ================================================================================
    echo Python installation failed. Please install Python manually and restart the script.
    echo ================================================================================
    pause
    goto end
)
goto install_modules_en

:install_python_de
cls
echo ================================================================================
echo Python wird installiert...
echo ================================================================================
winget install Python.Python.3
if %errorlevel% neq 0 (
    echo ================================================================================
    echo Fehler bei der Python-Installation. Bitte installieren Sie Python manuell und starten Sie das Skript erneut.
    echo ================================================================================
    pause
    goto end
)
goto install_modules_de

:install_python_fr
cls
echo ================================================================================
echo Installation de Python...
echo ================================================================================
winget install Python.Python.3
if %errorlevel% neq 0 (
    echo ================================================================================
    echo Échec de l'installation de Python. Veuillez installer Python manuellement et redémarrer le script.
    echo ================================================================================
    pause
    goto end
)
goto install_modules_fr

:install_modules_en
cls
echo ================================================================================
echo Installing required Python modules...
echo ================================================================================
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install elevate speedtest-cli chardet psutil

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

:install_modules_de
cls
echo ================================================================================
echo Installiere notwendige Python-Module...
echo ================================================================================
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install elevate speedtest-cli chardet psutil

if %errorlevel% == 0 (
    echo ================================================================================
    echo Installation der notwendigen Komponenten erfolgreich abgeschlossen!
    echo Starte nun die PCOptimus.py Datei, um das Tool zu nutzen.
    echo ================================================================================
) else (
    echo ================================================================================
    echo Fehler bei der Installation der Module. Bitte versuchen Sie es erneut.
    echo ================================================================================
)
pause
goto end

:install_modules_fr
cls
echo ================================================================================
echo Installation des modules Python nécessaires...
echo ================================================================================
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install elevate speedtest-cli chardet psutil

if %errorlevel% == 0 (
    echo ================================================================================
    echo Installation des composants nécessaires terminée avec succès!
    echo Lancez maintenant le fichier PCOptimus.py pour utiliser l'outil.
    echo ================================================================================
) else (
    echo ================================================================================
    echo Erreur lors de l'installation des modules. Veuillez réessayer.
    echo ================================================================================
)
pause
goto end

:end
exit