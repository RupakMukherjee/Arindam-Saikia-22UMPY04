# - Arindam Saikia -

import numpy as np
import matplotlib.pyplot as plt

def eqmap(x, xdot, library):
    model = np.linalg.lstsq(library, xdot, rcond=None)[0]
    return model

def plot(x):
    plt.plot(x)
    plt.show()

def least_squares(x, y):
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x * y)
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept

def lasso_regression(X, y, alpha=1.0, num_iterations=1000, learning_rate=0.01):
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(num_iterations):
        predictions = np.dot(X, theta)
        residuals = y - predictions
        for j in range(n):
            if j == 0:
                theta[j] += learning_rate * np.sum(residuals * X[:, j]) / m
            else:
                theta[j] += learning_rate * (np.sum(residuals * X[:, j]) - alpha * np.sign(theta[j])) / m
    return theta

t = np.linspace(0, 20, 100)
dt = t[1] - t[0]

omega = 10
A = 20
x = A * np.cos(t)
y = A * np.sin(t)
x_dot = 11 * x * y + 5 * y**2

library = np.zeros((len(t), 6))

library[:, 0] = 1
library[:, 1] = x
library[:, 2] = x**2
library[:, 3] = y
library[:, 4] = y**2
library[:, 5] = x * y

coeff = np.zeros((6, 1))

map = np.linalg.lstsq(library, x_dot, rcond=None)[0]

# Define the labels for each library term
labels = ['1', 'x', 'x^2', 'y', 'y^2', 'x*y']

# Plotting the coefficients as a bar graph with labels
plt.bar(range(len(map)), map)
plt.xlabel('Library Term')
plt.ylabel('Coefficient Value')
plt.title('Least Squares Coefficients')
plt.xticks(range(len(map)), labels)
plt.show()
