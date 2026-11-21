
# ============================================================
# Program  : TensorFlow Variables
# Author    : Ishwari Vijaykumar Surve
# Target:
# Create and update TensorFlow variables using assign(),
# assign_add() and assign_sub() operations
# ============================================================

import tensorflow as tf

print("=" * 60)
print("   Deep Learning : TensorFlow Basics")
print("   Program 33 : TensorFlow Variable Example")
print("=" * 60)

# Create a variable
weight = tf.Variable(5.0)

print("Initial Weight Value:")
print(weight.numpy())
print()

# Update variable value
weight.assign(10.0)
print("Updated Weight Value:")
print(weight.numpy())
print()

# Add value to variable
weight.assign_add(2.5)
print("After assign_add(2.5):")
print(weight.numpy())
print()

# Subtract value from variable
weight.assign_sub(1.5)
print("After assign_sub(1.5):")
print(weight.numpy())
