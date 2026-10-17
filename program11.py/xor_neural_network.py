import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output
y = np.array([[0], [1], [1], [0]])

# Initialize weights and biases
np.random.seed(10)
w1 = np.random.randn(2, 3)
b1 = np.zeros((1, 3))
w2 = np.random.randn(3, 1)
b2 = np.zeros((1, 1))

lr = 0.5

# Training
for i in range(20000):
    # Forward propagation
    h = sigmoid(X @ w1 + b1)
    out = sigmoid(h @ w2 + b2)

    # Backpropagation
    d_out = (y - out) * out * (1 - out)
    d_h = (d_out @ w2.T) * h * (1 - h)

    # Update weights and biases
    w2 += lr * (h.T @ d_out)
    b2 += lr * np.sum(d_out, axis=0, keepdims=True)

    w1 += lr * (X.T @ d_h)
    b1 += lr * np.sum(d_h, axis=0, keepdims=True)

# Display results
print("XOR Neural Network Output:")
print(np.round(out, 3))

print("\nFinal Predictions:")
print((out >= 0.5).astype(int))

print("\nResult: XOR implemented successfully!")