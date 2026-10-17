from sklearn.ensemble import RandomForestClassifier

# Input data: Age and Income
X = [
    [22, 20000],
    [25, 25000],
    [35, 50000],
    [40, 60000],
    [50, 80000],
    [55, 90000]
]

# Output labels
y = [0, 0, 1, 1, 1, 1]

# Create the model
model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)

# Train the model
model.fit(X, y)

# Get customer details
age = int(input("Enter customer age: "))
income = int(input("Enter customer income: "))

# Predict
prediction = model.predict([[age, income]])

if prediction[0] == 1:
    print("Customer is likely to buy the product")
else:
    print("Customer is unlikely to buy the product")