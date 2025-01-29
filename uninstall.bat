@echo off
echo Uninstalling 2898 Scouter...

:: Delete the main installation folder and its contents
del /Q "%USERPROFILE%\portable\2898.Scouter\*"
rmdir /S /Q "%USERPROFILE%\portable\2898.Scouter"

:: Remove the desktop shortcut
del "%USERPROFILE%\Desktop\2898 Scouter.url"

:: Remove the uninstall shortcut from the Start Menu
del "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Uninstall 2898 Scouter.bat"

echo Uninstallation complete!
pause
