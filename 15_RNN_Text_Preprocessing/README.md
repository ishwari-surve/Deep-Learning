# 15 RNN Text Preprocessing

## About
A neural network cannot read text. Text must be changed into numbers first.
These programs show every preprocessing step before text goes into an RNN.
All programs use the same 3 sentences, so the steps are easy to follow.

## Dataset
| Sentence | Label | Meaning |
|---|---|---|
| food was good | 1 | Positive |
| food was bad | 0 | Negative |
| food was not good | 0 | Negative |

## Steps
1. Dataset and labels.
2. Split each sentence into words.
3. Build a vocabulary: every unique word gets a number.
4. Use the Keras Tokenizer to do the same automatically.
5. Convert each sentence into a sequence of numbers.
6. Sequences have different lengths, so padding is needed.
7. Pad all sequences to the same length with pad_sequences.
8. Find the vocabulary size for the Embedding layer.
9. Understand the output labels: 1 is Positive, 0 is Negative.

## Key points
- RNN reads a sentence one word at a time, in order.
- Word index: food = 1, was = 2, good = 3, bad = 4, not = 5.
- Sequence of "food was not good" is [1, 2, 5, 3].
- Neural networks need fixed-size input, so shorter sequences are padded with 0.
- padding="pre" adds the zeros at the start. [1, 2, 3] becomes [0, 1, 2, 3].
- vocab_size = number of unique words + 1. The extra 1 is for the padding index 0.
- Here vocab_size = 5 + 1 = 6.
- This is binary classification, so the output is 0 or 1.

## Files
| File | What it does |
|---|---|
| 01_dataset_display.py | Shows sentences, labels and their meaning |
| 02_tokenization.py | Splits a sentence into words and shows each position |
| 03_vocabulary_creation.py | Builds the vocabulary and word index manually |
| 04_keras_tokenization.py | Creates the word index using Keras Tokenizer |
| 05_text_to_sequences.py | Converts sentences into number sequences |
| 06_use_of_padding.py | Shows why equal length input is needed |
| 07_padding_keras.py | Pads sequences to length 4 using pad_sequences |
| 08_vocabulary_size.py | Calculates vocabulary size for the Embedding layer |
| 09_output_labels.py | Explains labels for binary sentiment classification |

## Concepts covered
- Tokenization
- Vocabulary and word index
- Tokenizer, fit_on_texts, texts_to_sequences
- pad_sequences (maxlen, padding)
- Vocabulary size
- Binary labels

## Requirements
- Python 3
- TensorFlow (only for files 04, 05, 07, 08)

## Run
python 01_dataset_display.py
python 04_keras_tokenization.py

Note: files 01, 02, 03, 06 and 09 use plain Python. No library is needed.
