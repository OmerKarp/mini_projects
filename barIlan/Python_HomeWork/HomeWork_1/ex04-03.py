import numpy as np
from matplotlib import pyplot as plt


def fac(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


def ex(x, n):
    ex = 0
    for i in range(int(n)):
        ex += (x ** i) / fac(i)
    return ex

plt.figure()
x = np.arange(100)
plt.subplot(2,1,1)
plt.plot(x, np.exp(x), label='e^x', color='r')
plt.legend()


    # e^x graph

plt.subplot(2,1,2)
n = input("enter the amount of items in the tylor seiries: ")
y = ex(x, n)
plt.plot(x, y, label='tylor series', color='b')
plt.legend()
plt.show()

    #can't put more than n > 5 the tylor series breaks becuase we go over the limit...