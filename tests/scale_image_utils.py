# image_utils.py
from PIL import Image
from PIL.Image import Resampling
import os
import subprocess

def batch_resize(input_folder, output_folder, scale_factor):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                new_size = (int(img.width * scale_factor), int(img.height * scale_factor))

                resized_img = img.resize(
                    new_size,
                    Resampling.NEAREST if hasattr(Resampling, 'NEAREST')
                                    else Image.Resampling.NEAREST
                )
                resized_img.save(output_path)
