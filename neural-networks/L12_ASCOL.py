import numpy as np

# Function to compute softmax
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # For numerical stability
    return exp_x / exp_x.sum(axis=0, keepdims=True)

# Function to implement tanh activation
def tanh(x):
    return np.tanh(x)

# Initialize parameters
input_size = 5  # 5 letters in the alphabet (A, S, C, O, L)
hidden_size = 3  # 3 hidden nodes
output_size = 5  # Output is one of the 5 letters (A, S, C, O, L)

# Randomly initialize weights and biases
np.random.seed(42)
W_xh = np.random.randn(hidden_size, input_size)  # input to hidden
W_hh = np.random.randn(hidden_size, hidden_size)  # hidden to hidden
W_hy = np.random.randn(output_size, hidden_size)  # hidden to output
b_h = np.zeros((hidden_size, 1))  # hidden bias
b_y = np.zeros((output_size, 1))  # output bias

# One-hot encoded inputs for each time step (A, S, C, O)
# A = [1, 0, 0, 0, 0], S = [0, 1, 0, 0, 0], 
# C = [0, 0, 1, 0, 0], O = [0, 0, 0, 1, 0]
inputs = [
    np.array([[1], [0], [0], [0], [0]]),  # A
    np.array([[0], [1], [0], [0], [0]]),  # S
    np.array([[0], [0], [1], [0], [0]]),  # C
    np.array([[0], [0], [0], [1], [0]])   # O
]

# Initialize hidden state
h_prev = np.zeros((hidden_size, 1))

# index 1 = A, index 2 = S, etc.
association = ["A", "S", "C", "O", "L"] # for output

# Forward propagation for each input
for t in range(len(inputs)):
    x_t = inputs[t]
    
    # Calculate the hidden state at time step t
    h_t = tanh(np.dot(W_xh, x_t) + np.dot(W_hh, h_prev) + b_h)
    
    # Calculate the output at time step t
    y_t = np.dot(W_hy, h_t) + b_y
    y_t_softmax = softmax(y_t)
    
    # Update previous hidden state
    h_prev = h_t
    
    # Print the results [for looking through every step]
    # print(f"Time Step {t + 1}:")
    # print(f"Input (x_t):\n{x_t.T}")
    # print(f"Hidden State (h_t):\n{h_t.T}")
    # print(f"Output (y_t):\n{y_t.T}")
    # print(f"Softmax Output (Predicted Probability):\n{y_t_softmax.T}")
    # next_guess = association[y_t_softmax.tolist().index(max(y_t_softmax.T[0]))]
    # print(f"Next output (guess):\n {next_guess}")
    # print("-" * 50)

# Print the results
print(f"Output (y_t):\n{y_t.T}")
print(f"Softmax Output (Predicted Probability):\n{y_t_softmax.T}")
next_guess = association[y_t_softmax.tolist().index(max(y_t_softmax.T[0]))]
print(f"Next output (guess):\n {next_guess}")
print("-" * 50)

# The final output is the prediction of 'L' 
# based on the softmax output at the last time step
