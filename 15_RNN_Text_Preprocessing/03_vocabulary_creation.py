# ============================================================
# Program Name : Manual Vocabulary Creation
# Program No.  : 003
#
# Description  : This program demonstrates how to create a
#                vocabulary manually from a given text dataset.
#
#                It extracts individual words from sentences
#                using the split() method and stores only
#                unique words in a vocabulary list.
#
#                It also assigns a unique numerical index
#                to each vocabulary word using enumerate().
#
#                This process helps understand how text data
#                is represented numerically before being
#                processed by an RNN model.
#
# Author       : Ishwari Vijaykumar Surve
# Language     : Python
# Topic        : Deep Learning - Recurrent Neural Network (RNN)
# Concepts     : Vocabulary Creation, Word Tokenization,
#                Unique Words, Word Indexing, enumerate()
# ============================================================

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

vocabulary = []

print("=" * 60)
print("   Deep Learning : RNN Text Preprocessing")
print("   Program 3 : Manual Vocabulary Creation")
print("=" * 60)

print("Target of this Program:")
print("Create vocabulary manually from sentences")
print("-" * 60)

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

print("Vocabulary List:")
print(vocabulary)
print("-" * 60)

print("Manual Word Index:")
for index, word in enumerate(vocabulary, start=1):
    print(f"{word:10s} ---> {index}")

print("-" * 60)
print("Conclusion:")
print("Vocabulary contains all unique words from dataset.")
