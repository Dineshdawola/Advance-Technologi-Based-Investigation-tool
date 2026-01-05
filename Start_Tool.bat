@echo off
:: Drive switch ki tension khatam, folder location se hi run hoga
cd /d "%~dp0"
echo Starting Cyber Cops Software...
python -m streamlit run app.py
pause