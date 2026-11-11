# 20 Transformer Basics

## About
A Transformer reads all words of a sentence at the same time. It does not read them one by one like an RNN.
These programs show the three basic parts, with every calculation done by hand using NumPy:
1. Self attention
2. Multi head attention
3. Positional encoding

The weights are fixed by hand (identity matrices), so these are learning demos. No model is trained.

## 1. Self attention
Each word looks at every word of the same sentence and collects useful information.

Steps:
1. Each word is a vector. Input X has 3 words (I, love, AI) with 2 values each.
2. Q = X x Wq, K = X x Wk, V = X x Wv
3. Scores = Q x K.T
4. Scaled scores = Scores / sqrt(dk)
5. Softmax on each row gives attention weights. Each row adds up to 1.
6. Output = Attention weights x V

| Term | Meaning |
|---|---|
| Q (Query) | what the word is searching for |
| K (Key) | what the word contains |
| V (Value) | the information the word gives |

Sample result (file 01):
| Word | Attention weights (I, love, AI) | Output |
|---|---|---|
| I | 0.401, 0.198, 0.401 | [0.802, 0.599] |
| love | 0.198, 0.401, 0.401 | [0.599, 0.802] |
| AI | 0.248, 0.248, 0.503 | [0.752, 0.752] |

Each output vector now carries information from all the words. It is context aware.

## 2. Multi head attention
Several attention heads look at the same sentence in different ways. Their outputs are joined together.

- Input X has 3 words with 4 values each.
- Head 1 uses identity weights, so it sees the original features.
- Head 2 uses weights that swap the features in pairs.
- Output of both heads (3 x 4 each) is joined with concatenate. Final shape is 3 x 8.

Note: in this demo both heads give the same attention weights, because the second head only swaps the order of the features. Only the output vectors are different. In real models each head has its own learned weights, so the heads learn different patterns.

## 3. Positional encoding
Attention does not know the word order. Position information is added to each word vector.

Formulas:
- PE(pos, 2i) = sin(pos / 10000^(2i / d_model))
- PE(pos, 2i+1) = cos(pos / 10000^(2i / d_model))
- Final input = Embedding + Positional encoding

Sample result (file 03, 3 words, d_model = 4):
| Position | Positional encoding |
|---|---|
| 0 | [0.0000, 1.0000, 0.0000, 1.0000] |
| 1 | [0.8415, 0.5403, 0.0100, 1.0000] |
| 2 | [0.9093, -0.4161, 0.0200, 0.9998] |

Final input for the word "love" = [0.8, 0.7, 0.9, 0.6] + [0.8415, 0.5403, 0.0100, 1.0000] = [1.6415, 1.2403, 0.9100, 1.6000]

## Key points
- Self attention: every word sees every word.
- Scaling by sqrt(dk) keeps the scores small, so softmax stays stable.
- Softmax turns scores into probabilities. Each row sums to 1.
- Multi head attention gives many views of the same sentence.
- Positional encoding gives the word order, because a Transformer has no recurrence.

## Files
| File | What it does |
|---|---|
| 01_self_attention.py | Self attention step by step: Q, K, V, scores, scaling, softmax, output |
| 02_multi_head_attention.py | Two attention heads with different weights, outputs joined together |
| 03_positional_encoding.py | Calculates sin and cos positional encoding and adds it to the embeddings |

## Concepts covered
- Query, Key, Value
- Scaled dot product attention
- Softmax (row wise)
- Multi head attention and concatenation
- Sinusoidal positional encoding
- np.dot, np.sqrt, np.exp, np.sin, np.cos, np.concatenate

## Requirements
- Python 3
- NumPy

## Run
python 01_self_attention.py
python 02_multi_head_attention.py
python 03_positional_encoding.py
