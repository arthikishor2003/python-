class SVM:
    def __init__(self, lr=0.001, ni=1000):
        self.lr = lr
        self.ni = ni
        self.w = [0, 0]
        self.b = 0

    def fit(self, X, y):
        for _ in range(self.ni):
            for i in range(len(X)):
                x = X[i]

                if y[i] * (sum(a * b for a, b in zip(x, self.w)) + self.b) < 1:
                    self.w = [
                        w + self.lr * y[i] * xj
                        for w, xj in zip(self.w, x)
                    ]
                    self.b += self.lr * y[i]

    def predict(self, X):
        predictions = []
        for x in X:
            result = sum(a * b for a, b in zip(x, self.w)) + self.b
            predictions.append(1 if result >= 0 else -1)
        return predictions


# Input data
X = [[1, 2], [2, 3], [3, 4], [4, 5]]
y = [1, 1, -1, -1]

# Create and train the model
svm = SVM()
svm.fit(X, y)

# Predict the output
print("Prediction:", svm.predict(X))