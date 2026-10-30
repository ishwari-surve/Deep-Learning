# 02 Activation Functions

## About
An activation function decides the output of a neuron. This folder covers ReLU and Sigmoid, with graphs.

## Key points
- ReLU = max(0, z). Negative becomes 0. Used in hidden layers.
- Sigmoid = 1 / (1 + e^-z). Output is between 0 and 1. Used in the output layer for probability.

## Files
| File | What it does |
|---|---|
| 01_relu.py | Neuron with ReLU, plus ReLU graph |
| 02_sigmoid.py | Neuron with Sigmoid, plus Sigmoid graph |
| 03_sigmoid_vs_relu.py | Same neuron with both activations, plus comparison graph |

## Requirements
- Python 3
- NumPy
- Matplotlib

## Run
python 01_relu.py
