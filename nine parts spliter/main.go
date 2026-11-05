   ////////////////// USAGE ////////////////////
  // go build -o image-splitter				 //
 // ./image-splitter path/to/your/image.jpg	//
/////////////////////////////////////////////

package main

import (
	"flag"
	"image/jpeg"
	"image/png"
	"log"
	"os"
)

func main() {
	flag.Parse()
	imgPath := flag.Arg(0)
	if imgPath == "" {
		log.Fatal("Please provide an image path")
	}

	// Open and decode image
	imgFile, err := os.Open(imgPath)
	if err != nil {
		log.Fatal(err)
	}
	defer imgFile.Close()

	img, format, err := image.Decode(imgFile)
	if err != nil {
		log.Fatal(err)
	}

	// Calculate tile dimensions
	bounds := img.Bouds()

	// Create output directory




	// Split into 3x3 grid


		// ...
}

func saveImage(path string, img image.Image, format string{
	f, err := os.Create(path)

	// ...

}
