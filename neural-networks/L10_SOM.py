import numpy as np

print("SOM (2×2) clustering algorithm implemented:")

# Input data
x = np.array([[0.1, 0.8],
              [0.5, 0.4],
              [0.3, 0.7],
              [0.9, 0.2]])

# Initial weight vectors for neurons
w = np.array([[0.2, 0.6],
              [0.8, 0.2],
              [0.6, 0.7],
              [0.3, 0.3]])

# 2D grid coordinates of neurons
y = np.array([[0, 0],  # Neuron 1
              [0, 1],  # Neuron 2
              [1, 0],  # Neuron 3
              [1, 1]]) # Neuron 4

# SOM parameters
time_constant = 9.5
initial_nh_w = 1.0
alpha = 0.5
epochs = 5

# Arrays to store distances, neighbourhood function, and clustering info
D = np.zeros(4)  # To store distances from input to all neurons
d = np.zeros(4)  # To store distances between neurons
h = np.zeros(4)  # Neighbourhood function values
cluster = np.zeros(4, dtype=int)  # To store which neuron is the winner for each input

# Training loop for 5 epochs
for e in range(epochs):
    print(f"\nEpoch {e + 1}/{epochs}")
    
    # For each input, find the winning neuron and update weights
    for i in range(4):
        # Find distances from input x[i] to all neurons
        for j in range(4):
            D[j] = np.linalg.norm(x[i] - w[j])  # Euclidean distance between x[i] and w[j]
        
        # Winner neuron is the one with the minimum distance
        winner_index = np.argmin(D)
        cluster[i] = winner_index

        # Update all neurons based on distance from winner
        for k in range(4):
            # Distance from winner neuron to neuron k in the grid
            d[k] = np.linalg.norm(y[winner_index] - y[k])  # Euclidean distance between neurons
            
            # Calculate the neighbourhood width based on the current epoch
            nh_w = initial_nh_w * np.exp(-e / time_constant)
            
            # Calculate the neighbourhood function
            h[k] = np.exp(-(d[k]**2) / (2 * nh_w**2))
            
            # Update weight of neuron k towards the current input x[i]
            w[k] = w[k] + alpha * h[k] * (x[i] - w[k])

# Output the final clustering results
print("\n=== Final Clustering Results After 5 iterations ===")
for i in range(4):
    winner = cluster[i]
    print(f"Dataset {i+1} = {x[i]} -> Output Neuron = {winner+1}")
    print(f"  Winner's Final Weights = {w[winner]}")

# Output all final weights of the neurons
print("\n=== All Final Weights ===")
for i in range(4):
    print(f"w{i+1} = {w[i]}")
