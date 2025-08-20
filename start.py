import subprocess
import os

def run_ps1_script():

    ps1_script = r"start_chat.ps1"

    result = subprocess.run([
        "powershell", 
        "-ExecutionPolicy", "Bypass",
        "-File", ps1_script
    ], capture_output=True, text=True)
    
    print("Return code:", result.returncode)
    print("STDOUT:", result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr)

run_ps1_script()