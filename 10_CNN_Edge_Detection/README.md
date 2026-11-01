# 10 CNN Edge Detection

## About
Convolution is the main operation of a CNN. A small kernel (filter) moves over the image
and finds features like edges. The result is called a feature map.

## Setup used
- Image: 6x6 grayscale. Top 3 rows are black (0), bottom 3 rows are white (255).
- Kernel: 3x3, detects horizontal edges.

  [-1 -1 -1]
  [ 0  0  0]
  [ 1  1  1]

- Output size = (6 - 3 + 1) x (6 - 3 + 1) = 4x4

## Convolution steps
1. Take a 3x3 region from the image.
2. Multiply it with the kernel, element by element.
3. Add all values. This gives one output value.
4. Move the kernel one step and repeat.
5. All output values together form the feature map.

## Result
- Rows of the feature map where black meets white have a high value (765). This is the edge.
- Rows with no change have value 0.

## Files
| File | What it does |
|---|---|
| 01_edge_detection.py | Convolution written by hand using loops and NumPy |
| 02_edge_detection_result_display.py | Same convolution, prints every step and shows image, kernel and feature map |
| 03_edge_detection_animation.py | Shows each kernel position as a figure with 4 panels (image, region, kernel, feature map) |
| 04_edge_detection_canny.py | Edge detection on a real image using OpenCV Canny |
| sample.png | Input image for file 04 |

## Concepts covered
- Kernel, convolution, feature map
- Slicing a region: image[i:i+3, j:j+3]
- Element-wise multiplication and np.sum
- plt.imshow with cmap="gray"
- cv2.cvtColor, cv2.Canny, cv2.imshow

## Requirements
- Python 3
- NumPy
- Matplotlib
- opencv-python

## Run
python 01_edge_detection.py

Note: file 03 opens 16 windows, one for each step. Close each window to see the next step.
File 04 needs sample.png in the same folder. Press any key to close its windows.
