import subprocess
import urllib.request
from pathlib import Path

path_local = Path('.')
script_url = 'https://community.chocolatey.org/install.ps1'
ps_script_name = 'install_chocolatey.ps1'
ps_script_path = path_local / ps_script_name
urllib.request.urlretrieve(script_url, ps_script_path)

command = 'powershell.exe -noprofile -executionpolicy bypass -file ' + str(ps_script_path)

subprocess.call(command, shell=True)