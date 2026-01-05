@echo off
E:
cd "CDR Tool"
echo [SYSTEM] Starting Cyber Cops Master Sync...
git add .
git commit -m "Enterprise Architecture Locked - Version Fix"
git push origin main
echo [SUCCESS] Software is now Live on GitHub!
pause