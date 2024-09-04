import numpy as np
import matplotlib.pyplot as plt
def compute_cost(X, Y, m, c):
    n = len(Y)
    predictions = m * X + c
    cost = (1 / (2 * n)) * np.sum((predictions - Y) ** 2)
    return cost
def gradient_descent(X, Y, m, c, learning_rate, epochs):
    n = len(Y)
    cost_history = []
    for _ in range(epochs):
        predictions = m * X + c
        m_gradient = -(2 / n) * np.sum(X * (Y - predictions))
        c_gradient = -(2 / n) * np.sum(Y - predictions)
        m = m - learning_rate * m_gradient
        c = c - learning_rate * c_gradient
        cost = compute_cost(X, Y, m, c)
        cost_history.append(cost)
    return m, c, cost_history
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10])
m = 0
c = 0
learning_rate = 0.01
epochs = 1000
m, c, cost_history = gradient_descent(X, Y, m, c, learning_rate, epochs)
print(f"Optimized Slope (m): {m}")
print(f"Optimized Intercept (c): {c}")
plt.figure(figsize=(8, 6))
plt.plot(range(epochs), cost_history, color="blue")
plt.title("Cost Function History")
plt.xlabel("Epochs")
plt.ylabel("Cost")
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 6))
plt.scatter(X, Y, color="blue", label="Original Data")
plt.plot(X, m * X + c, color="red", label="Fitted Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression with Gradient Descent")
plt.legend()
plt.grid(True)
plt.show()
