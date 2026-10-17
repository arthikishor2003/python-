from sklearn.ensemble import RandomForestClassifier

# Input data: Study hours
X = [[1], [2], [3], [4], [5], [6]]

# Output: 0 = Fail, 1 = Pass
y = [0, 0, 0, 1, 1, 1]

# Create the model
model = RandomForestClassifier(n_estimators=10, random_state=42)

# Train the model
model.fit(X, y)

# Get student study hours
hours = int(input("Enter study hours: "))

# Predict result
prediction = model.predict([[hours]])

# Display result
if prediction[0] == 1:
    print("Student is likely to Pass")
else:
    print("Student is likely to Fail")