# Project Title: **Methods for Extracting Governing Equations and Dominant Patterns from Data** 

By **_Arindam Saikia_**
_Msc Physics Project_

Welcome! This project focuses on methods to extract governing equations and dominant patterns from data, applying techniques such as **Lasso Regression**, **Linear Regression**, **POD (Proper Orthogonal Decomposition)**, and **DMD (Dynamic Mode Decomposition)**.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Project Objectives](#project-objectives)
3. [Methodology](#methodology)
4. [Results](#results)
5. [Contact Information](#contact-information)

---

## Introduction

This project aims to apply data-driven algorithms to various sets of data and obtain very close approximations to the underlying governing equations that generate the data. In addition, assistance in conditioning the data properly, for feeding into the algorithm as well as reducing the dimensionality, has been utilized by incorporating decomposition methods like POD and DMD.

---

## Project Objectives

- Employ **linear regression** techniques to approximate governing equations for **simple dynamical systems**, establishing a baseline for comparison with more advanced methods.
- Use **Lasso Regression** in order to promote **sparsity** in the predicted model.
- Apply **decomposition methods** (POD and DMD) to extract **dominant modes** from the data and analyze the terms involved in generating these dominant modes.
- Achieve **noise reduction** through the decomposition algorithms.
  
---

## Methodology

The methodology includes the following key steps:

1. **Data Preparation**: Preparing datasets and formatting them into matrices. Datasets used - Equation with Linear terms, Equation with Non-linear terms, Kuramoto Model Order Parameter, and Gaussian + Sine profile with Noise data.
2. **Library Construction**: Constructing a library of basis functions for the regression model.
3. **Data Normalization**: Ensuring that all terms are on a comparable scale.
4. **Regression & Decomposition**: Performing the regression and decomposition algorithms on the given dataset.
5. **Coefficient Analysis and Visualization**: Visualizing the coefficients of the terms involved in the predicted model, extracted patterns from the modes, etc.

---

## Results

- Problem 1 : **u = 11x + 5y** data

![Surface Plot of the Equation.](image1.png)  
*Surface Plot of the Equation.*

![Scatter plot of the data points and the fitted regression line.](image2.png)  
*Scatter plot of the data points and the fitted regression line.*

- Problem 2 : **u = 11xy + 5y^2** data

![Surface Plot of the Equation.](image3.png)  
*Surface Plot of the Equation.*

![Plot of the data points and the fitted regression surface.](image4.png)  
*Plot of the data points and the fitted regression surface.*

- Problem 3 : **Phase Coupled Kuramoto Model's Order Parameter**

![Order Parameter trend.](image5.png)  
*Order Parameter trend.*

![Kuramoto order parameter over time.](image6.png)  
*Kuramoto order parameter over time.*

![Weightage of terms obtained from Lasso Regression.](image7.png)  
*Weightage of terms obtained from Lasso Regression.*

![Reconstruction of Data from obtained terms.](image8.png)  
*Reconstruction of Data from obtained terms.*

- Problem 4 : **Amplitude-Variated Phase Coupled Kuramoto Model’s Order Parameter**

![Order parameter trend.](image9.png)  
*Order parameter trend.*

![Sparsity Parameter comparison on terms(i)](image10a.png)  
*Sparsity Parameter comparison on terms(i)*

![Sparsity Parameter comparison on terms(ii)](image10b.png)  
*Sparsity Parameter comparison on terms(ii)*

![Sparsity Parameter comparison on model(i)](image11a.png)  
*Sparsity Parameter comparison on model(i)*

![Sparsity Parameter comparison on model(ii)](image11b.png)  
*Sparsity Parameter comparison on model(ii)*

- Problem 5 : **Gaussian + Sine profile with Noise data**

![Output Plots for t=0](image12.png)  
*Output Plots for t=0*

![Output Plots for t=0.5](image13.png)  
*Output Plots for t=0.5*

![Output Plots for t=1](image14.png)  
*Output Plots for t=1*

![Output Plots for t=1.5](image15.png)  
*Output Plots for t=1.5*

![Output Plots for t=2](image16.png)  
*Output Plots for t=2*

![Reconstructed plot demonstrating the removal of noise in the data.](image17.png)  
*Reconstructed plot demonstrating the removal of noise in the data.*

![Reconstructed plot demonstrating the removal of noise in the data.](image18.png)  
*Reconstructed plot demonstrating the removal of noise in the data.*

---

## Other Links

**Full Project Report** : [PDF](report.pdf)  
**Source Codes** : [Linear Regression-linear](lstlinear.py), [Linear Regression-nonlinear](lstlinear2.py), [Lasso Regression-standard kuramoto](LassoKuramoto.py), [Lasso Regression-varied kuramoto](LassovarKuramoto.py), [POD1](podmodes.py), [POD2](podmodesL1.py)

Email: arindamsaikia16@gmail.com
