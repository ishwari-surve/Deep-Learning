# 08 Feedforward Neural Network (FNN)

## About
A Feedforward Neural Network passes data in one direction: input layer, hidden layers, output layer.
These programs use scikit-learn (MLPRegressor and MLPClassifier) to solve small real problems.

## Key points
- Regression predicts a number (example: salary).
- Classification predicts a class (example: Pass or Fail).
- Scaling is done with StandardScaler.
- fit_transform is used on training data only. transform is used on test data and new data.
- hidden_layer_sizes=(5,) means 1 hidden layer with 5 neurons.
- hidden_layer_sizes=(8, 4) means 2 hidden layers with 8 and 4 neurons.

## Files
| File | What it does |
|---|---|
| 01_salary_prediction_regression.py | Predicts salary from experience, education, skill and certificates. Scales both input and output. |
| 02_student_result_classification.py | Predicts Pass or Fail from study hours, attendance and assignment score. No scaling. |
| 03_student_result_classification_scaling.py | Same problem, with scaling, stratify and lbfgs solver for better results. |
| 04_placement_prediction.py | Full pipeline: read CSV, analyse, split, scale, train, evaluate, graphs, save and load model, predict. |
| placement_data.csv | Dataset used by file 04. |

## Dataset (placement_data.csv)
Input columns: Aptitude, Coding, Communication, Academics, Internship
Target column: Placed (1 = Placed, 0 = Not Placed)

## Concepts covered
- MLPRegressor, MLPClassifier
- train_test_split
- StandardScaler and inverse_transform
- Accuracy, confusion matrix, classification report
- predict_proba (prediction probability)
- Loss curve
- Saving and loading a model with joblib

## Requirements
- Python 3
- scikit-learn
- pandas
- numpy
- matplotlib
- joblib

## Run
python 01_salary_prediction_regression.py

Note: file 04 needs placement_data.csv in the same folder.
It creates placement_fnn_model.pkl and placement_scaler.pkl when it runs.
