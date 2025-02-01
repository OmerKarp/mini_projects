import numpy as np

def f(x):
    return np.e ** np.sin(x)

def gaosApproximation(f, a, b, n):
    sum = 0
    temp=0
    for i in range(n):
        xi = a + ((b - a) / n) * i
        xi1 = a + ((b - a) / n) * (i+1)
        t = (xi1 - xi)/2
        sum += t*((np.e ** np.sin(t * (-1/np.sqrt(3)) + ((xi1+xi)/2))) + (np.e ** np.sin(t * (1/np.sqrt(3)) +((xi1+xi)/2))))
    return sum

a=0
b=2*np.pi
integral=7.9549265
sum = 0

for i in range(1,21):
    print(f"Number of intervals={i}\n"
          f"Aapproximated Integral={gaosApproximation(f,a,b,i)}\n"
          f"Absolute error={abs(integral - gaosApproximation(f,a,b,i))}\n"
          f"Relative error={abs((integral - gaosApproximation(f,a,b,i))/integral)}\n")
