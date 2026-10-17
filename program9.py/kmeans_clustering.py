import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# Input data
X = np.array([
    [1, 2], [2, 3], [3, 2], [3, 4],
    [7, 8], [8, 9], [9, 8], [9, 10]
])

# Create K-Means model
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
kmeans.fit(X)

# Get cluster labels and centroids
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Display output
print("Cluster Labels:", labels)
print("Centroids:\n", centers)

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=100)
plt.scatter(centers[:, 0], centers[:, 1],
            color='red', marker='X', s=200,
            label='Centroids')

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("K-Means Clustering")
plt.legend()
plt.show()