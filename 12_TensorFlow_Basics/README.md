# 12 TensorFlow Basics

## About
TensorFlow is a library for Deep Learning. Its main data structure is the tensor.
A tensor is a multi-dimensional array of numbers. These programs cover tensor basics,
and end with a single neuron built using TensorFlow.

## Key points
- Scalar = 0D tensor (single value).
- Vector = 1D tensor.
- Matrix = 2D tensor.
- tf.constant() makes a tensor whose value cannot change.
- tf.Variable() makes a tensor whose value can change. Weights are stored as variables.
- shape tells the size of each dimension.
- reshape changes the shape, but the total number of values stays the same.
- tf.matmul() does matrix multiplication. It is the main operation inside a neural network layer.

## Files
| File | What it does |
|---|---|
| 00_check_tensorflow_version.py | Prints the installed TensorFlow version |
| 01_tensor_types.py | Creates scalar, 1D, 2D and 3D tensors and prints their shapes |
| 02_tensor_operations.py | Add, subtract, multiply, divide, square, reduce_sum and reduce_mean |
| 03_tensor_shape_reshape.py | Reshapes 12 values into (3, 4) and (2, 2, 3) |
| 04_tensor_variable.py | tf.Variable with assign, assign_add and assign_sub |
| 05_matrix_multiplication.py | Multiplies two 2x2 matrices using tf.matmul |
| 06_single_neuron.py | Single neuron: weighted sum plus bias, then sigmoid |

## Concepts covered
- tf.constant, tf.Variable
- tf.add, tf.subtract, tf.multiply, tf.divide, tf.square
- tf.reduce_sum, tf.reduce_mean, tf.cast
- tf.reshape, tensor.shape
- tf.matmul
- tf.sigmoid
- .numpy() converts a tensor to a NumPy value

## Requirements
- Python 3
- TensorFlow

## Run
python 00_check_tensorflow_version.py
python 01_tensor_types.py
