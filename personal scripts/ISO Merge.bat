@ECHO OFF

:merge
set /p dir="What is the FULL DIRECTORY of the folder with the ISO parts (ex. C:\bla\bla\bla): "
cd %dir%
set /p name="Enter ISO Name: "
copy /b *.part0.iso+*.part1.iso+*.part2.iso+*.part3.iso+*.part4.iso+*.part5.iso+*.part6.iso+*.part7.iso+*.part8.iso %name%.iso
if %ERRORLEVEL% == 0 goto :endofscript
echo No ISO part files were found! Ensure you are in the right folder and try again.
pause
cls
goto :merge

:endofscript
echo The ISO merge was successful!
pause