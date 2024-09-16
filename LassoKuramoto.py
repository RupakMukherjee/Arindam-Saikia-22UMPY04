# - Arindam Saikia -

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

def get_feature_names(term_order, frequencies):
    feature_names = [f't^{i}' for i in range(term_order)]
    for f in frequencies:
        feature_names.append(f'sin({f} Hz)')
        feature_names.append(f'cos({f} Hz)')
    return feature_names

def pc(x, feature_names):
    plt.figure(figsize=(14, 7))
    bars = plt.bar(range(len(x)), x, color='royalblue')
    plt.xticks(ticks=range(len(x)), labels=feature_names, rotation=45, ha='right')
    plt.xlabel('Feature')
    plt.ylabel('Coefficient Value')
    plt.title('Lasso Regression Coefficients')
    plt.grid(True)
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height, f'{height:.2f}', ha='center', va='bottom', rotation=90)
    plt.show()

def c_diff(x, t):
    dt = t[1] - t[0]
    x_dot = np.zeros(len(x))
    x_dot[0] = (x[1] - x[0]) / dt
    for i in range(1, len(t) - 1):
        x_dot[i] = (x[i + 1] - x[i - 1]) / (2 * dt)
    x_dot[-1] = (x[-1] - x[-2]) / dt
    return x_dot

def create_library_matrix(t, frequencies, term_order):
    library = np.zeros((len(t), term_order + 2 * len(frequencies)))
    for i in range(term_order):
        library[:, i] = t**i
    for i, f in enumerate(frequencies):
        library[:, term_order + 2*i] = np.sin(2 * np.pi * f * t)
        library[:, term_order + 2*i + 1] = np.cos(2 * np.pi * f * t)
    return library

time_scale = 2
div = 1000
t = np.linspace(0, time_scale, div)

x_dot = np.loadtxt(r'D:\CUS\Dissertation\FINAL DISSERTATION THESIS\Report FIles\{Kuramoto Order Parameter}\order_parameters.txt')
rho_dot = x_dot 

plt.plot(rho_dot, label='rho_dot')
plt.legend()
plt.show()

term_order = 6
frequencies = [0.5, 1, 1.5, 2]

A = create_library_matrix(t, frequencies, term_order)
B = x_dot

sparsity_strength = 0.01
lasso = Lasso(alpha=sparsity_strength, max_iter=1000, tol=1e-5)
lasso.fit(A, B)

coeff_final = lasso.coef_
feature_names = get_feature_names(term_order, frequencies)

pc(coeff_final, feature_names)

rho_dot_predict = np.dot(A, coeff_final)
x_predict = np.cumsum(rho_dot_predict) * (t[1] - t[0])
plt.plot(t, rho_dot, label='rho_dot')
plt.plot(t, rho_dot_predict, label='rho_dot_predict')
plt.legend()
plt.show()

mse = mean_squared_error(B, rho_dot_predict)
print(f'Mean Squared Error: {mse:.4f}')
