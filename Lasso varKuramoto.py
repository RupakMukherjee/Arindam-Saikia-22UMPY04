# - Arindam Saikia -

import numpy as np
import matplotlib.pyplot as plt
import time

def fft(signal):
    fourier_transform = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal))
   
    #plt.figure(figsize=(10, 6))
    #plt.plot(freqs, np.abs(fourier_transform))
    #plt.xlabel('Frequency (Hz)')
    #plt.ylabel('Magnitude')
    #plt.title('Fourier Transform')
    #plt.grid(True)
    #plt.show()
    
    n = 9
    peak_indices = np.argsort(np.abs(fourier_transform))[::-1][1:n+1]

    dominant_freqs = freqs[peak_indices]

    #print("Dominant frequencies:", dominant_freqs)
    dum = 0
    return dum,dominant_freqs[0],dominant_freqs[1],dominant_freqs[2],dominant_freqs[3],dominant_freqs[4],dominant_freqs[5],dominant_freqs[6],dominant_freqs[7],dominant_freqs[8]
 
def p(x):
    plt.plot(x)
    plt.show()
    
def pc(x):
    plt.plot(x[0:], marker='o', markersize=10, linestyle='--') 
    plt.show()
    
def pr(x):
    print(x)
    
def ps(x):
    print(x.shape)

def normalize_mat(x):
    min_val = np.min(x)
    max_val = np.max(x)
    if max_val - min_val == 0:
        return x
    else:
        return (x - min_val) / (max_val - min_val)

file_path = r'D:\CUS\Dissertation\FINAL DISSERTATION THESIS\Report FIles\{Amp Varied Kuramoto}\order_parameters_var2.txt'

time_scale = 1
div = 1000
t = np.linspace(0, time_scale, div)

normalize = 1

if normalize == 1:
    x0 = np.loadtxt(file_path)
    x = normalize_mat(x0)
else:
    x = np.loadtxt(file_path)

def c_diff(x, t):
    dt = t[1] - t[0]
    x_dot = np.zeros_like(x)
    x_dot[0] = (x[1] - x[0]) / dt
    x_dot[-1] = (x[-1] - x[-2]) / dt
    for i in range(1, len(t) - 1):
        x_dot[i] = (x[i + 1] - x[i - 1]) / (2 * dt)
    return x_dot

def c_int(x_dot,t):
    dt = t[1] - t[0]
    x = np.zeros_like(x_dot)
    for i in range(1, len(x)):
        x[i] = x[i-1] + x_dot[i] * dt
    return x

x_dot = c_diff(x, t)

term_order = 20
library = np.zeros((div, term_order))

library[:, 0] = 1
library[:, 1] = t
library[:, 2] = t ** 2
library[:, 3] = t ** 3
library[:, 4] = t ** 4
library[:, 5] = t ** 5
library[:, 6] = t ** 6
library[:, 7] = t ** 7
library[:, 8] = t ** 8
library[:, 9] = t ** 9
library[:, 10] = t ** 10

do_fft = 'no'

if do_fft == 'yes':
    
    ff , f1, f2, f3 , f4 , f5, f6, f7 ,f8, f9 = fft(x_dot)

    #library[:, 11] = np.sin(2 * np.pi * f1 * t)
    #library[:, 12] = np.sin(2 * np.pi * f5 * t)
    #library[:, 13] = np.sin(2 * np.pi * f6 * t)
    #library[:, 14] = np.sin(2 * np.pi * f5 * t)
    #library[:, 15] = np.sin(2 * np.pi * f7 * t)
    #library[:, 16] = np.sin(2 * np.pi * f8 * t)
    #library[:, 17] = np.sin(2 * np.pi * f9 * t)
    #library[:, 18] = np.sin(2 * np.pi * f8 * t)
    #library[:, 19] = np.sin(2 * np.pi * f9 * t)

    library[:, 11] = np.sin(650 * 2 * np.pi * 0.00805 * t)
    library[:, 12] = 0
    library[:, 13] = 0
    library[:, 14] = 0
    library[:, 15] = 0
    library[:, 16] = 0
    library[:, 17] = 0
    library[:, 18] = 0
    library[:, 19] = 0


else :
    library[:, 11] = t ** 11
    library[:, 12] = t ** 12
    library[:, 13] = t ** 13
    library[:, 14] = t ** 14
    library[:, 15] = t ** 15
    library[:, 16] = np.sin(1.18 * t)
    library[:, 17] = np.sin(10 * t)
    library[:, 18] = np.sin(100 * t)
    library[:, 19] = np.sin(32.8601 * t)

B = x_dot
A = library

max_iter = 5000
sparsity_strength = 0.01 #0.001
learning_rate = 0.01
tolerance = 1e-10
step_positive = 0
step_size = 1e-5

if step_positive == 1:
    infinitesimal_step = step_size
else:
    infinitesimal_step = -step_size

dt = t[1] - t[0]
coeff = np.zeros(term_order)

def Loss(xcoeff):
    Loss_func = np.linalg.norm(np.dot(A, xcoeff) - B) + sparsity_strength * np.sum(np.abs(xcoeff))
    return Loss_func


for i in range(max_iter):
    L = Loss(coeff)
    if L <= tolerance:
        break
    grad = np.zeros_like(coeff)
    for j in range(len(coeff)):
        coeff[j] += infinitesimal_step
        L_forward = Loss(coeff)
        coeff[j] -= 2 * infinitesimal_step
        L_backward = Loss(coeff)
        grad[j] = (L_forward - L_backward) / (2 * infinitesimal_step)
        coeff[j] += infinitesimal_step

    coeff -= learning_rate * grad

    if np.linalg.norm(grad) < tolerance:
        break


coeff_final = coeff

pc(coeff_final)

print("Final Loss:", L)
#print("Final Coefficients:", coeff_final)

x_dot_predict = np.dot(A, coeff_final)
#x_predict = np.cumsum(x_dot_predict) * dt
x_predict = c_int(x_dot_predict,t)
plt.plot(t, x, label='x')
plt.plot(t, x_predict, label='x_predict')

#plt.plot(t, x_dot, label='x_dot')
#plt.plot(t, x_dot_predict, label='x_dot_predict')

plt.legend()
plt.show()