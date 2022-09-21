import urllib.request
import shutil
from vars import (
    ps_script_name,
    ps_script_url,
    openssh_msi_name,
    openssh_download_url,
    path_local,
)
from functions import (
    download_install_google,
    download_install_google_zip,
    execute,
)


def install_chocolatey():
    print("Instalando Chocolatey...")
    try:
        ps_script_path = path_local / ps_script_name
        urllib.request.urlretrieve(ps_script_url, ps_script_path)
        command = "powershell.exe -noprofile -executionpolicy bypass -file " + str(
            ps_script_path
        )
        execute(command)
    except Exception as e:
        print(e.args[0])


def install_chocolatey_program(programa, cmd):
    if not shutil.which("choco"):
        install_chocolatey()
    print(f"Instalando {programa}")
    try:
        execute("choco install -y " + cmd)
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

