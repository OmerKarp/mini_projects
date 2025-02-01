import numpy as np

def f(x):
    return np.e ** np.sin(x)

def trapezoidalApproximation(f, a, b, n):
    sum = 0
    for i in range(n):
        xi = a + (i / n) * (b - a)
        xi1 = a + ((i + 1) / n) * (b - a)
        sum += f(xi) + f(xi1)
    return sum * ((b - a) / (2 * n))

a=0
b=2*np.pi
integral=7.9549265
sum = 0

for i in range(1,21):
    print(f"Number of intervals={i}\n"
          f"Aapproximated Integral={trapezoidalApproximation(f,a,b,i)}\n"
          f"Absolute error={abs(integral - trapezoidalApproximation(f,a,b,i))}\n"
          f"Relative error={abs((integral - trapezoidalApproximation(f,a,b,i))/integral)}\n")
