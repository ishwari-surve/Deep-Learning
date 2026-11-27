# ============================================================
# Program Name : Split Sentence into Words
# Program No.  : 002
#
# Description  : This program demonstrates how a sentence
#                is divided into individual words using
#                Python's split() method.
#
#                It extracts each word from the input
#                sentence and displays its position using
#                the enumerate() function.
#
#                This demonstrates how text data is
#                processed word by word in sequence before
#                being used as input for an RNN model.
#
# Author       : Ishwari Vijaykumar Surve
# Language     : Python
# Topic        : Deep Learning - Recurrent Neural Network (RNN)
# Concepts     : String split(), enumerate(), Word Tokenization,
#                Sequential Text Processing
# ============================================================

sentence = "food was not good"

words = sentence.split() 

print("=" * 60)
print("   Deep Learning : RNN Text Preprocessing")
print("   Program 2 : Split Sentence into Words")
print("=" * 60)

print("Target of this Program:")
print("Split sentence into individual words")
print("-" * 60)
 
print("Original Sentence:", sentence)
print("Total Words:", len(words))
print("-" * 60)

for index, word in enumerate(words):
    print("Position", index + 1, ":", word)

print("-" * 60)
print("Conclusion:")
print("RNN processes sentence one word at a time.")
