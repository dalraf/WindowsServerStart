from pathlib import Path

# Chocolatey install list

# Parametros Chocolatey
ps_script_url = "https://community.chocolatey.org/install.ps1"
ps_script_name = "install_chocolatey.ps1"

# Parametros Caixa
caixa_google_id = "1u0JnYuLxxcOgMTU5iYwMR20SOwBq3vaB"
caixa_file_name = "Setup.jar"

# Parametros Adobe Air
adobeair_google_id = "13fUuPTnwpzIoydnefw9bcdX2h5KbJb0N"
adobeair_file_name = "AdobeAir.exe"

# Parametros Sisbr2.0
sisbr20_google_id = "13E-X5fZZrj2FMZDIcLWJ94c9DgTqUA3f"
sisbr20_file_name = "Sisbr2.0.exe"

# Parametros Citrix10
citrix_google_id = "19o1eGqGL6xR1B9b3VYunea4zzYe3Heb9"
citrix_file_name = "Citrix10.zip"

openssh_download_url = 'https://github.com/PowerShell/Win32-OpenSSH/releases/download/v8.9.1.0p1-Beta/OpenSSH-Win32-v8.9.1.0.msi'
openssh_msi_name = 'OpenSSH-Win32-v8.9.1.0.msi'

path_local = Path("./downloads").absolute()
path_local.mkdir(parents=True, exist_ok=True)
