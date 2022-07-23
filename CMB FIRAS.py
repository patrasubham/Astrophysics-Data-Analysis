#CMD Firas Data Analysis and fit with the Planck's Black body body radiation formula:
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from astropy import constants as con
#Consider P and Q are the two variables
def func(x,P,Q):
    return P*x**3/((np.exp(Q*x))-1.0)
data=np.loadtxt('CMB.txt')



x=data[:,0]
y=data[:,1]
z=data[:,2]

popt,pcov=curve_fit (func,x,y)
print(popt)
xfit=np.arange(0.0,25.0,0.01)
plt.errorbar (x,y,yerr=600*z,fmt='o''k',ecolor='black',capsize=3,label='CMB FIRAS data')
plt.plot(xfit,func(xfit,*popt),'r',label ='BBR Fit')
plt.xlabel('Frequency [cm$^-$$^1$]',fontweight='bold',fontsize='15')
plt.ylabel('Intensity[ Jy/sr] ',fontweight='bold',fontsize='15')
plt.title('Cosmic Microwave Background from COBE data\n'' Two variables are : P= 3.97704552e+04, Q= 0.528696750 ',fontweight='bold')
print("Planck Constant,h=", con.h.cgs,"\nVelocity of Lighy in Vaccum,c=", con.c.cgs,"\nBoltzmann Constant,kB=", con.k_B.cgs)
print ("T_CMB=",(con.h.cgs*con.c.cgs/(0.528696750*con.k_B.cgs)))
plt.grid()
plt.legend()
plt.show()
