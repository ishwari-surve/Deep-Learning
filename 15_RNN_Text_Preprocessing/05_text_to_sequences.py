# ============================================================
# Program Name : Text to Sequences using Keras
# Program No.  : 005
#
# Description  : This program demonstrates how to convert
#                complete sentences into numerical sequences
#                using the Keras Tokenizer.
#
#                It first creates a vocabulary by using
#                fit_on_texts() and then converts each
#                sentence into a list of numerical word
#                indices using texts_to_sequences().
#
#                Each word is replaced with its corresponding
#                numerical index from the generated vocabulary.
#
#                This process converts textual data into
#                numerical sequences that can be used as
#                input for Recurrent Neural Network (RNN)
#                models.
#
# Author       : Ishwari Vijaykumar Surve
# Language     : Python
# Framework    : TensorFlow / Keras
# Topic        : Deep Learning - RNN Text Preprocessing
# Concepts     : Tokenization, Vocabulary, Word Indexing,
#                fit_on_texts(), texts_to_sequences(),
#                Numerical Text Representation
# ============================================================

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

print("=" * 60)
print("   Deep Learning : RNN Text Preprocessing")
print("   Program 5 : Text to Sequences")
print("=" * 60)

print("Target of this Program:")
print("Convert each sentence into a sequence of numbers")
print("-" * 60)

print("Word Index:")
print(tokenizer.word_index)
print("-" * 60)

for sentence, sequence in zip(sentences, sequences):
    print("Sentence :", sentence)
    print("Sequence :", sequence)
    print("-" * 60)

print("Conclusion:")
print("A sentence is now represented as a list of word numbers.")
