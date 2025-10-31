# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 07:38:25 2024

@author: Khalid
"""

import numpy as np
import matplotlib.pyplot as plt
import torch
from scipy.constants import Stefan_Boltzmann
def blackbody_emissive_power(c_o,n,k,T,h,lambd):
    E_b_lambd=2*np.pi *h * c_o**2/ (np.exp(h*c_o/(n*lambd*k*T*1e-6))-1) *1/(n**2 *(lambd*1e-6)**4 *lambd)
    return E_b_lambd

def emissive_power(n,T):
    E_b=n**2 * Stefan_Boltzmann*T**4
    return E_b
    

c_o=3e8 #m/s
n=1
k=1.3807e-23 # J/K
T=np.array([300,500,1000,5777])#K
h=6.626e-34 #J.s
npoints=100
lambd=np.logspace(-2, 2,npoints)#micrometer

E_b=torch.zeros(T.size,1,npoints)

for i in range(T.size):
    E_b[i,0,:]=torch.from_numpy(blackbody_emissive_power(c_o,n,k,T[i],h,lambd))

plt.figure(dpi=600)
for i in range(T.size):
    plt.loglog(lambd,E_b[i,0,:],label=f'{T[i]} K')

plt.xlim([0.5e-1, 1e2])
plt.ylim([1e1, 1e8])
plt.ylabel("Blackbody emissive power (W/m² µm)")
plt.xlabel("Wavelength (µm)")


plt.fill_between(lambd, E_b.min(), E_b.max(), where=(lambd > 0.4) & (lambd < 0.7), color='gray', alpha=0.5)

#plt.text(0.3,1e5,"Visible part of spectrum"rotation=90)
plt.text(0.5, 1e5, "Visible part of spectrum",
         rotation=90,
         color='black',
         fontsize=10,
         ha='center',
         va='center')
#%%
T=np.array([100,300,500,1000,5777])#K
lambda_max=2898/T 
Eb_max=torch.zeros(T.size,1,1)

for i in range(T.size):
    Eb_max[i,0,0]=(blackbody_emissive_power(c_o,n,k,T[i],h,lambda_max[i]))

plt.plot(lambda_max,Eb_max[:,0,0],'o')
plt.plot(lambda_max,Eb_max[:,0,0],'k--',label="Wien's law")
plt.legend()
plt.show()

#%% Evaluate spectral blackbody emissive power
T_eval=2000
lambda_at_2000K=2898/T_eval
Spectral_blackbody_emissive_power_at_2000K=blackbody_emissive_power(c_o,n,k,2000,h,lambda_at_2000K)
print(f'{Spectral_blackbody_emissive_power_at_2000K} W/m²µm')


#%% Evaluate spectral blackbody emissive power


total_emissive_power=emissive_power(n,T_eval)
print(f'{total_emissive_power} W/m²')




