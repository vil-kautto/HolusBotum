CD /d "%~dp0"
python -m pip install -U discord.py[voice]
python -m pip install -U --upgrade pip
python -m pip install requests
python core.py
pause