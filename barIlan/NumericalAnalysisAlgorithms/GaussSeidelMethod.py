import numpy as np
import matplotlib.pyplot as plt
import math
import random

A = [[-2, 1, 1],
     [0, 3, -1],
     [1, 0, -4]]
b = [2, 0, 3]

xs = np.arange(1, 21)
ys = np.array([])

x = [1/2, 1, -1]
xtemp = [1, 1, 1]
solution = [-1.8, -0.4, -1.2]
for temp in range(20):
    for i in range(3):
        errorAbs = 0
        rel_error = 0
        sum_ = 0
        for j in range(3):
            if i != j:
                sum_ += A[i][j] * x[j]
        xtemp[i] = 1 / (A[i][i]) * (b[i] - sum_)
    for t in range(3):
        x[t] = xtemp[t]
    for i in range(3):
        errorAbs += abs(solution[i] - x[i])
        rel_error += errorAbs/abs(x[i])
    ys = np.append(ys, errorAbs)
    print(f"absolute error with {temp} iteration is {errorAbs}...while the relative error for {temp} iteration is {rel_error}")

plt.plot(xs, ys,label='(1/2, 1, -1)')

xs = np.arange(1, 21)
ys = np.array([])
x = [2, 2, -2]
xtemp = [1, 1, 1]
solution = [-1.8, -0.4, -1.2]
for temp in range(20):
    for i in range(3):
        errorAbs = 0
        rel_error = 0
        sum_ = 0
        for j in range(3):
            if i != j:
                sum_ += A[i][j] * x[j]
        xtemp[i] = 1 / (A[i][i]) * (b[i] - sum_)
    for t in range(3):
        x[t] = xtemp[t]
    for i in range(3):
        errorAbs += abs(solution[i] - x[i])
        rel_error += errorAbs/abs(x[i])
    ys = np.append(ys, errorAbs)
    print(f"absolute error with {temp} iteration is {errorAbs}...while the relative error for {temp} iteration is {rel_error}")
plt.plot(xs, ys,label='(2, 2, -2)')

plt.legend()
plt.show()