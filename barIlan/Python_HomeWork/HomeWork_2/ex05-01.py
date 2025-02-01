import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy

plt.figure()

f = np.genfromtxt('filedata.txt', delimiter=',')
x = f[:, 0]
y = f[:, 1]

plt.subplot(2, 1, 1)
plt.plot(x, y, 'o', label="normal x,y", color='r')
plt.legend()
plt.subplot(2, 1, 2)

func = scipy.interpolate.interp1d(x,y)

xnew=x
ynew=func(xnew)
plt.plot(xnew,ynew,label='interpolation',color='b')

plt.legend()
plt.show()