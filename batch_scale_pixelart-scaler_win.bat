# install ` pip install pixelart-scaler`, works better on png, if you have jpg use this script:
# for %i in (*.jpg) do convert "%i" "%~ni.png" #  (using ImageMagick's convert)
# WHAT IS: batch scale images without "blurring" them on Windows using 'pixelart-scaler'
#!/bin/bash

@echo off
set input_folder=path\to\input\folder
set output_folder=path\to\output\folder
set scale_factor=16

if not exist "%output_folder%" mkdir "%output_folder%"

for %%i in ("%input_folder%\*.png") do (
    set output_file="%output_folder%\%%~nxi"
    pixelart-scaler "%%i" %output_file% --scale-factor %scale_factor%
)

# After saving this file...
# Execute the script: `batch_scale_pixelart-scaler_win.bat`
