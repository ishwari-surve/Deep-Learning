# 18 RNN Sentiment Model

## About
This folder builds a complete RNN sentiment model in Keras.
It joins all the steps from folders 15, 16 and 17: preprocessing, embedding,
RNN layer, sigmoid output and binary cross entropy loss.
The model reads a sentence and says Positive or Negative.
The last file shows the same flow with every calculation done by hand.

## Dataset
| Sentence | Label |
|---|---|
| food was good | 1 (Positive) |
| food was bad | 0 (Negative) |
| food was not good | 0 (Negative) |

## Model architecture (files 01 to 04)
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

## Manual calculation (file 05)
- Sentence: "food was not good", tokens [1, 2, 5, 3]
- Embedding is a lookup table. The token number is the row number.
- Each word vector has 3 values. RNN weights are fixed: Wx (3x3), Wh (3x3), bias.
- Formula at each time step: h_t = tanh(Wx . x_t + Wh . h_previous + b)
- Hidden state after each word:

| Word | Hidden state |
|---|---|
| food | [0.2636, 0.3004, 0.2821] |
| was | [0.5397, 0.4486, 0.5928] |
| not | [0.7636, 0.6734, 0.7504] |
| good | [0.8753, 0.8315, 0.9098] |

- Dense layer: z = Wy . h_final + by, with Wy = [-2.0, -1.5, -1.2] and by = 1.0
- z = -3.0897
- Sigmoid(z) = 0.0435, which is below 0.5, so the prediction is Negative.
- The weights are fixed by hand. The model is not trained in this file.

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
| 04_complete_sentiment_application.py | All steps in one file, with predictions for all 3 sentences |
| 05_rnn_detailed_math_graphical.py | Full mathematical demo with NumPy. Shows embedding lookup, RNN, dense layer and sigmoid step by step, with 7 graphs. |

## Concepts covered
- Sequential model
- Embedding, SimpleRNN, Dense layers
- model.build, model.summary
- compile, fit, predict
- Tokenizer and pad_sequences
- Sigmoid output and the 0.5 threshold
- Matrix and vector multiplication inside an RNN
- Hidden state and memory flow

## Requirements
- Python 3
- NumPy
- Matplotlib (file 05)
- TensorFlow (files 01 to 04)

## Run
python 01_rnn_architecture.py
python 04_complete_sentiment_application.py
python 05_rnn_detailed_math_graphical.py

Note:
- Files 02, 03 and 04 train the model for 800 epochs. This takes a few seconds.
- File 05 opens 7 graph windows. Close each window to see the next step.
