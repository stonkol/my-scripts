## Install ImageMagick on Mac:
In terminal enter `$ brew install imagemagick`

## Batch Upscaling with ImageMagick:
Assuming your images are in a directory named input and you want to save the upscaled images to a directory named output, you can use the following command:
`$ mogrify -path output -resize 1600x1600 -filter point -type TrueColor input/*.png`

> [!WARNING]
> The `mogrify` command modifies the input images in place.
> If you want to keep the original images, consider copying them to a new directory before running the command.

1. `path output`: Specifies the output directory where the upscaled images will be saved.
1. `resize 1600x1600`: Sets the maximum size to which the images will be resized. You can adjust these values based on your specific requirements.
1. `filter point`: Specifies the nearest-neighbor interpolation method, which maintains the pixelated appearance.
1. `type TrueColor`: Ensures that the output images are in TrueColor format.
input/*.png: Specifies the input directory and the type of files to be processed (in this case, all PNG files).
