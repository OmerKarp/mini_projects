import copy
from sympy import *
import numpy as np
import math

x = Symbol('x')
f = np.e**sin(x)
df_dx = f.diff(x)
n = int(input("enter a number"))

temp = copy.copy(df_dx)
sum_ = 1


for i in range(1, n+1):
    temp = lambdify(x, temp)
    sum_ += (temp(np.pi)/math.factorial(i)) * (x - np.pi) ** i
    df_dx = df_dx.diff(x)
    temp = copy.copy(df_dx)
int_ = integrate(sum_)
int_ = lambdify(x, int_)
print(int_(2*np.pi) - int_(0))
