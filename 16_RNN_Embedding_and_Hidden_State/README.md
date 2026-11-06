# 16 RNN Embedding and Hidden State

## About
After text is changed into number sequences, two ideas are needed before the RNN:
1. Embedding: each word number becomes a vector of numbers.
2. Hidden state: the memory of the RNN, updated at every word.

## Key points
- Embedding gives each word a vector, so the network can learn the meaning of words.
- Padding index 0 has a vector of zeros.
- Embedding layer output shape = (samples, time steps, embedding size).
- Time step = the position of one word in the sentence. RNN reads one word per time step.
- Hidden state is the memory. It stores information from the words already read.
- At each time step, the new hidden state is made from the current word and the old hidden state.

## RNN formula
h_t = tanh(Wx * x_t + Wh * h_t-1 + bias)

| Symbol | Meaning |
|---|---|
| x_t | current input |
| h_t-1 | previous hidden state |
| Wx | weight for the current input |
| Wh | weight for the previous hidden state |
| h_t | new hidden state |

## Manual example (file 05)
- Sentence: "food was not good", sequence [1, 2, 5, 3]
- Wx = 0.5, Wh = 0.8, bias = 0.1, starting hidden state = 0
- Hidden state after each word: 0.54, 0.91, 0.997, 0.98 (rounded)
- The last hidden state holds the meaning of the full sentence.

## Files
| File | What it does |
|---|---|
| 01_embedding_manual.py | Shows embedding as a table: token number to a vector of 3 values |
| 02_embedding_keras.py | Uses the Keras Embedding layer on padded sequences and prints the vectors and output shape |
| 03_time_steps.py | Shows that the RNN reads one word at each time step |
| 04_hidden_state.py | Shows hidden state as memory that grows with each word |
| 05_manual_rnn_calculation.py | Calculates the hidden state at each time step with the RNN formula |

## Concepts covered
- Embedding (manual and Keras)
- Embedding layer: input_dim, output_dim
- Time steps
- Hidden state
- tanh activation
- np.tanh

## Requirements
- Python 3
- NumPy (file 05)
- TensorFlow (file 02 only)

## Run
python 01_embedding_manual.py
python 05_manual_rnn_calculation.py

Note:
- Files 01, 03, 04 use plain Python.
- In file 02 the vectors are random, because the Embedding layer is not trained yet.
