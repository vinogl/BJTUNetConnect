@echo off

mkdir package
cd package

call:generate_exe message w
call:generate_exe connect c


:generate_exe
pyinstaller -F -%~2 -i ..\Logo\%~1.ico ..\%~1.py
move .\dist\%~1.exe %~1.exe
del %~1.spec
rmdir /s /Q build
rmdir /s /Q dist
goto:eof

