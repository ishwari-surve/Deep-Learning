# 07 Backpropagation

## About
Backpropagation finds how much each weight caused the error. Gradient descent then corrects the weights.

## Network
Single neuron with Sigmoid. Inputs = (1, 2), target = 1, learning rate = 0.1.

## Steps in each epoch
1. Forward: z = x1*w1 + x2*w2 + b, output = sigmoid(z)
2. Loss: 0.5 * (target - output)^2
3. Backward (chain rule): dL/dz = (output - target) * output * (1 - output)
4. Gradients: dL/dw1 = dL/dz * x1, dL/dw2 = dL/dz * x2, dL/db = dL/dz
5. Update: weight = weight - (learning_rate * gradient)

## Files
| File | What it does |
|---|---|
| 01_gradient_backpropagation.py | Training for 10 epochs with printed values |
| 02_gradient_backpropagation_animation.py | Training for 20 epochs, plus animation of the neuron |

## Requirements
- Python 3
- Matplotlib

## Run
python 01_gradient_backpropagation.py
