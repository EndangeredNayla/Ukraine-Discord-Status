@echo off
rmdir bin /s /q
pyinstaller -n UkraineStatus --onefile --noupx --icon=icon.ico "main.py"
rmdir build /s /q
REN dist bin
PAUSE
