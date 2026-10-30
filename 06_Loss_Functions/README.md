# 06 Loss Functions


## About
A loss function measures how wrong the prediction is. Lower loss means a better model.

## Loss functions
| Loss | Formula | Used for |
|---|---|---|
| MSE | average of (y_true - y_pred)^2 | Regression |
| MAE | average of abs(y_true - y_pred) | Regression |
| Binary Cross Entropy | -(y*log(p) + (1-y)*log(1-p)) | 0/1 classification |

## Key points
- MSE punishes big errors more than MAE.
- In Binary Cross Entropy, p is limited between 0.001 and 0.999 to avoid log(0).

## Files
| File | Sample output |
|---|---|
| 01_mse.py | 5.67 |
| 02_mae.py | 2.33 |
| 03_binary_cross_entropy.py | about 0.184 |

## Requirements
- Python 3

## Run
python 01_mse.py
