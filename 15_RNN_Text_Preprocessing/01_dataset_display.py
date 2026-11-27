# ============================================================
# Program Name : Dataset and Labels for RNN
# Program No.  : 001
#
# Description  : This program creates a simple text dataset
#                containing sentences and their corresponding
#                sentiment labels.
#
#                It demonstrates how input sentences are
#                associated with numerical output labels:
#                1 - Positive Sentiment
#                0 - Negative Sentiment
#
#                The program uses the zip() function to
#                iterate through sentences and labels
#                simultaneously and displays their meanings.
#
# Author       : Ishwari Vijaykumar Surve
# Language     : Python
# Topic        : Deep Learning - Recurrent Neural Network (RNN)
# Concepts     : Dataset Creation, Sentiment Labels,
#                Text Data and zip() Function
# ============================================================

sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1, 0, 0]

print("=" * 60)
print("   Deep Learning : RNN Text Preprocessing")
print("   Program 1 : Dataset and Labels")
print("=" * 60)

print("Target of this Program:")
print("Understand input dataset and sentiment labels")
print("-" * 60)

for sentence, label in zip(sentences, labels):
    sentiment = "Positive" if label == 1 else "Negative"

    print("Sentence :", sentence)
    print("Label    :", label)
    print("Meaning  :", sentiment)
    print("-" * 60)
