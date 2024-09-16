# - Arindam Saikia -

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the POD modes
file_path = 'D:/CUS/Dissertation/FINAL DISSERTATION THESIS/Report FIles/{Gaussian POD}/podmodes.txt'
df = pd.read_csv(file_path, sep=' ')

# Perform Lasso regression for each column
time_scale = 2
div = 100
t = np.linspace(0, time_scale, div)

# Define the library with sine and Gaussian terms
num_sine_terms = 6
num_gaussian_terms = 6
total_terms = num_sine_terms + num_gaussian_terms

library = np.zeros((div, total_terms))

# Sine terms
for i in range(num_sine_terms):
    library[:, i] = np.sin((i + 1) * np.pi * t)

# Gaussian terms
gaussian_centers = np.linspace(0, time_scale, num_gaussian_terms)
for i, center in enumerate(gaussian_centers):
    library[:, num_sine_terms + i] = np.exp(-((t - center)**2) / (2 * (0.1)**2))

# Labels for the terms
labels = [f'sin({i + 1}πt)' for i in range(num_sine_terms)]
labels += [f'gaussian(center={center:.2f})' for center in gaussian_centers]

scaler = StandardScaler()

for col in df.columns:
    B = df[col].values
    A = library

    # Normalize the data
    A = scaler.fit_transform(A)
    B = scaler.fit_transform(B.reshape(-1, 1)).flatten()

    lasso = Lasso(alpha=0.1)
    lasso.fit(A, B)
    coeffs = lasso.coef_

    # Plot the coefficients
    plt.bar(range(len(coeffs)), coeffs)
    plt.xlabel('Library Term')
    plt.ylabel('Coefficient Value')
    plt.title(f'Lasso Coefficients for {col}')
    plt.xticks(range(len(coeffs)), labels, rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
