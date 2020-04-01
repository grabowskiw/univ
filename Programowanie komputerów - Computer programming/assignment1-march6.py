@echo off
@chcp 65001>nul

set /p haslo="Hasło: "
if %haslo%==IwB goto ok
if not %haslo%==IwB exit

:ok
color 2b
cls
echo.
echo 1 otwórz Notatnik
echo 2 otwórz wp.pl
echo 3 lista aktywnych procesów
echo 4 foldery zalogowanego użytkownika
echo 5 drzewo katalogów
echo 6 sprawdzenie połączenia z Internetem
echo 0 wyłącz komputer
echo.
set /p option="Którą opcję wykonać?: "
if %option%==1 start notepad
if %option%==2 start chrome http://wp.pl
if %option%==3 tasklist | more
if %option%==4 cd C: && cd /Users/%USERNAME% && dir
if %option%==5 tree
if %option%==6 (
ping usz.edu.pl>nul
if errorlevel 1 ( echo BRAK POŁĄCZENIA )
if errorlevel 0 ( echo INTERNET DZIAŁA )
)
if %option%==0 shutdown
