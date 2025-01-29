import requests
import sys
import os
import webbrowser

print("2898 Scouter Installer")

file_urls = [
    "https://ant-throw-pology.github.io/2898-scouter/index.html",
    "https://ant-throw-pology.github.io/2898-scouter/index.css",
    "https://ant-throw-pology.github.io/2898-scouter/index.js",
    "https://ant-throw-pology.github.io/2898-scouter/favicon.svg",
    "https://raw.githubusercontent.com/droid-kk11/2898-scouter-installer/refs/heads/main/uninstall.bat",
    "https://raw.githubusercontent.com/droid-kk11/2898-scouter-installer/refs/heads/main/uninstall-mac.sh",
    "https://raw.githubusercontent.com/droid-kk11/2898-scouter-installer/refs/heads/main/uninstall-linux.sh",
]

username = os.getlogin()
if os.name == "posix":
    if username != "root":
        install_dir = f"/home/{username}/portable/2898.Scouter/"
        portable_dir = f"/home/{username}/portable/"
        uninstall_script = "uninstall-linux.sh" if sys.platform.startswith("linux") else "uninstall-mac.sh"
    else:
        print("This installer cannot be run in a root shell or via sudo. Quitting.")
        sys.exit()
elif os.name == "nt":
    if username in ["Public", "SYSTEM", "TrustedInstaller"]:
        print("This installer cannot be run as a system user account. Quitting.")
        sys.exit()
    else:
        install_dir = f"C:\\Users\\{username}\\portable\\2898.Scouter\\"
        portable_dir = f"C:\\Users\\{username}\\portable\\"
        uninstall_script = "uninstall.bat"

print(f"The scouting app will install to: {install_dir}")
continue_ = input("Continue? [Y/N]: ")
if continue_.lower() == "n":
    sys.exit()

os.makedirs(install_dir, exist_ok=True)
print("Created install directory")

# Download files
for file in file_urls:
    fail_count = 0
    response = requests.get(file)
    file_name = file.split("/")[-1]
    save_path = os.path.join(install_dir, file_name)

    while fail_count < 5:
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"File {file_name} saved to {save_path}")
            break
        else:
            fail_count += 1
            if fail_count == 5:
                print(f"Failed to download {file_name}. Aborting installation.")
                sys.exit()
            print(f"Retrying download {file_name}... (Attempt {fail_count})")

print("All files downloaded successfully.")

index_html = os.path.join(install_dir, "index.html")

# **Step 1: Open index.html in the default browser**
webbrowser.open(f"file://{index_html}")

# **Step 2: Create launch & uninstall shortcuts**
def create_shortcuts():
    uninstall_path = os.path.join(install_dir, uninstall_script)

    if os.name == "nt":
        # **Windows Shortcuts**
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        app_list = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs")
        
        # Create "Open 2898 Scouter" shortcut
        scouter_shortcut = os.path.join(desktop, "2898 Scouter.url")
        with open(scouter_shortcut, "w") as shortcut:
            shortcut.write(f"[InternetShortcut]\nURL=file:///{index_html.replace('\\', '/')}\n")
        
        # Create "Uninstall 2898 Scouter" shortcut
        uninstall_shortcut = os.path.join(app_list, "Uninstall 2898 Scouter.bat")
        with open(uninstall_shortcut, "w") as batch_file:
            batch_file.write(f'@echo off\nstart "" "{uninstall_path}"\nexit')

        print(f"Shortcuts created:\n- {scouter_shortcut}\n- {uninstall_shortcut}")

    elif sys.platform == "darwin":  # **macOS**
        user_apps_folder = os.path.expanduser("~/Applications")
        os.makedirs(user_apps_folder, exist_ok=True)  # Ensure it exists

        # Create "Open 2898 Scouter" alias
        scouter_alias = os.path.join(user_apps_folder, "2898_Scouter.webloc")
        with open(scouter_alias, "w") as alias:
            alias.write(f"""<?xml version='1.0' encoding='UTF-8'?>
<!DOCTYPE plist PUBLIC '-//Apple//DTD PLIST 1.0//EN' 'http://www.apple.com/DTDs/PropertyList-1.0.dtd'>
<plist version='1.0'>
<dict>
    <key>URL</key>
    <string>file://{index_html}</string>
</dict>
</plist>
""")

        # Create "Uninstall 2898 Scouter" launcher
        uninstall_shortcut = os.path.join(user_apps_folder, "Uninstall 2898 Scouter.command")
        with open(uninstall_shortcut, "w") as command_file:
            command_file.write(f"#!/bin/bash\nchmod +x '{uninstall_path}'\n'{uninstall_path}'")

        os.system(f"chmod +x '{uninstall_shortcut}'")

        print(f"Shortcuts created:\n- {scouter_alias}\n- {uninstall_shortcut}")

    else:  # **Linux**
        desktop_entry = f"""[Desktop Entry]
Type=Application
Name=2898 Scouter
Exec=xdg-open file://{index_html}
Icon=html
Terminal=false
Categories=Utility;
"""

        uninstall_entry = f"""[Desktop Entry]
Type=Application
Name=Uninstall 2898 Scouter
Exec=sh -c 'chmod +x {uninstall_path}; {uninstall_path}'
Icon=utilities-terminal
Terminal=true
Categories=Utility;
"""

        local_applications = os.path.expanduser("~/.local/share/applications")
        os.makedirs(local_applications, exist_ok=True)

        scouter_desktop = os.path.join(local_applications, "2898_scouter.desktop")
        uninstall_desktop = os.path.join(local_applications, "uninstall_2898_scouter.desktop")

        with open(scouter_desktop, "w") as desktop_file:
            desktop_file.write(desktop_entry)
        with open(uninstall_desktop, "w") as uninstall_file:
            uninstall_file.write(uninstall_entry)

        os.chmod(scouter_desktop, 0o755)
        os.chmod(uninstall_desktop, 0o755)

        print(f"Shortcuts created:\n- {scouter_desktop}\n- {uninstall_desktop}")

# Call function to create shortcuts
create_shortcuts()

# **Step 3: Ensure uninstall scripts are executable (macOS/Linux)**
if os.name == "posix":
    os.system(f"chmod +x '{install_dir}/uninstall-mac.sh'")
    os.system(f"chmod +x '{install_dir}/uninstall-linux.sh'")

print("Installation complete. You can now access the 2898 Scouter!")

