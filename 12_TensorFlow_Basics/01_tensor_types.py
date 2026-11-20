# ============================================================
# Program 30 : TensorFlow Tensor Types
# Author    : Ishwari Vijaykumar Surve
# Target:
# Create scalar, 1D, 2D and 3D tensors and print their shapes
# ============================================================

import tensorflow as tf

print("=" * 60)
print("   Deep Learning : TensorFlow Basics")
print("   Program 30 : TensorFlow Tensor Creation Example")
print("=" * 60)

# Scalar tensor (single value)
scalar_tensor = tf.constant(10)
print("Scalar Tensor:")
print(scalar_tensor)
print()

# 1D tensor (vector)
vector_tensor = tf.constant([10, 20, 30, 40])
print("1D Tensor / Vector:")
print(vector_tensor)
print()

# 2D tensor (matrix)
matrix_tensor = tf.constant([
    [1, 2, 3],
    [4, 5, 6]
])
print("2D Tensor / Matrix:")
print(matrix_tensor)
print()

# 3D tensor
tensor_3d = tf.constant([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print("3D Tensor:")
print(tensor_3d)
print()

# Show shape of tensors
print("Shape of scalar tensor:", scalar_tensor.shape)
print("Shape of vector tensor:", vector_tensor.shape)
print("Shape of matrix tensor:", matrix_tensor.shape)
print("Shape of 3D tensor:", tensor_3d.shape)
