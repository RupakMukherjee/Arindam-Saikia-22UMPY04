# - ARINDAM SAIKIA -

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

pi= 3.14159265358979323846
t_space = np.linspace (0,4*np.pi,100) 
time_int = 20 # set the time column here
dt = t_space[1] - t_space[0]
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
data_array = ([])

load = np.loadtxt('D:/CUS/Dissertation/POD and DMD/Drafts/2gauss.dat')
col = np.zeros((10000, 1))
col[:,0] = load[:,time_int]
z = np.zeros((len(x), 1))
z = col.reshape(100, 100)

U, Sig, V = np.linalg.svd(z)

# Plot singular values
plt.plot(Sig[:25], marker='o', linestyle='-', color='b')
plt.xlabel('Singular Value Index')
plt.ylabel('Singular Value Magnitude')
plt.title('Singular Values of Sigma Matrix from SVD')
plt.show()

tr = 4

Utr = U[:, :tr]
Sigtr = Sig[:tr]
Vtr = V[:tr, :]

# Plot modes
fig2, axs = plt.subplots(nrows=1, ncols=tr, figsize=(15, 5))
for i in range(tr):
    axs[i].plot(Utr[:, i])
    axs[i].set_title(f'POD Mode {i+1}')
    axs[i].set_xlabel('Index')
    axs[i].set_ylabel(f'U[:, {i}]')
plt.tight_layout()
plt.show()

# Save modes to file
#save_path = 'D:/CUS/Dissertation/FINAL DISSERTATION THESIS/Report FIles/{Gaussian POD}/podmodes.txt'
#df = pd.DataFrame(Utr, columns=[f'Mode_{i+1}' for i in range(tr)])
#df.to_csv(save_path, index=False, sep=' ')

datapod = Utr @ np.diag(Sigtr) @ Vtr