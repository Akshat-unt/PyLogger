Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "cmd /c Python-Updater.bat"
oShell.Run strArgs, 0, false