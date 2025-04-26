################################################################
# WHAT IS: batch scale images without "blurring" them on macOS using 'pillow'
################################################################
# Install `pip3 install Pillow`
# Works better with PNG, for JPG:
# ```py
# for file in *.jpg; do
#  sips -s format png "$file" --out "${file%.jpg}.png"; done` #using sips(a command-line tool that is included with macOS)
################################################################

from PIL import Image
from PIL.Image import Resampling  # Required for Pillow ≥10.0.0
import os

def batch_resize(input_folder, output_folder, scale_factor):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                new_size = (int(img.width * scale_factor),
                           int(img.height * scale_factor))
                # Version-compatible resampling
                resized_img = img.resize(
                    new_size,
                    Resampling.NEAREST if hasattr(Resampling, 'NEAREST')
                                    else Image.NEAREST
                )
                resized_img.save(output_path)

if __name__ == "__main__":
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"
    scale_factor = 8  # Adjust scale factor as needed

    batch_resize(input_folder, output_folder, scale_factor)
