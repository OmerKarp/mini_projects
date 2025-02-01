import numpy as np
import matplotlib.pyplot as plt

x = []
y = np.array([])
n = int(input("how many points? (bigger then one): "))
for i in range(0, n):
    x.append((2 * i) / (n - 1) - 1)
    y = np.append(y, 1 / (((2 * i) / (n - 1) - 1) ** 2 + 1))

xplt = np.linspace(-1, 1)
vander = np.zeros((n, n))

for i in range(0, n):
    for k in range(0, n):
        if k == 0:
            vander[i][k] = 1
        else:
            vander[i][k] = x[i] ** k
coef = np.linalg.solve(vander, y)

def f(x):
    func = 0
    for i in range(0, n):
        func += coef[i] * (xplt ** i)
    return func


def g(x):
    return 1 / (xplt ** 2 + 1)


plt.plot(xplt, f(x), label="the red one is the interpolation", color="red")
plt.plot(xplt, g(x), label="the blue one is the real function", color="blue")
plt.legend()
plt.show()
