Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "Start_Tool.bat" & Chr(34), 0
Set WinScriptHost = Nothing