@echo off
setlocal
rem Install with: py -m pip install pixelart-scaler
set "input_folder=path\to\input\folder"
set "output_folder=path\to\output\folder"
set "scale_factor=16"

if not exist "%input_folder%\" (
    echo Input folder does not exist: "%input_folder%"
    exit /b 1
)
if not exist "%output_folder%\" mkdir "%output_folder%"
if errorlevel 1 exit /b 1

set "found=0"
for %%I in ("%input_folder%\*.png") do if exist "%%~fI" (
    set "found=1"
    pixelart-scaler "%%~fI" "%output_folder%\%%~nI_scaled.png" --scale-factor %scale_factor%
    if errorlevel 1 exit /b 1
)
if "%found%"=="0" echo No PNG files found in "%input_folder%".
endlocal
