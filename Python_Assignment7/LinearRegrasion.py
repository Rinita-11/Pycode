import numpy as np
import matplotlib.pyplot as plt
def linear_regression(X, Y):
    n = len(X)
    mean_X, mean_Y = np.mean(X), np.mean(Y)
    numerator = np.sum((X - mean_X) * (Y - mean_Y))
    denominator = np.sum((X - mean_X) ** 2)
    m = numerator / denominator
    c = mean_Y - m * mean_X   
    return m, c
def predict(X, m, c):
    return m * X + c
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
Y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10])
m, c = linear_regression(X, Y)
print(f"Slope (m): {m}")
print(f"Intercept (c): {c}")
Y_pred = predict(X, m, c)
plt.scatter(X, Y, color="blue", label="Original Data")
plt.plot(X, Y_pred, color="red", label="Fitted Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()
