import numpy as np
from statistics import stdev
import matplotlib.pyplot as plt
from scipy.stats import kurtosis,skew

x=np.loadtxt('Qband_wmap5year.txt')
plt.xlim(-0.5,0.5)


a=np.median(x)
b=np.mean(x)
c=stdev(x)
#print ('Median=',a,'Mean=',b,'Standard Deviation=',c)
p=-2.0
q=2.0

d=[]
for j in range(len(x)):
    if(p<=x[j]<=q):
        d.append(x[j])
mu=np.mean(d)
sigma=stdev(d)
median=np.median(d)
print (mu,sigma,median)
num_bins = 200
   
n, bins, patches = plt.hist(d,num_bins, density = 1,color ='green',alpha = 0.7,ec='black')
   
y = ((1 / (np.sqrt(2 * np.pi) * sigma))*np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
  
plt.plot(bins, y, color ='black')
  
plt.xlabel('No. of Bins',fontweight='bold',fontsize='15')
plt.ylabel('Histogram',fontweight='bold',fontsize='15')
  
plt.title('Q-band WMAP in range -2.0 $\mu$K to 2.0$\mu$K\n''$\mu$= 0.01047424061354726, $\sigma$= 0.13270143683228416,M= 0.00605559',
          fontweight ="bold")
#Find Kurtosis:
print( '\nKurtosis for normal distribution :',kurtosis(y))
#Find Skewness:
print( '\nSkewness for data : ', skew(y))
  
plt.show()
