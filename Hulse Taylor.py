import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from astropy import constants as con

def func(t,A,t_0):
    return A*(t-t_0)**2
data=np.loadtxt('Hulse_Taylor.txt')



a=data[:,0]
b=data[:,1]
c=data[:,2]
d=data[:,3]
e=data[:,4]
f=data[:,5]
g=data[:,6]
h=data[:,7]
plt.plot(a,f,'o k')

popt,pcov=curve_fit (func,a,f)
#popt,pcov=curve_fit (func,b,f)

print(popt)

xfit=np.arange(1973,2014.0,0.01)

plt.plot(xfit,func(xfit,*popt),'r')
plt.title("Hulse Taylor Binary",fontsize='15',fontweight='bold')

plt.xlabel('Year',fontsize='15',fontweight='bold')
plt.ylabel('Cumulative Shift of Periastron Time(s)',fontsize='15',fontweight='bold')
plt.grid()
plt.show()
