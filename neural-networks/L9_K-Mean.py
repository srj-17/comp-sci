import numpy as np

print("K-Mean algorithm implemented:")


d = np.array([[1,1],
              [2,1],
              [4,3],
              [5,4]])
k = 2
c = np.array([[1,1],
              [5,4]])
# K-means implementation (k=2)
max_iter = 100
epoch = 0
prev_labels = None

while True:
    # Assign points to the nearest centroid
    labels = np.zeros(d.shape[0], dtype=int)
    for i in range(d.shape[0]):
        dist0 = np.sqrt((d[i][0] - c[0][0])**2 + (d[i][1] - c[0][1])**2)
        dist1 = np.sqrt((d[i][0] - c[1][0])**2 + (d[i][1] - c[1][1])**2)
        labels[i] = 0 if dist0 <= dist1 else 1

    # If labels did not change, we've converged
    if prev_labels is not None and np.array_equal(labels, prev_labels):
        break

    # Update centroids as mean of assigned points
    # Calculate new centroid 1 (label = 0)
    sum_x1, sum_y1, count1 = 0, 0, 0
    for i in range(4):
        if labels[i] == 0:
            sum_x1 += d[i][0]
            sum_y1 += d[i][1]
            count1 += 1
    if count1 > 0:
        c[0][0] = sum_x1 / count1
        c[0][1] = sum_y1 / count1
    
    # Calculate new centroid 2 (label = 1)
    sum_x2, sum_y2, count2 = 0, 0, 0
    for i in range(4):
        if labels[i] == 1:
            sum_x2 += d[i][0]
            sum_y2 += d[i][1]
            count2 += 1
    if count2 > 0:
        c[1][0] = sum_x2 / count2
        c[1][1] = sum_y2 / count2
    prev_labels = labels.copy()
    epoch += 1
    if epoch >= max_iter:
        print(f"Reached max iterations ({max_iter}).")
        break

# Final output: clusters and centroids
print(f"\nConverged in {epoch} iterations\n")

# Print Cluster 1 (label = 0)
print("Cluster 1:")
for i in range(4):
    if prev_labels[i] == 0:
        print(f"  Point: ({d[i][0]}, {d[i][1]})")
print(f"Centroid 1: ({c[0][0]}, {c[0][1]})")

print()

# Print Cluster 2 (label = 1)
print("Cluster 2:")
for i in range(4):
    if prev_labels[i] == 1:
        print(f"  Point: ({d[i][0]}, {d[i][1]})")
print(f"Centroid 2: ({c[1][0]}, {c[1][1]})")
