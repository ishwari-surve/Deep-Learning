# 05 Multi Neuron Training

## About
Training a small network: 2 inputs, 2 hidden neurons (ReLU), 1 output neuron.
All 6 weights and 3 biases start random. Input = (2, 3), expected output = 8.

## Settings
- Learning rate: 0.01
- Training steps: 50

## Note
The hidden layer update is a simplified teaching version. Real backpropagation is in folder 07.

## Files 
| File | What it does |
|---|---|
| 01_multi_neuron_training.py | Training loop with 5 graphs (loss, prediction, hidden outputs, weights) |
| 02_multi_neuron_training_graphical.py | Adds final network diagram with all trained values |
| 03_multi_neuron_training_animation.py | Adds animation of the learning process |

## Requirements
- Python 3
- Matplotlib

## Run
python 01_multi_neuron_training.py
