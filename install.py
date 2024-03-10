import os

def install():
    os.system('chmod 777 autoTOR.py')
    os.system('mkdir /usr/share/aut')
    os.system('cp autoTOR.py /usr/share/aut/autoTOR.py')

    cmnd = '#! /bin/sh \n exec python3 /usr/share/aut/autoTOR.py "$@"'
    with open('/usr/bin/aut', 'w') as file:
        file.write(cmnd)
    os.system('chmod +x /usr/bin/aut & chmod +x /usr/share/aut/autoTOR.py')
    print('\n\nCongratulations, auto Tor IP Changer is installed successfully. From now just type "aut" in terminal.')

def uninstall():
    os.system('rm -r /usr/share/aut')
    os.system('rm /usr/bin/aut')
    print('[!] Now Auto Tor IP changer has been removed successfully.')

def main():
    choice = input('[+] To install press (Y), to uninstall press (N) >> ')
    if str(choice).lower() == 'y':
        install()
    elif str(choice).lower() == 'n':
        uninstall()
    else:
        print("Invalid choice. Please enter 'Y' for install or 'N' for uninstall.")

if __name__ == "__main__":
    main()
