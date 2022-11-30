import urllib.request
import shutil
from vars import (
    ps_script_name,
    ps_script_url,
    openssh_msi_name,
    openssh_download_url,
    path_local,
    choco_path,
)
from functions import (
    download_install_google,
    download_install_google_zip,
    execute,
    execute_powershell,
)


def install_chocolatey():
    print("Instalando Chocolatey...")
    try:
        command = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        execute_powershell(command)
    except Exception as e:
        print(e.args[0])


def install_chocolatey_program(programa, cmd):
    try:
        execute(f"{choco_path} install -y " + cmd)
    except Exception as e:
        print(e.args[0])


def install_google_chrome():
    install_chocolatey_program("Chrome", "googlechrome")


def install_firefox():
    install_chocolatey_program("Firefox", "firefox")


def install_rsync():
    install_chocolatey_program("Rsync", "rsync")

def install_openssh():
    openssh_msi_path = path_local / openssh_msi_name
    urllib.request.urlretrieve(openssh_download_url, openssh_msi_path)
    command = ' msiexec /i' + str(openssh_msi_path)
    execute(command)

