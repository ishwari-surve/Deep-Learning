# 21 Transformer Encoder and Decoder

## About
A Transformer has two main blocks:
1. Encoder: reads the input sentence and understands it.
2. Decoder: uses that understanding to generate the output sentence.

These programs build one encoder block and one decoder block by hand using NumPy.
The weights are fixed by hand, so these are learning demos. No model is trained.

## Encoder (file 01)
Input sentence: "I love AI" (3 words, 4 values each).

Steps:
1. Input embeddings.
2. Add positional encoding.
3. Self attention (Q, K, V, scores, scaling, softmax, output).
4. Add and Layer Normalization. The attention output is added to the input, then normalized.
5. Feed Forward Network: Dense layer, ReLU, Dense layer.
6. Add and Layer Normalization again.
7. Encoder output: one context aware vector for each word.

Layer normalization formula: (x - mean) / (std + 1e-6), calculated for each word.

Result of file 01:
| Word | Encoder output |
|---|---|
| I | [0.488, -0.697, -1.171, 1.380] |
| love | [-0.269, 0.398, -1.436, 1.307] |
| AI | [0.804, -1.193, -0.769, 1.158] |

## Decoder (file 02)
The decoder works on the target sentence "मला AI आवडतो" (Marathi for "I love AI").

Steps:
1. Encoder output (given as fixed example values).
2. Decoder input embeddings of the words generated so far.
3. Add positional encoding.
4. Masked self attention. A word cannot see the future words.
5. Add and Layer Normalization.
6. Encoder-decoder attention. Q comes from the decoder. K and V come from the encoder.
7. Add and Layer Normalization.
8. Feed Forward Network.
9. Add and Layer Normalization.
10. Linear layer and softmax over the vocabulary. This gives a probability for every possible next word.

Masked attention weights in file 02 (rows = words, columns = words seen):
| Word | Weights |
|---|---|
| 1st word | 1.000, 0, 0 |
| 2nd word | 0.411, 0.589, 0 |
| 3rd word | 0.345, 0.213, 0.442 |

The 1st word can see only itself. The 2nd word sees the 1st and itself. The 3rd word sees all three.

## Important notes
- The encoder output used in file 02 is a fixed set of example values. It is not the output of file 01.
- The weights are not trained. So the words predicted in file 02 do not make a correct sentence (it prints AI, AI, मला). The aim is to understand the flow of calculation, not the prediction.

## Key points
- Encoder: self attention to understand the input, then feed forward.
- Decoder: masked self attention, then encoder-decoder attention, then feed forward.
- The mask hides future words so the decoder cannot cheat while generating text.
- Add and Layer Normalization (residual connection) is used after every sub layer.
- In encoder-decoder attention, Q is from the decoder, K and V are from the encoder.
- The final linear layer and softmax choose the next word.

## Files
| File | What it does |
|---|---|
| 01_encoder.py | One Transformer encoder block with every step printed |
| 02_decoder.py | One Transformer decoder block with masked attention, encoder-decoder attention and word prediction |

## Concepts covered
- Positional encoding
- Self attention and masked self attention
- Encoder-decoder (cross) attention
- Residual connection and layer normalization
- Feed forward network with ReLU
- Linear layer and softmax for word prediction
- np.triu for the mask matrix

## Requirements
- Python 3
- NumPy

## Run
-python 01_encoder.py
-python 02_decoder.py
