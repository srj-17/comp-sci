import numpy as np

print("Backpropagation algorithm (3 Bit: 3x2x1x1) implemented:")

# Define inputs (3-bit data)
x1 = [0, 0, 0, 0, 1, 1, 1, 1]
x2 = [0, 0, 1, 1, 0, 0, 1, 1]
x3 = [0, 1, 0, 1, 0, 1, 0, 1]

# Define target (majority function)
y = [0, 0, 0, 1, 0, 1, 1, 1]

# Initialize weights and biases
w = np.random.randn(9)  # 3 input to first hidden, 
                        # 2 hidden to second hidden, 1 hidden to output
b = np.random.randn(4)  # 3 biases for hidden layers and 1 for output

# Hyperparameters
alpha = 0.5  # Learning rate
mse = 5.0  # Initial MSE
epoch = 0
max_epoch = 20000  # Max number of epochs

# Arrays to store activations and deltas
y4, y5, y6, y7 = [None] * 8, [None] * 8, [None] * 8,[None] * 8
e = [None] * 8  # Errors for each output

# Backpropagation loop
while mse > 0.01 and epoch < max_epoch:
    # Initialize gradients
    dw = np.zeros(9)
    db = np.zeros(4)

    for i in range(8):
        # Forward pass: Compute activations for each layer
        v4 = x1[i]*w[0] + x2[i]*w[1] + x3[i]*w[2] + b[0]
        y4[i] = 1 / (1 + np.exp(-v4))  # Sigmoid activation

        v5 = x1[i]*w[3] + x2[i]*w[4] + x3[i]*w[5] + b[1]
        y5[i] = 1 / (1 + np.exp(-v5))  # Sigmoid activation

        v6 = y4[i]*w[6] + y5[i]*w[7] + b[2]
        y6[i] = 1 / (1 + np.exp(-v6))  # Sigmoid activation

        v7 = y6[i]*w[8] + b[3]
        y7[i] = 1 / (1 + np.exp(-v7))  # Sigmoid activation (final output)

        # Backward pass: Compute gradients and deltas
        delta_7 = y7[i] * (1 - y7[i]) * (y[i] - y7[i])
        delta_6 = y6[i] * (1 - y6[i]) * (delta_7 * w[8])
        delta_4 = y4[i] * (1 - y4[i]) * (delta_6 * w[6])
        delta_5 = y5[i] * (1 - y5[i]) * (delta_6 * w[7])

        # Gradient accumulation
        dw[0] += delta_4 * x1[i]
        dw[1] += delta_4 * x2[i]
        dw[2] += delta_4 * x3[i]
        db[0] += delta_4

        dw[3] += delta_5 * x1[i]
        dw[4] += delta_5 * x2[i]
        dw[5] += delta_5 * x3[i]
        db[1] += delta_5

        dw[6] += delta_6 * y4[i]
        dw[7] += delta_6 * y5[i]
        db[2] += delta_6

        dw[8] += delta_7 * y6[i]
        db[3] += delta_7

        e[i] = (y[i] - y7[i]) ** 2  # Squared error for each output
    
    # Update weights and biases (gradient descent)
    w += alpha * dw
    b += alpha * db

    # Compute mean squared error for this epoch
    mse = np.mean(e)

    epoch += 1
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, MSE = {mse}")

# Print final results
print("\nFinal Result:")
print(f"Number of Epochs = {epoch}")
print(f"MSE = {mse}")
print(f"Final Weights = {w}")
print(f"Final Bias = {b}")
print(f"\nFinal ANN of configuration 3x2x1x1 to achieve majority function:")

print(f"Inputs: x1={x1}")
print(f"        x2={x2}")
print(f"        x3={x3}")
print(f"Target: {y}")
print(f"Output: {[round(val, 4) for val in np.array(y7).tolist()]}")
