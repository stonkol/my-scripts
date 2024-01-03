# install `pip install pixelart-scaler`, works better with PNG, if they are JPG:
# `for file in *.jpg; do convert "$file" "${file%.jpg}.png"; done`
# WHAT IS: batch scale images without "blurring" them on Linux using 'pixelart-scaler'
#!/bin/bash

input_dir="path/to/your/input/directory" #replace to your path
output_dir="path/to/your/output/directory" #replace to your path
scale_factor=16  # Adjust as needed

for file in "$input_dir"/*.png; do
    filename=$(basename "$file")
    output_file="$output_dir/${filename%.*}_scaled.png"
    pixelart-scaler "$file" "$output_file" --scale-factor $scale_factor

# After saving this file...
# In the Terminal navigate to your script directory. 
# Run this to make the script executable: `batch_scale_pixelart-scaler_linux.sh`
# Execute the script: `./batch_scale_pixelart-scaler_linux.sh`
