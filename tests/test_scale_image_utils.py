# test_image_utils.py
import os
from PIL import Image
from scale_image_utils import batch_resize

def test_batch_resize_creates_resized_image(tmp_path):
    # Setup input and output directories
    input_folder = tmp_path / "input"
    output_folder = tmp_path / "output"
    input_folder.mkdir()
    output_folder.mkdir()

    # Create a dummy image (10x10 red square)
    img_path = input_folder / "test.png"
    img = Image.new("RGB", (10, 10), color="red")
    img.save(img_path)

    # Run batch_resize with scale factor 2
    batch_resize(str(input_folder), str(output_folder), 2)

    # Check if resized image exists
    resized_img_path = output_folder / "test.png"
    assert resized_img_path.exists()

    # Optional: Open resized image and check size
    with Image.open(resized_img_path) as resized_img:
        assert resized_img.size == (20, 20)
