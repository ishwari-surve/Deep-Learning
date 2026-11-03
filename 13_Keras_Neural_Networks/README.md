# 13 Keras Neural Networks

## About
Keras is the easy interface of TensorFlow for building neural networks.
These programs build the first Keras models: regression, binary classification
and image classification.

## Model building steps
1. Create the model with Sequential.
2. Add layers with Dense.
3. Compile the model: choose optimizer, loss and metrics.
4. Train with model.fit().
5. Evaluate with model.evaluate().
6. Predict with model.predict().

## Key points
- Dense layer = fully connected layer.
- ReLU is used in hidden layers.
- Sigmoid in the output layer gives a probability for 2 classes.
- Softmax in the output layer gives probabilities for many classes.
- Regression uses loss = mse.
- Binary classification uses loss = binary_crossentropy.
- Multi-class classification uses loss = sparse_categorical_crossentropy.
- Pixel values are divided by 255 to bring them between 0 and 1.
- Flatten converts a 28x28 image into a vector of 784 values.
- np.argmax picks the class with the highest probability.

## Files
| File | What it does |
|---|---|
| 01_simple_neural_network.py | Regression. Learns the pattern output = 2 x input. Hidden layer of 4 neurons. Predicts for input 6. |
| 02_binary_classification.py | Pass or Fail from study hours and attendance. Layers 8, 4, 1 (sigmoid). Prints probability and class. |
| 03_fashion_mnist_image_classification.py | Classifies clothing images (10 classes) from the Fashion MNIST dataset using Flatten, Dense 128 and Dense 10 (softmax). |

## Model details
| File | Layers | Loss | Epochs |
|---|---|---|---|
| 01 | Dense 4 (relu), Dense 1 | mse | 200 |
| 02 | Dense 8 (relu), Dense 4 (relu), Dense 1 (sigmoid) | binary_crossentropy | 200 |
| 03 | Flatten, Dense 128 (relu), Dense 10 (softmax) | sparse_categorical_crossentropy | 10 |

## Concepts covered
- Sequential, Dense, Flatten
- compile, fit, evaluate, predict
- Adam optimizer
- Accuracy metric
- Loading a dataset with keras.datasets
- Normalization of images
- Showing images with plt.imshow

## Requirements
- Python 3
- TensorFlow
- NumPy
- Matplotlib
- Internet on the first run of file 03, to download the dataset

## Run
python 01_simple_neural_network.py
python 02_binary_classification.py
python 03_fashion_mnist_image_classification.py

Note: file 03 first opens 10 image windows, then a grid of 25 images. Close each window to continue to training.
