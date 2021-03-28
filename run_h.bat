@ECHO OFF
set timestamp=%DATE:/=-%
set timestamp=%timestamp: =%
title Butter Finger 1.0
echo Butter Finger 1.0
title 0/7
bf1.0_h.py >> %timestamp: =%_output.txt | type %timestamp: =%_output.txt
cls
title 1/7
bf1.0_h.py >> %timestamp: =%_output.txt | type %timestamp: =%_output.txt
cls
title 2/7
bf1.0_h.py >> %timestamp: =%_output.txt | type %timestamp: =%_output.txt
cls
title 3/7
bf1.0_h_h.py >> %timestamp: =%_output.txt | type %timestamp: =%_output.txt
cls
title 4/7
bf1.0_h.py >> %timestamp: =%_output.txt | type %timestamp: =%_output.txt
cls
title 5/7
bf1.0_h.py >> %timestamp: =%_output.txt | type %timestamp: =%_output.txt
cls
title 6/7
bf1.0_h.py >> %timestamp: =%_output.txt | type %timestamp: =%_output.txt
cls
title 7/7
ping -n 1 localhost >nul
title Done!

:choice
set /P c=Open Scribbler[Y/N]?
if /I "%c%" EQU "Y" goto :scribbler
if /I "%c%" EQU "N" goto :output

:scribbler
Scribbler_v1.1.1_Windows_x86\Scribbler.exe
exit

:output
set /P c=Open Output[Y/N]?
if /I "%c%" EQU "Y" goto :txt
if /I "%c%" EQU "N" goto :fin

:txt
"%timestamp: =%_output.txt"
exit