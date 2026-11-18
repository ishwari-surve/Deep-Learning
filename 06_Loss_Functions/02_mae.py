# ============================================================
# Program  : MAE (Mean Absolute Error) Loss
# Author    : Ishwari Vijaykumar Surve
# Target:
# Calculate the Mean Absolute Error between actual and
# predicted values
# Formula   : MAE = sum of abs(y_true - y_pred) / n
# ============================================================

print("=" * 60)
print("   Deep Learning : Loss Functions")
print("   Program 14 : MAE Loss Demonstration")
print("=" * 60)


def MAE(y_true, y_pred):
    n = len(y_true)
    total_error = 0

    for i in range(n):
        error = abs(y_true[i] - y_pred[i])
        total_error += error

    mae = total_error / n
    return mae


# Sample Data
y_true = [10, 20, 30]
y_pred = [12, 18, 33]

loss = MAE(y_true, y_pred)
print("MAE Loss:", loss)
