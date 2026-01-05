@echo off
cd /d "%~dp0"
echo Starting Cyber Cops Powerhouse...
python -m streamlit run app.py
pause