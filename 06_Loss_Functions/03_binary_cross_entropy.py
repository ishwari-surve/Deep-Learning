# ============================================================
# Program 15 : Binary Cross Entropy Loss
# Author    : Ishwari Vijaykumar Surve
# Target:
# Calculate the Binary Cross Entropy loss for 0/1 classification
# Formula   : -(y * log(p) + (1 - y) * log(1 - p))
# ============================================================

import math

print("=" * 60)
print("   Deep Learning : Loss Functions")
print("   Program 15 : Binary Cross Entropy Demonstration")
print("=" * 60)


def Binary_CrossEntropy(y_true, y_pred):
    total_loss = 0
    n = len(y_true)

    for i in range(n):
        y = y_true[i]
        p = y_pred[i]

        # Avoid log(0)
        p = max(min(p, 0.999), 0.001)

        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        total_loss += loss

    return total_loss / n


# Sample Data
y_true = [1, 0, 1]
y_pred = [0.9, 0.2, 0.8]

loss = Binary_CrossEntropy(y_true, y_pred)
print("Binary Cross Entropy Loss:", loss)
