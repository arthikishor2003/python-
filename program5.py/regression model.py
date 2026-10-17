from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Input data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict values
predictions = model.predict(X)
new_value = np.array([[6]])
prediction = model.predict(new_value)

print("Prediction for X = 6:", prediction[0])

# Plot the data
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.scatter(new_value, prediction, color='green', label='Predicted Point')

plt.title("Linear Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()