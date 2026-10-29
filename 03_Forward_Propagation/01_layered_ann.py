
# ---------------------------------------------------------
# Program : Artificial Neural Network Forward Propagation
# Author  : Ishwari Vijaykumar Surve
#
# Network Structure:
#   Input Layer   : 2 inputs
#   Hidden Layer  : 2 neurons with ReLU activation
#   Output Layer  : 1 neuron with Sigmoid activation
# ---------------------------------------------------------

import math


# ---------------------------------------------------------
# Function Name : relu
# Description   : Applies ReLU activation function
# Formula       : ReLU(x) = max(0, x)
# Use           : Commonly used in hidden layers
# ---------------------------------------------------------
def relu(value):
    return max(0, value)


# ---------------------------------------------------------
# Function Name : sigmoid
# Description   : Applies Sigmoid activation function
# Formula       : 1 / (1 + e^(-x))
# Use           : Commonly used in output layer for
#                 binary classification
# Output Range  : (0, 1)
# ---------------------------------------------------------
def sigmoid(value):
    return 1 / (1 + math.exp(-value))


# ---------------------------------------------------------
# Function Name : calculate_weighted_sum
# Description   : Calculates weighted sum of inputs
# Formula       : z = (x1*w1 + x2*w2 + ... + xn*wn) + b
# Parameters    :
#   inputs  -> List of input values
#   weights -> List of weights
#   bias    -> Bias value
# Returns       : Weighted sum
# ---------------------------------------------------------
def calculate_weighted_sum(inputs, weights, bias):
    weighted_sum = sum(
        weight * input_value
        for weight, input_value in zip(weights, inputs)
    ) + bias

    return weighted_sum


# ---------------------------------------------------------
# Function Name : display_multiplication_details
# Description   : Displays step-by-step multiplication of
#                 inputs and weights for one neuron
# Parameters    :
#   inputs  -> List of inputs
#   weights -> List of weights
# ---------------------------------------------------------
def display_multiplication_details(inputs, weights):
    print("  Step 1: Multiply inputs by corresponding weights")

    for index in range(len(inputs)):
        print(
            f"    ({weights[index]} * {inputs[index]}) = "
            f"{weights[index] * inputs[index]:.3f}"
        )


# ---------------------------------------------------------
# Function Name : process_hidden_layer
# Description   : Processes all neurons of hidden layer
#                 using ReLU activation function
# Parameters    :
#   inputs         -> Input values from input layer
#   hidden_weights -> Weight matrix for hidden layer
#   hidden_biases  -> Bias list for hidden neurons
# Returns          : List of hidden layer outputs
# ---------------------------------------------------------
def process_hidden_layer(inputs, hidden_weights, hidden_biases):
    hidden_outputs = []

    print("\n================ HIDDEN LAYER ================\n")

    for neuron_index in range(len(hidden_weights)):
        print(f"Hidden Neuron {neuron_index + 1}:")

        current_weights = hidden_weights[neuron_index]
        current_bias = hidden_biases[neuron_index]

        # Display multiplication details
        display_multiplication_details(inputs, current_weights)

        # Calculate weighted sum
        z_value = calculate_weighted_sum(
            inputs,
            current_weights,
            current_bias
        )

        print(
            f"  Step 2: Add all multiplication results "
            f"and bias {current_bias}"
        )
        print(f"    z = {z_value:.3f}")

        # Apply ReLU activation
        activated_output = relu(z_value)

        print("  Step 3: Apply ReLU activation")
        print(
            f"    ReLU({z_value:.3f}) = "
            f"{activated_output:.3f}\n"
        )

        hidden_outputs.append(activated_output)

    return hidden_outputs


# ---------------------------------------------------------
# Function Name : process_output_layer
# Description   : Processes output layer neuron using
#                 Sigmoid activation function
# Parameters    :
#   hidden_outputs -> Outputs from hidden layer
#   output_weights -> Weights of output neuron
#   output_bias    -> Bias of output neuron
# Returns          : Final weighted sum and final output
# ---------------------------------------------------------
def process_output_layer(hidden_outputs, output_weights, output_bias):
    print("\n================ OUTPUT LAYER ================\n")

    print("Output Neuron:")
    print("  Step 1: Multiply hidden layer outputs by output weights")

    for index in range(len(hidden_outputs)):
        print(
            f"    ({output_weights[index]} * "
            f"{hidden_outputs[index]:.3f}) = "
            f"{output_weights[index] * hidden_outputs[index]:.3f}"
        )

    # Calculate weighted sum for output layer
    z_output = calculate_weighted_sum(
        hidden_outputs,
        output_weights,
        output_bias
    )

    print(
        f"  Step 2: Add all multiplication results "
        f"and bias {output_bias}"
    )
    print(f"    z = {z_output:.3f}")

    # Apply Sigmoid activation
    final_output = sigmoid(z_output)

    print("  Step 3: Apply Sigmoid activation")
    print(
        f"    Sigmoid({z_output:.3f}) = "
        f"{final_output:.3f}"
    )

    return z_output, final_output


# ---------------------------------------------------------
# Function Name : display_network_summary
# Description   : Displays final outputs of network
# Parameters    :
#   hidden_outputs -> Hidden layer outputs
#   final_output   -> Output layer final value
# ---------------------------------------------------------
def display_network_summary(hidden_outputs, final_output):
    print("\n================ FINAL SUMMARY ================\n")

    print(f"Hidden Layer Outputs : {hidden_outputs}")
    print(f"Final Network Output : {final_output:.3f}")
    print(f"Output Percentage    : {final_output * 100:.2f}%")

    if final_output >= 0.5:
        print("Prediction           : Positive Class")
    else:
        print("Prediction           : Negative Class")


# ---------------------------------------------------------
# Function Name : ann_forward_pass
# Description   : Complete forward pass of ANN
# Parameters    :
#   inputs -> List of input values
# Flow          :
#   Input Layer -> Hidden Layer -> Output Layer
# ---------------------------------------------------------
def ann_forward_pass(inputs):
    print("================ INPUT LAYER ================\n")

    print(f"Input x1 = {inputs[0]}")
    print(f"Input x2 = {inputs[1]}")

    # -----------------------------------------------------
    # Hidden layer weights and biases
    # Two neurons in hidden layer
    # -----------------------------------------------------
    hidden_weights = [
        [0.5, -0.2],   # Weights for hidden neuron 1
        [0.8, 0.4]     # Weights for hidden neuron 2
    ]

    hidden_biases = [
        0.1,   # Bias for hidden neuron 1
        -0.1   # Bias for hidden neuron 2
    ]

    # -----------------------------------------------------
    # Output layer weights and bias
    # One neuron in output layer
    # -----------------------------------------------------
    output_weights = [1.0, -1.5]
    output_bias = 0.2

    # Process hidden layer
    hidden_outputs = process_hidden_layer(
        inputs,
        hidden_weights,
        hidden_biases
    )

    # Process output layer
    z_output, final_output = process_output_layer(
        hidden_outputs,
        output_weights,
        output_bias
    )

    # Display summary
    display_network_summary(hidden_outputs, final_output)


# ---------------------------------------------------------
# Function Name : main
# Description   : Entry point of program
# ---------------------------------------------------------
def main():
    # Example input values
    # Change these values to test different outputs
    inputs = [2.0, 3.0]

    # Start ANN forward pass
    ann_forward_pass(inputs)


if __name__ == "__main__":
    main()
