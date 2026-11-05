// Split an image into nine tiles. Usage: image-splitter <image-path>
package main

import (
	"fmt"
	"image"
	"image/jpeg"
	"image/png"
	"log"
	"os"
	"path/filepath"
	"strings"
)

func main() {
	log.SetFlags(0)
	if len(os.Args) != 2 {
		log.Fatal("usage: image-splitter <image-path>")
	}
	imgPath := os.Args[1]
	file, err := os.Open(imgPath)
	if err != nil {
		log.Fatal(err)
	}
	img, format, err := image.Decode(file)
	closeErr := file.Close()
	if err != nil {
		log.Fatal(err)
	}
	if closeErr != nil {
		log.Fatal(closeErr)
	}
	if format != "jpeg" && format != "png" {
		log.Fatalf("unsupported image format %q (supported: JPEG, PNG)", format)
	}

	outDir := strings.TrimSuffix(imgPath, filepath.Ext(imgPath)) + "_parts"
	if err := os.MkdirAll(outDir, 0755); err != nil {
		log.Fatal(err)
	}
	bounds := img.Bounds()
	w, h := bounds.Dx(), bounds.Dy()
	if w < 3 || h < 3 {
		log.Fatal("image must be at least 3 pixels wide and 3 pixels tall")
	}
	for row := 0; row < 3; row++ {
		for col := 0; col < 3; col++ {
			x0 := bounds.Min.X + col*w/3
			x1 := bounds.Min.X + (col+1)*w/3
			y0 := bounds.Min.Y + row*h/3
			y1 := bounds.Min.Y + (row+1)*h/3
			tile := crop(img, image.Rect(x0, y0, x1, y1))
			ext := ".png"
			if format == "jpeg" {
				ext = ".jpg"
			}
			outPath := filepath.Join(outDir, fmt.Sprintf("part_%d_%d%s", row+1, col+1, ext))
			if err := saveImage(outPath, tile, format); err != nil {
				log.Fatal(err)
			}
		}
	}
	fmt.Printf("Saved nine tiles to %s\n", outDir)
}

func crop(src image.Image, rect image.Rectangle) image.Image {
	dst := image.NewRGBA(image.Rect(0, 0, rect.Dx(), rect.Dy()))
	for y := rect.Min.Y; y < rect.Max.Y; y++ {
		for x := rect.Min.X; x < rect.Max.X; x++ {
			dst.Set(x-rect.Min.X, y-rect.Min.Y, src.At(x, y))
		}
	}
	return dst
}

func saveImage(path string, img image.Image, format string) error {
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	if format == "jpeg" {
		err = jpeg.Encode(f, img, &jpeg.Options{Quality: 95})
	} else {
		err = png.Encode(f, img)
	}
	closeErr := f.Close()
	if err != nil {
		return err
	}
	return closeErr
}
