# ============================================================
# Program Name : Need of Padding in RNN
# Program No.  : 06
#
# Description  : This program demonstrates the need for
#                padding in Recurrent Neural Networks (RNN).
#
#                It uses numerical sequences of different
#                lengths to understand why input sequences
#                need to have a uniform length.
#
#                It explains that neural networks generally
#                require fixed-size input when processing
#                batches of sequences.
#
#                Padding solves this problem by adding zeros
#                to shorter sequences so that all sequences
#                have equal lengths.
#
# Author       : Ishwari Vijaykumar Surve
# Language     : Python
# Topic        : Deep Learning - RNN Text Preprocessing
# Concepts     : Sequence Length, Padding, Fixed-Size Input,
#                Numerical Text Representation
# ============================================================

sequences = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 5, 3]
]

print("=" * 60)
print("   Deep Learning : RNN Text Preprocessing")
print("   Program 6 : Need of Padding")
print("=" * 60)

print("Target of this Program:")
print("Understand the need of padding")
print("-" * 60)

print("Original Sequences:")
for sequence in sequences:
    print(sequence, "Length:", len(sequence))

print("-" * 60)
print("Problem:")
print("All sequences do not have the same length.")
print("Neural networks require fixed-size input.")

print("-" * 60)
print("Solution:")
print("Add 0 as padding to shorter sequences.")
