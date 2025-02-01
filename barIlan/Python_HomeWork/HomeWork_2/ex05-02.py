import numpy as np
import matplotlib.pyplot as plt
import scipy

def f(x):
    return 2-x**2


sol=scipy.optimize.root(f,[-1,1])
for i in sol.x:
    if(i>0):
        print("the approximation is:",i)
        value=i
sqrt2=1.41421356237
print(f"the square root of 2 is {sqrt2},we got {value},the difference is {sqrt2-value}")


# סעיף ב'

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
g = lambda x: a * x ** 2 + b * x + c
sol = scipy.optimize.root(g, [-b, b])
if b ** 2 - 4 * a * c < 0:
    print("There are no real roots")
else:
    print(f'the root/s are {sol.x}')


x=np.arange(-20,20)
y=g(x)
plt.plot(x,y)
plt.axhline(0,color='b',linestyle="--",linewidth=1)
plt.axvline(0,color='b',linestyle="--",linewidth=1)
plt.show()