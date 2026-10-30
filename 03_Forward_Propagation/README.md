# 03 Forward Propagation

## About
Forward propagation means passing input through all layers to get a prediction.

## Network used
- Input layer: 2 inputs
- Hidden layer: 2 neurons, ReLU
- Output layer: 1 neuron, Sigmoid
- Output 0.5 or more is Positive class, below 0.5 is Negative class

## Files
| File | What it does |
|---|---|
| 01_layered_ann.py | Function-based version using loops |
| 02_layered_ann_simplified.py | Step-by-step version, every calculation written by hand |
| 03_layered_ann_graphical.py | Same network, plus 4 graphs (network diagram, bar chart, sigmoid point, value flow) |

## Requirements
- Python 3
- NumPy
- Matplotlib

## Run
python 01_layered_ann.py
