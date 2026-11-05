#!/usr/bin/env bash
# Install with: python3 -m pip install pixelart-scaler
set -euo pipefail

input_dir="path/to/your/input/directory" # replace with your path
output_dir="path/to/your/output/directory" # replace with your path
scale_factor=16

if [[ ! -d "$input_dir" ]]; then
    echo "Input directory does not exist: $input_dir" >&2
    exit 1
fi
mkdir -p "$output_dir"
shopt -s nullglob
files=("$input_dir"/*.png)
if ((${#files[@]} == 0)); then
    echo "No PNG files found in $input_dir"
    exit 0
fi

for file in "${files[@]}"; do
    filename=$(basename "$file")
    output_file="$output_dir/${filename%.*}_scaled.png"
    pixelart-scaler "$file" "$output_file" --scale-factor "$scale_factor"
done
