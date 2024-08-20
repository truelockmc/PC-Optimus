@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

rem Set the log file path
set logfile=log.txt

rem Start logging
echo ==== Starting setup.bat ====> %logfile%
echo ==== Starting setup.bat ====> %logfile% >> %logfile%

rem Check if the script is running with administrator privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrative privileges. Relaunching with elevation... >> %logfile%
    powershell -Command "Start-Process cmd -ArgumentList '/c %~0 %*' -Verb RunAs" >> %logfile% 2>&1
    exit /b
)

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
python --version >nul 2>>%logfile%
if %errorlevel% == 0 (
    echo Python is already installed.
    echo Press Enter to proceed with module installation...
    pause >nul
    goto install_modules_en
) else (
    echo Python is not installed or not found in PATH! >> %logfile%
    echo Python is not installed, but needed to run .py files. Do you want to install Python now? >> %logfile%
    set /p install_python="(Y/N): "
    if /i "%install_python%"=="Y" (
        echo Opening Python 3.12 installation page in Microsoft Store... >> %logfile%
        start ms-windows-store://pdp/?productid=9PJPW5LD2B5P
        echo ================================================================================
        echo Please press Install in the Microsoft Store to install Python.
        echo ================================================================================
        pause
        goto end
    ) else (
        echo ================================================================================
        echo Please install Python manually or you won’t be able to use PCOptimus.
        echo ================================================================================
        pause
        goto end
    )
)

:check_python_de
cls
echo ================================================================================
echo Überprüfe Python-Installation...
echo ================================================================================
python --version >nul 2>>%logfile%
if %errorlevel% == 0 (
    echo Python ist bereits installiert.
    echo Drücke Enter um fortzufahren und die notwendigen Module zu installieren...
    pause >nul
    goto install_modules_de
) else (
    echo Python ist nicht installiert oder nicht im PATH gefunden! >> %logfile%
    echo Python ist nicht installiert, wird jedoch benötigt, um .py-Dateien auszuführen. Möchten Sie Python jetzt installieren? >> %logfile%
    set /p install_python="(J/N): "
    if /i "%install_python%"=="J" (
        echo Öffne Python 3.12 Installationsseite im Microsoft Store... >> %logfile%
        start ms-windows-store://pdp/?productid=9PJPW5LD2B5P
        echo ================================================================================
        echo Bitte klicken Sie auf Installieren im Microsoft Store, um Python zu installieren.
        echo ================================================================================
        pause
        goto end
    ) else (
        echo ================================================================================
        echo Bitte installieren Sie Python manuell oder Sie können PCOptimus nicht verwenden.
        echo ================================================================================
        pause
        goto end
    )
)

:check_python_fr
cls
echo ================================================================================
echo Vérification de l'installation de Python...
echo ================================================================================
python --version >nul 2>>%logfile%
if %errorlevel% == 0 (
    echo Python est déjà installé.
    echo Appuyez sur Entrée pour continuer avec l'installation des modules...
    pause >nul
    goto install_modules_fr
) else (
    echo Python n'est pas installé ou introuvable dans PATH! >> %logfile%
    echo Python n'est pas installé, mais est nécessaire pour exécuter des fichiers .py. Voulez-vous installer Python maintenant? >> %logfile%
    set /p install_python="(O/N): "
    if /i "%install_python%"=="O" (
        echo Ouverture de la page d'installation de Python 3.12 dans le Microsoft Store... >> %logfile%
        start ms-windows-store://pdp/?productid=9PJPW5LD2B5P
        echo ================================================================================
        echo Veuillez appuyer sur Installer dans le Microsoft Store pour installer Python.
        echo ================================================================================
        pause
        goto end
    ) else (
        echo ================================================================================
        echo Veuillez installer Python manuellement ou vous ne pourrez pas utiliser PCOptimus.
        echo ================================================================================
        pause
        goto end
    )
)

:install_modules_en
cls
echo ================================================================================
echo Installing required Python modules...
echo ================================================================================
python -m ensurepip --upgrade >> %logfile% 2>&1
python -m pip install --upgrade pip >> %logfile% 2>&1
python -m pip install speedtest-cli chardet psutil wmi >> %logfile% 2>&1

if %errorlevel% == 0 (
    echo ================================================================================
    echo Installation of required components completed successfully!
    echo Now start the PCOptimus.py file to use the tool.
    echo ================================================================================
) else (
    echo ================================================================================
    echo Error installing modules. Please check %logfile% for details.
    echo ================================================================================
)
pause
goto end

:install_modules_de
cls
echo ================================================================================
echo Installiere notwendige Python-Module...
echo ================================================================================
python -m ensurepip --upgrade >> %logfile% 2>&1
python -m pip install --upgrade pip >> %logfile% 2>&1
python -m pip install speedtest-cli chardet psutil wmi >> %logfile% 2>&1

if %errorlevel% == 0 (
    echo ================================================================================
    echo Installation der notwendigen Komponenten erfolgreich abgeschlossen!
    echo Starte nun die PCOptimus.py Datei, um das Tool zu nutzen.
    echo ================================================================================
) else (
    echo ================================================================================
    echo Fehler bei der Installation der Module. Bitte überprüfen Sie %logfile% für Details.
    echo ================================================================================
)
pause
goto end

:install_modules_fr
cls
echo ================================================================================
echo Installation des modules Python nécessaires...
echo ================================================================================
python -m ensurepip --upgrade >> %logfile% 2>&1
python -m pip install --upgrade pip >> %logfile% 2>&1
python -m pip install speedtest-cli chardet psutil wmi >> %logfile% 2>&1

if %errorlevel% == 0 (
    echo ================================================================================
    echo Installation des composants nécessaires terminée avec succès!
    echo Lancez maintenant le fichier PCOptimus.py pour utiliser l'outil.
    echo ================================================================================
) else (
    echo ================================================================================
    echo Erreur lors de l'installation des modules. Veuillez vérifier %logfile% pour les détails.
    echo ================================================================================
)
pause
goto end

:end
echo ==== Script ended ====> %logfile%
echo ==== Script ended ====> %logfile% >> %logfile%
exit
