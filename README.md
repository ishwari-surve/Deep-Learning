# Deep Learning

Concept-wise Deep Learning programs in Python. They go from a single neuron
to Transformers. Each folder covers one concept, with small programs that
are numbered in learning order. Every folder has its own README.

## What you will find
- Neural network basics: neuron, activation functions, forward propagation
- Training: loss functions, gradient descent, backpropagation
- Feedforward networks with scikit-learn and Keras
- Images and CNN: pixels, convolution, edge detection, CNN layers, real-time classification
- TensorFlow basics
- RNN for text: tokenization, embedding, hidden state, sentiment analysis
- Transformers: attention, encoder, decoder, mini GPT, translation

Many programs are written by hand with plain Python and NumPy, so every
calculation can be seen step by step. Later programs use TensorFlow and Keras.

## Repository structure

| Folder | Topic | Programs |
|---|---|---|
| 01_Single_Neuron | One neuron with weights, bias and ReLU | 1 |
| 02_Activation_Functions | ReLU, Sigmoid and their comparison | 3 |
| 03_Forward_Propagation | Forward pass of a 2-2-1 network | 3 |
| 04_Single_Neuron_Training | Error, loss and weight update | 2 |
| 05_Multi_Neuron_Training | Training a small network, with graphs and animation | 3 |
| 06_Loss_Functions | MSE, MAE, Binary Cross Entropy | 3 |
| 07_Backpropagation | Gradient and backpropagation using the chain rule | 2 |
| 08_Feedforward_Neural_Network | FNN with scikit-learn (regression, classification, placement prediction) | 4 |
| 09_Image_Basics | Images as pixel values (grayscale and colour) | 3 |
| 10_CNN_Edge_Detection | Convolution, kernels, feature map, Canny edges | 4 |
| 11_Realtime_Image_Classification | Webcam classification with a pre-trained MobileNetV2 | 1 |
| 12_TensorFlow_Basics | Tensors, operations, variables, matmul, single neuron | 7 |
| 13_Keras_Neural_Networks | First Keras models, Fashion MNIST | 3 |
| 14_CNN_Layers | Convolution, ReLU, pooling, flatten, fully connected layer | 4 |
| 15_RNN_Text_Preprocessing | Tokenizer, vocabulary, sequences, padding | 9 |
| 16_RNN_Embedding_and_Hidden_State | Embedding, time steps, hidden state | 5 |
| 17_RNN_Activation_and_Loss | tanh, sigmoid, binary cross entropy | 3 |
| 18_RNN_Sentiment_Model | Complete RNN sentiment model in Keras | 5 |
| 19_RNN_Applications | Next character, sentiment and sequence prediction | 3 |
| 20_Transformer_Basics | Self attention, multi head attention, positional encoding | 3 |
| 21_Transformer_Encoder_Decoder | Encoder block and decoder block | 2 |
| 22_Transformer_Applications | Sentiment (encoder), translation (encoder-decoder), mini GPT (decoder) | 3 |

Total: 22 folders and 76 programs.

## Suggested learning order
1. Folders 01 to 07: how a neuron works and how a network learns.
2. Folders 08 and 12 to 13: first models with scikit-learn and Keras.
3. Folders 09 to 11 and 14: images and CNN.
4. Folders 15 to 19: text and RNN.
5. Folders 20 to 22: Transformers.

## Tech stack
Python, NumPy, Matplotlib, Pandas, scikit-learn, TensorFlow, Keras, OpenCV, Pillow, joblib

## Setup
1. Install Python 3.9 or newer. Use a version that your TensorFlow supports.
2. Install the libraries:

pip install numpy matplotlib pandas scikit-learn joblib pillow opencv-python tensorflow

3. Open a folder and run a program:

cd 03_Forward_Propagation
python 01_layered_ann.py

You only need the libraries for the folder you are using. For example,
folders 01 to 07 need only NumPy and Matplotlib.

## Important notes
- These are learning programs. The datasets are very small, and some programs
  use fixed weights, so the aim is to understand the steps, not to get the best accuracy.
- Some programs open many graph windows. Close each window to see the next step.
- Some programs need extra files that are kept in the same folder
  (placement_data.csv, sample images).
- Folder 11 needs a webcam and internet on the first run (model download).
- Programs using Keras datasets (Fashion MNIST) download data on the first run.
- Results of trained models can be slightly different on each run.
- Some Marathi words are used in a translation example. Save and open files with UTF-8.

## Related repositories
- Generative-AI: Streamlit basics and AI agents
- Projects (CNN, LSTM and others): separate repositories

## Author
Ishwari Vijaykumar Surve
