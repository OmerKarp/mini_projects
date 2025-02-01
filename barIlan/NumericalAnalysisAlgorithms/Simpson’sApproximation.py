import numpy as np

def f(x):
    return np.e ** np.sin(x)

def simpsonsApproximation(f, a, b, n):
    sum = 0
    for i in range(n):
        xi = a + ((b - a) / n) * i
        xi1 = a + ((b - a) / n) * (i+1)
        sum +=np.e ** np.sin(xi) + 4 * np.e ** np.sin((xi + xi1)/2) + np.e ** np.sin(xi1)
    return sum * ((b - a) / (6 * n))

a=0
b=2*np.pi
integral=7.9549265
sum = 0

for i in range(1,21):
    print(f"Number of intervals={i}\n"
          f"Aapproximated Integral={simpsonsApproximation(f,a,b,i)}\n"
          f"Absolute error={abs(integral - simpsonsApproximation(f,a,b,i))}\n"
          f"Relative error={abs((integral - simpsonsApproximation(f,a,b,i))/integral)}\n")
