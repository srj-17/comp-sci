import numpy as np

print("XOR problem using Radial Basis Function (RBF)\n")

# Input and output
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])

# RBF centers and sigma
centers = np.array([
    [0, 0],
    [1, 1]
])
sigma = 1.0

# --- RBF computation ---
# Shape: (samples, centers)
diff = X[:, None, :] - centers[None, :, :]
dist_sq = np.sum(diff**2, axis=2)
phi = np.exp(-dist_sq / (2 * sigma**2))

# Add bias
phi_aug = np.hstack((phi, np.ones((phi.shape[0], 1))))

# Solve weights using least squares
weights, _, _, _ = np.linalg.lstsq(phi_aug, y, rcond=None)

# Predictions
y_pred = phi_aug @ weights

# --- Output ---
print("RBF Hidden Layer Output (Φ):")
print(phi)

print("\nAugmented Φ (with bias):")
print(phi_aug)

print("\nWeights [w1, w2, bias]:")
print(weights.flatten().tolist())

print("\nInput:")
print(X.tolist())

print("\nDesired Output:")
print(y.flatten().tolist())

print("\nPredicted Output:")
print(y_pred.flatten().tolist())

print("\nRounded Output:")
print(np.round(y_pred).flatten().tolist())
