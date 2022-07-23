from math import sin
from numpy import array,arange
import numpy as np
import pylab as plt
z1=np.linspace(6,100,94)
for T_s in [1,10,100]:
    T=[]
    Z=[]
    d=[]
    z=6.0
    for i in range (len(z1)):
        T_nu=(4.0/T_s)*(0.044*(6.626*10**(-34.0))*0.7/0.2)*((0.3*(1+z)**3.0)+0.69+((8.4*10**-5.0)*(1+z)**4.0))**(1.0/2.0)
        delta=(T_s-(2.73*(1+z)))*T_nu/(1+z)
        T.append(T_nu)
        d.append(delta)
        Z.append(z)
        z+=1

    plt.figure(1)   
    plt.plot(Z,T,label=T_s)
    plt.legend({'T_s=1','T_s=10','T_s=100'})
    plt.grid()
    plt.xlabel('z')
    plt.ylabel('\u03C4_\u03C5')
    plt.title('\u03C4_\u03C5 vs z')
    plt.figure(2)
    plt.plot(Z,d,label=T_s)
    plt.legend({'T_s=1','T_s=10','T_s=100'})
    plt.grid()
    plt.xlabel('z')
    plt.ylabel('\u03B4T_b')
    plt.title('\u03B4T_b vs z')
plt.show()
    

    
