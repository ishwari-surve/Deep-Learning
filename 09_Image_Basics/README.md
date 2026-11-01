# 09 Image Basics


## About
A computer sees an image as numbers. These programs show how an image is read as pixel values.
This is the base for CNN, because CNN takes these numbers as input.

## Key points
- Image = collection of pixels.
- Grayscale pixel is one value from 0 (black) to 255 (white).
- Colour pixel has 3 values: [R, G, B].
- Grayscale image shape is (28, 28).
- Colour image shape is (28, 28, 3). The 3 is the number of channels.
- 28x28 is the standard digit image size (MNIST).

## Files
| File | What it does |
|---|---|
| 01_convert_grayscale_28x28.py | Converts an image to grayscale and resizes it to 28x28 |
| 02_grayscale_pixel_display.py | Converts the image to a NumPy array and prints its pixel values |
| 03_color_image_pixel_display.py | Reads a colour image and shows shape, channels, sample pixels and RGB values |
| digit.png | Input image for file 01 |
| digit_28x28.png | Output of file 01 and input for file 02 |
| color.png | Input image for file 03 |

## Concepts covered
- Image.open, convert("L"), resize, save
- np.array(img) to convert an image into a matrix
- Shape, height, width, channels
- RGB values of one pixel

## Requirements
- Python 3
- Pillow
- NumPy

## Run
python 01_convert_grayscale_28x28.py
python 02_grayscale_pixel_display.py
python 03_color_image_pixel_display.py

Note: run file 01 before file 02, because file 02 uses digit_28x28.png.
Keep the images in the same folder as the programs.
