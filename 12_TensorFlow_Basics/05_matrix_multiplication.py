# ============================================================
# Program  : TensorFlow Matrix Multiplication
# Author    : Ishwari Vijaykumar Surve
# Target:
# Perform matrix multiplication using tf.matmul()
# ============================================================

import tensorflow as tf

print("=" * 60)
print("   Deep Learning : TensorFlow Basics")
print("   Program 34 : Matrix Multiplication Example")
print("=" * 60)

# Create two matrices
matrix1 = tf.constant([
    [1, 2],
    [3, 4]
], dtype=tf.float32)

matrix2 = tf.constant([
    [5, 6],
    [7, 8]
], dtype=tf.float32)

print("Matrix 1:")
print(matrix1)
print()

print("Matrix 2:")
print(matrix2)
print()

# Matrix multiplication
result = tf.matmul(matrix1, matrix2)

print("Matrix Multiplication Result:")
print(result)
