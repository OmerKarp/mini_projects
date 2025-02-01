import math

import matplotlib.pyplot as plt
import numpy as np
import scipy


def tylorSeries(n, f, a, x):
    s=0
    for i in range(n+1):
        top=scipy.misc.derivative(f,a,dx=1e-6,n=i)
        bot=math.factorial(i)
        s += (top*(x - a) ** i)/bot
    return s

def f(x):
    return np.e**np.sin(x)


x=np.linspace(0,2*np.pi,100)
y=f(x)
yTylor=tylorSeries(2,f,np.pi,x)
yder=scipy.misc.derivative(f, x, dx=1e-5,n=1)
plt.plot(x,y,label='normal')
plt.plot(x,yTylor,label='Tylor')

plt.plot(x,yder,label='der numer 1')



plt.axhline(0,color='b',linestyle="--",linewidth=1)
plt.axvline(0,color='b',linestyle="--",linewidth=1)
plt.legend()
plt.show()