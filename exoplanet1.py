import numpy as np
from numpy import loadtxt,append
from scipy.optimize import curve_fit
import pylab as pl
import pwlf
import matplotlib.pyplot as plt
data=np.genfromtxt("exoplanet.dat")
#print(data)
x=[]
y=[]
y1=[]
y2=[]
yerror=[]
for i in range(len(data)):
	for j in range(3):
		if j==0:
			x.append(data[i][j])
		if j==1:
			y.append(data[i][j])
		
		if j==2:
			yerror.append((data[i][j]))
x1=[]
x11=[]
y1=[]
x3=[]
x33=[]
y3=[]
x2=[]
x22=[]
y2=[]
x4=[]
x44=[]
y4=[]
x6=[]
x66=[]
y6=[]		
#print(len(y))
#print x(i)
for i in range(len(data)):
	if x[i] <= -0.06 :
		x1.append(x[i])
		y1.append(y[i])
	if x[i] >= 0.06 :
		x1.append(x[i])
		y1.append(y[i])

	if x[i] >= -0.043 :
		if x[i] <= 0.043 :
			x3.append(x[i])
			y3.append(y[i])

	if x[i] >= -0.06 :
		if x[i] <= -0.043 :
			x2.append(-x[i])
			y2.append(y[i])
	if x[i] >= 0.043 :
		if x[i] <= 0.06 :
			x2.append(x[i])
			y2.append(y[i])	

		

X4=np.linspace(0.0409,0.063,100)
X44=X4*0.8265820384644904 +0.9494079783499862
X6=np.linspace(-0.063,-0.0409,100)
X66=-X6*0.8265820384644904 +0.9494079783499862
pl.plot(X6,X66,"red")
pl.plot(X4,X44,"red")

X1=np.linspace(-0.16,-0.05,100)
X11=-X1*0.0 +0.9996387072334545
pl.plot(X1,X11,"red")

X5=np.linspace(0.05,0.16,100)
X55=-X5*0.0 +0.9996387072334545
pl.plot(X5,X55,"red")

X3=np.linspace(-0.05,0.05,100)
X33=-X3*0.0 +0.9850330919182078
pl.plot(X3,X33,"red")

m2,c2=pl.polyfit(x2,y2,1)
#print(m2,c2)
#print(x1,y1,x11)
#print(x3,y3,x33)
#m,c=pl.polyfit(x1,y1,1)
m3,c3=pl.polyfit(x3,y3,1)
#print(m3,c3)

plt.scatter(x,y)
"""
pl.plot(x1,x11,"red")
pl.plot(x3,x33,"red")
#pl.plot(X4,x4*0.7219108407419356+0.9551348794510607,"red")
#pl.plot(x4,x44,"red")
#pl.plot(x6,x66,"red")
"""
pl.xlabel('Time (the fractions of a day  from the time at the center of the transit)')
pl.ylabel('Relative Fluxes')
pl.title("Fit a piece-wise linear model into the light-curve data")
pl.grid()
pl.show()
		
'''
plt.plot(x,y)
plt.scatter(x,y)
plt.errorbar(x,y,yerr=yerror)


'''
