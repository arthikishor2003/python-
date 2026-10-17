import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input data
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

# Expected output
y = np.array([[0],
              [1],
              [1],
              [0]])

# Initialize weights
np.random.seed(1)
w1 = np.random.rand(2, 4)
w2 = np.random.rand(4, 1)

learning_rate = 0.5

# Training
for epoch in range(20000):

    # Forward propagation
    hidden = sigmoid(np.dot(X, w1))
    output = sigmoid(np.dot(hidden, w2))

    # Calculate error
    error = y - output

    # Backpropagation
    output_delta = error * sigmoid_derivative(output)
    hidden_delta = output_delta.dot(w2.T) * sigmoid_derivative(hidden)

    # Update weights
    w2 += learning_rate * hidden.T.dot(output_delta)
    w1 += learning_rate * X.T.dot(hidden_delta)

# Display output
print("Predicted Output:")
print(np.round(output))

print("\nActual Output:")
print(y)

print("\nResult: Thus, the Deep Learning Network was successfully implemented.")