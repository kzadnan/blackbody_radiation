# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:21:52 2024

@author: Khalid
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from scipy.constants import Stefan_Boltzmann
def f(x):
    f=x**3/(np.exp(x)-1)
    return f

#%%constants

c_o=3e8 #m/s
n=1
k=1.3807e-23 # J/K
h=6.626e-34 #J.s

C1=2*np.pi*h*c_o**2
C2=h*c_o/k 

#%% Given inputs

lambd2=1e+10 #converting into meter to be unitless in integral
lambd1=1e-6
n=1
T=300

#%%
x=np.linspace(0.1,20,100)
function=f(x)*(C1/C2**4) *n**3 *T**4 /(n**2 *Stefan_Boltzmann*T**4)
plt.figure(dpi=300)
plt.plot(x,function)
plt.ylim([0,max(function)*1.2])

# Define the integration limits
upper_limit=C2/(n*lambd1*T)
lower_limit=C2/(n*lambd2*T)

plt.fill_between(x,0 ,f(x)*(C1/C2**4) *n**3 *T**4 /(n**2 *Stefan_Boltzmann*T**4), where=(x >lower_limit) & (x < upper_limit), color='red', alpha=0.5)
#plt.fill_between(x,0 ,f(x)*(C1/C2**4) *n**3 *T**4 /(n**2 *Stefan_Boltzmann*T**4), where=(x >4) & (x < 7), color='red', alpha=0.5)




# Perform the integration
integral, error = integrate.quad(f, lower_limit, upper_limit)

fraction_power=integral *(C1/C2**4) *n**3 *T**4 /(n**2 *Stefan_Boltzmann*T**4)
print(f'fraction power is {fraction_power}')
plt.text(6,max(function)/2,f"Percentage of emissive power\n in ultraviolet range is {fraction_power*100:.4f}%")
plt.xlabel(r'$x = C_2 /n \lambda T$  ')
plt.ylabel("Fraction of  \n blackbody emissive power")
#%%

