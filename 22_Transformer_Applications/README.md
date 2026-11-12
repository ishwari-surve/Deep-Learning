# 22 Transformer Applications
 
## About
Three small Transformer models built with TensorFlow and Keras.
Each one uses a different type of Transformer:
1. Encoder only: sentiment classification (like BERT).
2. Encoder and decoder: machine translation (like the original Transformer).
3. Decoder only: next word prediction and text generation (like GPT).

The datasets are very small, so these are learning demos. The models learn their training data only.

## Overview
| File | Type | Task | Output layer | Loss |
|---|---|---|---|---|
| 01 | Encoder only | Positive or Negative sentiment | Dense 1, sigmoid | binary_crossentropy |
| 02 | Encoder and decoder | English to Marathi translation | Dense (vocab size), softmax | sparse_categorical_crossentropy |
| 03 | Decoder only | Next word prediction and generation | Dense (vocab size), softmax | sparse_categorical_crossentropy |

## 1. Sentiment classification (encoder only)
- Dataset: 24 short sentences about a course, 12 positive and 12 negative.
- TextVectorization turns each sentence into 8 token numbers.
- Token embedding and position embedding (16 values) are added.
- One Transformer encoder block: multi head attention (2 heads), feed forward network (32 units), layer normalization, dropout.
- GlobalAveragePooling1D joins all word vectors into one vector.
- Then Dense 32 (ReLU), Dropout 0.2 and Dense 1 (sigmoid).
- Trained for 80 epochs with batch size 2.
- The program also shows the attention output and attention score matrix of one sentence.
- It is tested on 8 sentences. Score 0.5 or more is Positive.

## 2. Machine translation (encoder and decoder)
- Dataset: 10 pairs of English sentences and Marathi sentences (Marathi is written in English letters).
- Target sentences get a start token and an end token, like "start mala ai avadte end".
- Decoder input = target tokens without the last token.
- Decoder target = target tokens shifted by one word.
- Encoder block: self attention and feed forward network.
- Decoder block: masked self attention, encoder-decoder attention and feed forward network (with a causal mask).
- Embedding size 32, 2 heads, feed forward 64 units.
- Trained for 300 epochs with batch size 2.
- Translation works word by word: start with "start", predict a word, add it to the decoder input, repeat. It stops at "end".

## 3. Mini GPT (decoder only)
- Dataset: 20 short sentences about AI, machine learning and Transformers.
- Input = previous words, target = next words (shifted by one).
- Example: input "i love artificial", target "love artificial intelligence".
- Two decoder-only blocks with masked self attention (2 heads, feed forward 64 units, embedding size 32).
- The program prints the causal mask. 1 means visible, 0 means hidden.
- Trained for 300 epochs with batch size 2.
- predict_next_word gives one next word. generate_text repeats this to make a longer text. This is called autoregressive generation.

## Key points
- Encoder only: reads the full sentence in both directions. Good for classification.
- Decoder only: masked attention, each word sees only the previous words. Good for text generation.
- Encoder and decoder: the decoder looks at the encoder output through encoder-decoder attention.
- Teacher forcing: during training the correct previous words are given to the decoder.
- Token embedding gives meaning. Position embedding gives word order.
- Softmax over the vocabulary gives the probability of every possible next word.

## Important notes
- The datasets are tiny. The models mostly memorize them.
- In file 01, 3 of the 8 test sentences are also in the training data (course was difficult, teacher explained very well, i am confused).
- In file 02, all 6 test sentences are from the training data. So the result shows learning of the training pairs, not general translation.
- The weights start random, so the output can be different on each run.
- Steps 3 and 4 of file 01 use separate sample layers to show shapes. They are not the trained layers.

## Files
| File | What it does |
|---|---|
| 01_sentiment_classification_encoder_only.py | Encoder only Transformer for sentiment classification |
| 02_machine_translation_encoder_decoder.py | Encoder-decoder Transformer for English to Marathi translation |
| 03_gpt_decoder_only.py | Decoder-only mini GPT for next word prediction and text generation |

## Concepts covered
- TextVectorization
- Embedding and custom TokenAndPositionEmbedding layer
- MultiHeadAttention
- Causal attention mask
- Custom Keras layers for encoder and decoder blocks
- LayerNormalization, Dropout, GlobalAveragePooling1D
- Autoregressive generation

## Requirements
- Python 3
- TensorFlow
- NumPy

## Run
python 01_sentiment_classification_encoder_only.py
python 02_machine_translation_encoder_decoder.py
python 03_gpt_decoder_only.py

Note: files 02 and 03 train for 300 epochs. This can take a few minutes.
