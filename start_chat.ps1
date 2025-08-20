$current_dir = Get-Location
$venv_path = "$current_dir\venv"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$current_dir'; .\venv\Scripts\activate; python main.py"