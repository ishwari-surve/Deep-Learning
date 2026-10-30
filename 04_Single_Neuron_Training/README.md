# 04 Single Neuron Training

## About
How a neuron learns. The weight starts random and is corrected step by step.

## Learning steps
1. Predict: predicted = x * weight
2. Error: error = actual - predicted
3. Loss: loss = error^2
4. Update: weight = weight + (learning_rate * error * x)

## Example
Input = 2, expected output = 10, learning rate = 0.1. The weight moves toward 5.

## Files
| File | What it does |
|---|---|
| 01_training_steps.py | Training loop with printed steps (10 steps) |
| 02_training_steps_graphical.py | Same, plus 3 graphs: loss, prediction vs actual, weight change (20 steps) |

## Requirements
- Python 3
- Matplotlib

## Run
python 01_training_steps.py
