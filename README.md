# 2898 Scouter Installer
The official installer for [2898 Scouter](https://github.com/Ant-Throw-Pology/2898-scouter). Version numbering of the installer is unrelated to the scouter.

Available for Windows, macOS, and Linux. Please test it out and let us know how it goes. If you run into any issues, please be sure to open an issue. For any code suggestions, please be sure to make a PR.

Tested on:

- [ ] Windows
- [X] Linux (tested here more often, on Arch Linux)
- [ ] Mac OS

To use the latest development installer (assuming you have Python installed):
1. Download `installer.py` from this repository.
2. Install the python module `requests`. For Ubuntu/Debian, run `sudo apt install python3-requests`. For Arch Linux, run `sudo pacman -S python-requests`. For Windows/macOS, run `pip3 install requests` or `pip install requests`.
3. Run the installer with `python3 installer.py` or `python installer.py` (assuming you are in the same directory where you saved the installer. Do NOT run the installer as SYSTEM, TrustedInstaller, or Public (on Windows), or root (on macOS/Linux).
4. The installer should run!
To use the latest stable installer:
1. Download the latest binary for your OS in the releases tab (use the Ubuntu one regardless of Linux distro).
2. Open a terminal and change directory to the same directory as the downloaded binary. (On Windows, you may be able to run the installer by double clicking the exe file).
3. Run the installer with either ```2898_Scouter_Installer_win.exe``` (for Windows), ```chmod +x 2898_Scouter_Installer_mac && ./2898_Scouter_Installer_mac``` (for macOS), or ```chmod +x 2898_Scouter_Installer_linux && ./2898_Scouter_Installer_linux``` (for Linux).
4. The installer should run!

# Uninstall
To uninstall, use the app titled "Uninstall 2898 Scouter" in your apps list. Within 15 seconds, the app should uninstall.
