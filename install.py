import os
import sys

def install():
    try:
        os.makedirs("/usr/share/aut", exist_ok=True)
        os.chmod("autoTOR.py", 0o755)
        os.system("cp autoTOR.py /usr/share/aut/autoTOR.py")

        cmnd = '#!/bin/sh\nexec python3 /usr/share/aut/autoTOR.py "$@"'
        with open("/usr/bin/aut", "w") as file:
            file.write(cmnd)
        os.chmod("/usr/bin/aut", 0o755)
        print('\n\nCongratulations, auto Tor IP Changer is installed successfully. From now just type "aut" in terminal.')
    except Exception as e:
        print(f"Error occurred during installation: {e}")
        sys.exit(1)

def uninstall():
    try:
        os.system("rm -rf /usr/share/aut")
        os.system("rm /usr/bin/aut")
        print("[!] Now Auto Tor IP changer has been removed successfully.")
    except Exception as e:
        print(f"Error occurred during uninstallation: {e}")
        sys.exit(1)

def main():
    choice = input("[+] To install press (Y), to uninstall press (N) >> ")
    if choice.lower() == "y":
        install()
    elif choice.lower() == "n":
        uninstall()
    else:
        print("Invalid choice. Please enter 'Y' for install or 'N' for uninstall.")

if __name__ == "__main__":
    main()
