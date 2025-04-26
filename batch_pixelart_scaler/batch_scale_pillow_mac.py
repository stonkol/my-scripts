################################################################
# WHAT IS: batch scale images without "blurring" them on macOS using 'pillow'
################################################################
# You need to install `pip3 install Pillow`
# Works better with PNG, for JPG:
# ```py
# for file in *.jpg; do
#  sips -s format png "$file" --out "${file%.jpg}.png"; done` #using sips(a command-line tool that is included with macOS)
################################################################

from PIL import Image
from PIL.Image import Resampling  # Required for Pillow ≥10.0.0
import os
import subprocess  # For opening images on macOS

def batch_resize(input_folder, output_folder, scale_factor):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open the image
            with Image.open(input_path) as img:
                # Calculate the new size
                new_size = (int(img.width * scale_factor),
                           int(img.height * scale_factor))

                # Resize using nearest-neighbor resampling
                resized_img = img.resize(
                    new_size,
                    Resampling.NEAREST if hasattr(Resampling, 'NEAREST')
                                    else Image.Resampling.NEAREST
                )
                # Save the resized image
                resized_img.save(output_path)

            # Open the resized image using macOS 'open' command
            subprocess.run(["open", output_path])

if __name__ == "__main__":
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"
    scale_factor = 8  # Adjust scale factor as needed

    batch_resize(input_folder, output_folder, scale_factor)
