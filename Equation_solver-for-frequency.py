# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:32:40 2024

@author: Khalid
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def f(x):
    f=3/x-np.exp(x)/((np.exp(x)-1) )
    return f

def df(x_value):
    # Define the symbolic variable
    x = sp.symbols('x')
    f = 3/x - sp.exp(x)/(sp.exp(x) - 1)
    f_prime = sp.diff(f, x)
    value_at_x_value = f_prime.subs(x,x_value)
    return value_at_x_value
#%%

x=np.linspace(-10,100,210)

function=f(x)
plt.figure(dpi=300)
plt.axhline(y=0, linestyle='--', color='black')
plt.ylim([-20,10])
plt.plot(x,function)
plt.xlabel("x")
plt.ylabel("f")

#%% Solution of the function

x=np.zeros(1000)
err=np.ones(1000)
x_value=2
x[0]=x_value
for i in range(x.size-1):
    value=x[i]
    x[i+1]=x[i]-f(value)/df(value)
    err[i]=(x[i+1]-x[i])/x[i] *100
    if err[i]==0:
        print(f'Solution is {x[i]}')
        solution=x[i]
        break

plt.axvline(x=x[i],linestyle='--', color='red')
plt.text(10,10/2,f"{solution:0.4f} is the solution ") # upto 4 decimal point solution