# 18 RNN Sentiment Model

## About
This folder builds a complete RNN sentiment model in Keras.
It joins all the steps from folders 15, 16 and 17: preprocessing, embedding,
RNN layer, sigmoid output and binary cross entropy loss.
The model reads a sentence and says Positive or Negative.

## Dataset
| Sentence | Label |
|---|---|
| food was good | 1 (Positive) |
| food was bad | 0 (Negative) |
| food was not good | 0 (Negative) |
 
## Model architecture
| Layer | Settings | Job |
|---|---|---|
| Embedding | input_dim = 6, output_dim = 8 | Word number to a vector of 8 values |
| SimpleRNN | 8 units, tanh | Reads words one by one and keeps memory |
| Dense | 1 unit, sigmoid | Gives a value between 0 and 1 |

## Flow
Input Sentence -> Tokenization -> Padding -> Embedding -> SimpleRNN -> Dense -> Sigmoid output

## Training settings
- Optimizer: Adam
- Loss: binary_crossentropy
- Metric: accuracy
- Epochs: 800
- Padding: pre, max length 4

## Prediction flow
1. Convert the sentence into a sequence of numbers.
2. Map each word to its number.
3. Pad the sequence to length 4.
4. The model gives a value between 0 and 1.
5. Value 0.5 or more is Positive. Below 0.5 is Negative.

## Key points
- vocab_size = number of unique words + 1 = 6.
- return_sequences=False means the RNN gives only the last hidden state to the Dense layer.
- model.build(input_shape=(None, 4)) fixes the input size so that summary() works.
- The dataset has only 3 sentences, so this is a learning demo only.
- The model is tested on its own training sentences.
- A word that is not in the vocabulary gives an error in file 03.

## Files
| File | What it does |
|---|---|
| 01_rnn_architecture.py | Builds Embedding, SimpleRNN and Dense layers and prints the model summary |
| 02_train_model.py | Prepares the data, compiles the model and trains it for 800 epochs. Prints final loss and accuracy. |
| 03_prediction_flow.py | Trains the model and shows each prediction step for a sentence |
| 04_complete_sentiment_application.py | Final program. All steps in one file, with predictions for all 3 sentences. |

## Concepts covered
- Sequential model
- Embedding, SimpleRNN, Dense layers
- model.build, model.summary
- compile, fit, predict
- Tokenizer and pad_sequences
-
