import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

# Input data
X = [
    [25, 50, 120],
    [35, 100, 130],
    [45, 140, 150],
    [55, 160, 160],
    [65, 180, 170],
    [30, 95, 125]
]

# Output data
y = [0, 0, 1, 1, 1, 0]

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict heart disease
patient = [[50, 150, 155]]
result = model.predict(patient)

print("Prediction:", result)

# Display result
if result[0] == 1:
    print("Heart Disease")
else:
    print("No Heart Disease")

# Plot the prediction results
status = ["No Disease", "Disease"]
patients = [3, 3]

plt.bar(status, patients, color="orange")
plt.title("Heart Disease Prediction")
plt.xlabel("Result")
plt.ylabel("Patients")
plt.show()