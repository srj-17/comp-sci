'''Write a Python program to implement Learning
 Vector Quantization (LVQ) for the dataset (1,1) → 0,(2,1)
 → 0,(4,3) → 1,(5,4) → 1, update prototypes for 5 itera
tions, and classify the dataset'''

import numpy as np

print("LVQ classification algorithm implemented:")

x = np.array([[1,1],
              [2,1],
              [4,3],
              [5,4]])
true_class = [0,0,1,1]
w = np.array([[1.0,1.0], # Class 0 weight assumption
              [4.0,3.0]])  # Class 1 weight assumption
learning_rate = 0.3
epoch = 5
D = np.full((1,2),None)


for e in range(epoch):
    for i in range(4):
        # Calculate distances to both prototypes
        for j in range(2):
            D[0][j] = np.sqrt((x[i][0]-w[j][0])**2+(x[i][1]-w[j][1])**2)
        winner_index = np.argmin(D)
        
        # LVQ update rule: attract if correct class, repel if wrong class
        if winner_index == true_class[i]:
            # Correct classification: move prototype closer
            w[winner_index] = w[winner_index] + learning_rate * (x[i] - w[winner_index])
        else:
            # Wrong classification: move prototype away
            w[winner_index] = w[winner_index] - learning_rate * (x[i] - w[winner_index])

print(f"\nFinal Prototypes after {epoch} iterations:")
print(f"  Class 0 prototype (w0) = {w[0]}")
print(f"  Class 1 prototype (w1) = {w[1]}")

print("\n=== Classification Results ===")
for i in range(4):
    # Calculate distances to both prototypes
    for j in range(2):
        D[0][j] = np.sqrt((x[i][0]-w[j][0])**2+(x[i][1]-w[j][1])**2)
    winner_index = np.argmin(D)
    
    if true_class[i] == winner_index:
        print(f"Input {x[i]} -> Predicted Class: {winner_index}, True Class: {true_class[i]} (Correct)")
    else:
        print(f"Input {x[i]} -> Predicted Class: {winner_index}, True Class: {true_class[i]} (Incorrect)")
        
