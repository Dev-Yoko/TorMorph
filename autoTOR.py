import time
import os
import subprocess
import requests

def install_package(package_name):
    try:
        check_package = subprocess.check_output(f"dpkg -s {package_name}", shell=True)
        if "install ok installed" in str(check_package):
            return
    except subprocess.CalledProcessError:
        print(f"[+] {package_name} not installed")
        subprocess.check_output("sudo apt update", shell=True)
        subprocess.check_output(f"sudo apt install {package_name} -y", shell=True)
        print(f"[!] {package_name} installed successfully")


def install_python_package(package_name):
    try:
        __import__(package_name)
    except ImportError:
        print(f"[+] python3 {package_name} is not installed")
        os.system(f"sudo pip3 install {package_name}")
        print(f"[!] python3 {package_name} is installed")


def ma_ip():
    url = "https://www.myexternalip.com/raw"
    get_ip = requests.get(
        url,
        proxies=dict(http="socks5://127.0.0.1:9050", https="socks5://127.0.0.1:9050"),
    )
    return get_ip.text


def change():
    if not os.path.exists('/run/tor'):
        try:
            os.makedirs('/run/tor', mode=0o755)
            os.chown('/run/tor', uid=116, gid=126)
        except Exception as e:
            print(f"Failed to create '/run/tor' directory: {e}")
            return

    os.system("sudo service tor reload")
    print("[+] Your IP has been Changed to : " + str(ma_ip()))


def main():
    install_package("python3-pip")
    install_python_package("requests")
    install_package("tor")

    os.system("clear")
    print(
        """\033[1;32;40m \n
                    _          _______
         /\        | |        |__   __|
        /  \  _   _| |_ ___      | | ___  _ __
       / /\ \| | | | __/ _ \     | |/ _ \| '__|
      / ____ \ |_| | || (_) |    | | (_) | |
     /_/    \_\__,_|\__\___/     |_|\___/|_|
                    V 2.1
    from Dev-Yoko
    """
    )
    print("\033[1;40;31m http://facebook.com/ninja.hackerz.kurdish/\n")

    os.system("sudo service tor start")
    time.sleep(3)
    print("\033[1;32;40m change your SOCKS to 127.0.0.1:9050 \n")
    
    try:
        x = int(input("[+] time to change IP in seconds [type=60] >> "))
        lin = int(input("[+] how many times do you want to change your IP [type=1000], for infinite IP changes type [0] >>"))
    except ValueError:
        print("[!] Invalid input. Please enter valid numbers.")
        return
    
    try:
        if lin == 0:
            while True:
                time.sleep(x)
                change()
        else:
            for i in range(lin):
                time.sleep(x)
                change()
    except KeyboardInterrupt:
        print("\nauto tor is closed ")

if __name__ == "__main__":
    main()
