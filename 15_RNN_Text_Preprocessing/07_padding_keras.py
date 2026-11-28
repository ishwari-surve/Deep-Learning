# ============================================================
# Program Name : Padding using Keras
# Program No.  : 07
#
# Description  : This program demonstrates how to apply
#                padding to numerical text sequences using
#                the Keras pad_sequences() function.
#
#                It first converts sentences into numerical
#                sequences using the Keras Tokenizer.
#
#                The pad_sequences() function is then used
#                to make all sequences equal in length.
#
#                Pre-padding is applied by adding zeros
#                at the beginning of shorter sequences.
#
#                This ensures that all input sequences have
#                a fixed length before being passed to an
#                RNN model.
#
# Author       : Ishwari Vijaykumar Surve
# Language     : Python
# Framework    : TensorFlow / Keras
# Topic        : Deep Learning - RNN Text Preprocessing
# Concepts     : Tokenization, Numerical Sequences,
#                pad_sequences(), Pre-padding,
#                Fixed-Length Input Sequences
# ============================================================

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

max_length = 4

padded_sequences = pad_sequences(
    sequences,
    maxlen=max_length,
    padding="pre"
)

print("=" * 60)
print("   Deep Learning : RNN Text Preprocessing")
print("   Program 7 : Padding using Keras")
print("=" * 60)

print("Target of this Program:")
print("Apply padding to make all sequences length 4")
print("-" * 60)

print("Maximum Length:", max_length)
print("Padding Type   : pre")
print("Padding Value  : 0")
print("-" * 60)

for sentence, sequence, padded in zip(sentences, sequences, padded_sequences):
    print("Sentence          :", sentence)
    print("Original Sequence :", sequence)
    print("Padded Sequence   :", padded)
    print("-" * 60)
