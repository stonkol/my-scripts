# Metadata Removal (exiftool)
1. Install exiftool `$ brew install exiftool`
1. Create a new AppleScript Application [Exiftool-remove-metadata.scpt](https://github.com/stonkol/my-scripts/blob/main/Exiftool-remove-metadata.scpt)
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
