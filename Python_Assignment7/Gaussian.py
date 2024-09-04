import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
def gaussian_distribution(X, mean, variance):
    std_dev = np.sqrt(variance)
    return norm.pdf(X, mean, std_dev)
X = np.linspace(-10, 10, 1000)
means = [0, 0, 0]
variances = [0.5, 1, 2]
plt.figure(figsize=(10, 6))
for mean, variance in zip(means, variances):
    Y = gaussian_distribution(X, mean, variance)
    plt.plot(X, Y, label=f'Mean={mean}, Variance={variance}')
plt.title('Gaussian Distribution with Varying Mean and Variance')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
