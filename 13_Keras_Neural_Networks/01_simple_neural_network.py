# ============================================================
# Program 36 : Simple Neural Network using Keras
# Author    : Ishwari Vijaykumar Surve
# Target:
# Build a small Keras network that learns the pattern
# output = 2 x input, then predict the output for input 6
# ============================================================

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

print("=" * 60)
print("   Deep Learning : Keras Neural Networks")
print("   Program 36 : Simple Neural Network")
print("=" * 60)

# Sample input and output
X = np.array([[1], [2], [3], [4], [5]], dtype=float)
Y = np.array([[2], [4], [6], [8], [10]], dtype=float)

# Create model
model = Sequential()

# Add one hidden layer with 4 neurons
model.add(Dense(4, activation='relu', input_shape=(1,)))

# Add output layer
model.add(Dense(1))

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X, Y, epochs=200, verbose=0)

print("Training completed")

# Test prediction
test_value = np.array([[6]], dtype=float)
prediction = model.predict(test_value, verbose=0)

print(f"Prediction for input 6: {prediction[0][0]:.4f}")
