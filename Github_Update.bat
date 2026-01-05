@echo off
cd /d "%~dp0"
git add .
git commit -m "Security Update: Zero-Trust Model"
git push origin main
pause