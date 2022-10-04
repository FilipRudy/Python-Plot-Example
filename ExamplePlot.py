import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


x = np.array([16,14,12,10,8,6,4,2,0,-2,-4,-6,-8,-10,-12,-14,-16])
y = np.array([10.69,10.68,10.72,9.96,7.97,5.97,3.97,1.98,0,-1.98,-3.97,-5.97,-7.96,-9.95,-10.73,-10.68,-10.69])
z = np.array([10.69,10.68,10.72,9.96,7.97,5.97,3.97,1.98,0,-1.98,-3.97,-5.97,-7.96,-9.95,-10.73,-10.68,-10.69])
f=interp1d(x,y,kind='cubic')
xnew =np.linspace(x[0],x[-1])

plt.scatter(x,z)
plt.plot(xnew,f(xnew))
plt.xticks(np.arange(min(x), max(x)+1, 2.0))
plt.yticks(np.arange(min(x), max(x)+1, 1.5))
plt.xlabel('Iset[mA]')
plt.ylabel('IA[mA]')
plt.gca().legend(['punkty danych','IA[mA]'], loc="upper left")


plt.grid()
plt.show()
