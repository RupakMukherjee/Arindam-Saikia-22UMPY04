# - Arindam Saikia -

import numpy as np
import matplotlib.pyplot as plt

def DMD(DATA,tr,t_space,SigPlot):
    data_m = np.zeros((10000,t_space-1))
    data_m = DATA[:,:t_space-1]
    data_m_shifted = np.zeros((10000,t_space-1))
    data_m_shifted = DATA [:,1:t_space]
    U, Sig, V = np.linalg.svd(data_m)
    Utr=U[:,:tr]
    Sigtr=np.diag(Sig)
    Sigtr=Sigtr[:tr,:tr]
    Vtr=V[:tr,:]
    U_shifted , Sig_shifted , V_shifted = np.linalg.svd(data_m_shifted)
    Utr_shifted=U_shifted[:,:tr]
    Sigtr_shifted=np.diag(Sig_shifted)
    Sigtr_shifted=Sigtr_shifted[:tr,:tr]
    Vtr_shifted=V_shifted[:tr,:]
    data_m_shifted_tr = Utr_shifted @ Sigtr_shifted @ Vtr_shifted
    Atilde = Utr.conj().T @ data_m_shifted_tr @ Vtr.T @ np.linalg.pinv(Sigtr) 
    eigval_lambda, eigvect_W = np.linalg.eig(Atilde)
    phi = data_m_shifted_tr @ Vtr.T @ np.linalg.pinv(Sigtr) @ eigvect_W
    
     
    if SigPlot == 1 :
        plt.plot(Sig, marker='o', linestyle='-', color='b')
        plt.xlabel('Singular Value Index')
        plt.ylabel('Singular Value Magnitude')
        plt.title('Singular Values of Sigma Matrix from SVD')
        plt.show()
    else :
        pass
    return phi,eigval_lambda,data_m

data = np.loadtxt('D:/CUS/Dissertation/POD and DMD/Drafts/2gauss.dat')

Phi,Lambda,data_m = DMD(data,4,100,0)

num_modes = Phi.shape[1]

for i in range(num_modes):
    plt.subplot(1, num_modes, i+1)
    plt.imshow(np.real(Phi[:, i].reshape((100, 100))), cmap='viridis')
    plt.title(f'Mode {i+1}')

plt.show()

dt = 4*np.pi/100

lambda_diag = np.diag(Lambda)
omega = np.log(lambda_diag)/dt
x1 = data_m[:,0]
b = np.linalg.pinv(Phi) @ x1
mm1 = data_m.shape[1]
time_dynamics = np.zeros((tr,mm1))
tt = np.arange(mm1) * dt

for iter in range(mm1) :
  time_dynamics[:, iter] = (b.reshape(-1, 1) * np.exp(omega * tt[iter]))


Xdmd = Phi @ time_dynamics