# install `pip3 install Pillow`, works better with PNG, if they are JPG:
# `for file in *.jpg; do sips -s format png "$file" --out "${file%.jpg}.png"; done` #using sips(a command-line tool that is included with macOS) 
# WHAT IS: batch scale images without "blurring" them on macOS using 'pillow'

from PIL import Image
import os

def batch_resize(input_folder, output_folder, scale_factor):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open the image
            image = Image.open(input_path)

            # Calculate the new size
            new_size = (image.width * scale_factor, image.height * scale_factor)

            # Resize using nearest-neighbor resampling
            resized_image = image.resize(new_size, Image.NEAREST)

            # Save the resized image
            resized_image.save(output_path)

if __name__ == "__main__":
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"
    scale_factor = 16  # Adjust the scale factor as needed

    batch_resize(input_folder, output_folder, scale_factor)

