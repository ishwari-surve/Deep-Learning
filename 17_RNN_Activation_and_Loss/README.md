# 17 RNN Activation and Loss

## About
An RNN sentiment model uses two activation functions and one loss function:
1. tanh inside the RNN layer, to keep the hidden state controlled.
2. sigmoid at the output, to give a Positive or Negative decision.
3. binary cross entropy, to measure how wrong the prediction is.

## Tanh
- Formula: tanh(x) = (e^x - e^-x) / (e^x + e^-x)
- Output is between -1 and +1.
- Negative input gives a negative output. Zero gives 0.
- It keeps the hidden state values in a controlled range.

| Input | tanh |
|---|---|
| -3 | -0.9951 |
| -1 | -0.7616 |
| 0 | 0 |
| 1 | 0.7616 |
| 3 | 0.9951 |

## Sigmoid
- Formula: sigmoid(x) = 1 / (1 + e^-x)
- Output is between 0 and 1.
- 0.5 or more is Positive. Below 0.5 is Negative.

| Input | sigmoid | Decision |
|---|---|---|
| -3 | 0.0474 | Negative |
| -1 | 0.2689 | Negative |
| 0 | 0.5 | Positive |
| 1 | 0.7311 | Positive |
| 3 | 0.9526 | Positive |

## Binary cross entropy loss
- Formula: Loss = -[y * log(p) + (1 - y) * log(1 - p)]
- y is the actual label (0 or 1). p is the predicted probability.
- A good prediction gives a small loss.
- A wrong and confident prediction gives a large loss.

| Actual | Predicted | Loss |
|---|---|---|
| 1 | 0.90 | 0.1054 |
| 1 | 0.60 | 0.5108 |
| 1 | 0.20 | 1.6094 |
| 0 | 0.10 | 0.1054 |
| 0 | 0.40 | 0.5108 |
| 0 | 0.80 | 1.6094 |

## Files
| File | What it does |
|---|---|
| 01_tanh.py | Prints tanh for -3, -1, 0, 1, 3 |
| 02_sigmoid.py | Prints sigmoid for the same values, with the Positive or Negative decision |
| 03_binary_cross_entropy_loss.py | Calculates the loss for 6 examples of good and bad predictions |

## Concepts covered
- tanh activation (np.tanh)
- sigmoid activation (np.exp)
- Decision threshold 0.5
- Binary cross entropy loss (np.log)

## Requirements
- Python 3
- NumPy

## Run
python 01_tanh.py
python 02_sigmoid.py
python 03_binary_cross_entropy_loss.py
