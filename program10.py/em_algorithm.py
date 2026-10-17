import numpy as np

def em(data, pi, A, B, max_iters=100):
    data = np.array(data)

    for _ in range(max_iters):
        # E-Step
        gamma = np.zeros((len(data), 2))

        for i, x in enumerate(data):
            gamma[i, 0] = pi * B[0]**x * (1 - B[0])**(1 - x)
            gamma[i, 1] = (1 - pi) * B[1]**x * (1 - B[1])**(1 - x)

            gamma[i] /= gamma[i].sum()

        # M-Step
        pi = gamma[:, 0].mean()

        B[0] = np.sum(gamma[:, 0] * data) / np.sum(gamma[:, 0])
        B[1] = np.sum(gamma[:, 1] * data) / np.sum(gamma[:, 1])

    return pi, A, B


# Input data
data = [1, 0, 1, 1, 0, 1]
pi = 0.5
A = [0.7, 0.6]
B = [0.9, 0.6]

# Run EM algorithm
pi, A, B = em(data, pi, A, B)

# Display output
print("Pi:", pi)
print("A:", A)
print("B:", B)