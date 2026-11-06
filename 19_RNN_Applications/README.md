# 19 RNN Applications

## About
Three small applications that use a SimpleRNN in Keras.
Each one shows a different kind of RNN task:
1. Predict the next character.
2. Classify the sentiment of a sentence.
3. Predict the next number in a sequence.

## Applications
| Task | Input | Output | Output layer | Loss |
|---|---|---|---|---|
| Character prediction | 3 characters | next character | Dense 4, softmax | categorical_crossentropy |
| Sentiment analysis | sentence | Positive or Negative | Dense 1, sigmoid | binary_crossentropy |
| Sequence prediction | 5 numbers | next number | Dense 1, no activation | mse |

## 1. Character prediction
- Text: "hellohellohellohello" (a repeating pattern).
- Unique characters: e, h, l, o. Each character gets a number.
- Sliding window of 3 characters gives the next character. Example: "hel" gives "l".
- Output is one-hot encoded with to_categorical.
- Input is reshaped to (samples, time steps, features) = (17, 3, 1).
- Model: SimpleRNN 16 units (tanh), then Dense with softmax.
- Trained for 300 epochs. Test input h, e, l should give l.

## 2. Sentiment analysis
- Dataset: 10 short movie review sentences, 5 positive and 5 negative.
- Steps: Tokenizer, texts_to_sequences, pad_sequences (length 5).
- Model: Embedding (8 values per word), SimpleRNN 8 units (tanh), Dense 1 (sigmoid).
- Trained for 30 epochs.
- Tested on two new sentences: "I enjoyed this film" and "I hated this film".
- A word not
