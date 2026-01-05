@echo off
cd /d "%~dp0"
echo [SYSTEM] Starting Cyber Cops Master Sync...
git add .
git commit -m "Enterprise Architecture Locked - Path Fix"
git push origin main
echo [SUCCESS] Software is now Live on GitHub!
pause