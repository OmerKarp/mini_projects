import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure()
f=np.genfromtxt('filedata.txt', delimiter=',')
cordsx=f[:,0]
cordsy=f[:,1]
plt.subplot(2,1,1)
plt.plot(cordsx,cordsy,'o',label="normal x,y",color='r')
plt.legend()
plt.subplot(2,1,2)
plt.plot(cordsx,cordsy**2,'o',label="x,y^2",color='b')
plt.legend()
plt.show()

