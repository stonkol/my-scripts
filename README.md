# my scripts

## The Scripts

1. **Batch Media Compressor**: sort all the videos in a folder and compress them with `ffmpeg`. For inf

1. **Batch Upscaler**: batch scale images without "blurring" them on macOS using 'pillow'

1. **Metadata Remover**: using `exiftool`

1. **Weather CLI Tool**: written in Go, using data from [weather api](www.weatherapi.com).

## todo list

- [ ] script to remove files (pics+vids...) that are not in the new version of that folder
- [ ] batch scale pixelart `.py` -> `.go`
- [ ] implement features of `weather-cli-learn` into weather `go.main`

## Batch Upscaler

Install ImageMagick on Mac:
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

## Metadata Remover: (exiftool)

1. Install exiftool `$ brew install exiftool`
1. Create a new AppleScript Application
   - In Script Editor paste this [Exiftool-remove-metadata.scpt](https://github.com/stonkol/my-scripts/blob/main/Exiftool-remove-metadata.scpt)
   - Save as an Application
      - Click on "File" in the menu bar > click "Export" or "Save As"
      - Choose "Application" from the "File Format/Format" dropdown menu.
      - Click "Save".
1. Set Up a Smart Folder
   - Open Finder.
   - Click on "File" in the menu bar and select "New Smart Folder."
   - Click on the "+" button in the top-right corner of the Smart Folder window to add criteria.
   - Set the criteria to search for files in the specific folder you want (e.g., Downloads or Desktop).
1. Automate the Script Execution
   - Move the AppleScript application you created to a convenient location.
   - Right-click on the Smart Folder you created and select "Folder Actions Setup."
   - Check the box for "Enable Folder Actions" in the Folder Actions Setup window.
   - Drag the AppleScript application onto the right side of the Folder Actions Setup window, where it says "Attach folder action:"
   - Close the Folder Actions Setup window.

Now, any file you place into the smart folder should trigger the AppleScript, which will attempt to remove metadata using exiftool.

> [!IMPORTANT]
> The effectiveness of this approach depends on the specific metadata you want to remove and the file types involved. Also, exiftool might not remove all types of metadata for all file formats.

### List of metadata types that exiftool can handle:

1. EXIF Data (Exchangeable image file format): Camera settings (aperture, shutter speed, ISO, etc.). Date and time information. GPS coordinates. Camera make and model. Software used for processing the image.
1. IPTC Data (International Press Telecommunications Council): Caption and description. Keywords. Object name. By-line (photographer's name).
1. XMP Data (Extensible Metadata Platform): Extensible metadata in XML format. Often includes information similar to EXIF and IPTC.
1. ICC Profiles (International Color Consortium): Color profiles associated with the image.
1. Adobe APP14 Segment: Adobe-specific metadata often found in JPEG images.
1. MakerNotes: Manufacturer-specific metadata embedded by the camera.
1. QuickTime Data: Metadata in QuickTime files (MOV).
1. PDF Metadata: Metadata embedded in PDF documents.
1. PNG Textual Data: Textual information stored in PNG images.
1. Other Formats: exiftool supports a wide range of file types, including various image formats (JPEG, PNG, TIFF, GIF, etc.), audio files, video files, PDFs, and more.

# Split Image

Equally divide the image into 9 equally portions. Is at `split-image.py`.
