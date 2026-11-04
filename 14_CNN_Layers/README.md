# 14 CNN Layers

## About
These programs show every step of a CNN with NumPy, without any library for the layers.
The network looks at a small image and decides: Vertical Line or Horizontal Line.

## CNN pipeline
1. Convolution: a kernel moves over the image and creates a feature map.
2. ReLU: negative values become 0.
3. Max Pooling: the biggest value of each 2x2 block is kept. The size becomes smaller.
4. Flatten: the matrix becomes a single list of values.
5. Fully Connected layer: values x weights, added with bias, give a score.
6. Prediction: score above 0 means Vertical Line, otherwise Horizontal Line.

## Key points
- Convolution output size = image size - kernel size + 1.
- Kernel used: [-1, 1, -1] in each row. It detects a vertical line.
- ReLU removes negative values from the feature map.
- Pooling keeps the strongest feature and reduces size.
- Flatten is needed because the fully connected layer takes a list, not a matrix.
- Weights in the fully connected layer are fixed values here. Training is not done.

## Files
| File | What it does |
|---|---|
| 01_cnn_convolution_relu_pooling_fc.py | Full pipeline on a 5x5 image. Prints every calculation and shows each result as a graph. |
| 02_cnn_convolution_relu_pooling_fc_graphical.py | Same pipeline with step by step visuals. A yellow box shows the kernel and pooling block moving, with a pause between steps. |
| 03_cnn_relu_pooling_flatten.py | Starts from a ready 4x4 feature map. Shows ReLU, pooling, flatten and the fully connected layer. No graphs. |
| 04_cnn_pipeline_large_image.py | Pipeline on a 6x6 image with a 3x4 kernel and pooling with stride 1. Shows the flatten, fully connected and output layers as a network diagram. |

## Sample result of file 03
- Feature map after ReLU, pooling gives: 5, 4, 3, 6
- Fully connected: weights 0.8, 0.5, 0.3, 0.9 and bias 1.0
- Final output = 13.3, so the prediction is Strong Feature Detected

## Concepts covered
- Convolution, kernel, feature map
- ReLU activation
- Max pooling (size and stride)
- Flatten
- Fully connected layer
- np.maximum, np.max, flatten()
- plt.imshow and plt.text to show values inside cells
- Rectangle patch to highlight the current region

## Requirements
- Python 3
- NumPy
- Matplotlib

## Run
python 01_cnn_convolution_relu_pooling_fc.py

Note:
- Files 01, 02 and 04 ask for input. Enter 1 for Vertical Line or 2 for Horizontal Line.
- These files open many graph windows. Close each window to see the next step.
- This folder is the theory base for Keras CNN models (Conv2D, MaxPooling2D, Flatten, Dense).
