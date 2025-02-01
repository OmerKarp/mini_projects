import numpy as np
import matplotlib.pyplot as plt

print("Using (1/2, 1, -1) as starting guess")
xplt1 = np.arange(1, 21)
yplt1 = np.array([])
A = [[-2, 1, 1], [0, 3, -1], [1, 0, -4]]
b = [2, 0, 3]
x = [1/2, 1, -1]  # starting guess
temp_x = [1, 1, 1]  # temp variable
solution = [-1.8, -0.4, -1.2]  # the real solution for error analysis
for _ in range(20):
    for i in range(3):
        sum_ = 0
        for k in range(3):
            if i == k:
                continue
            else:
                sum_ += A[i][k] * x[k]
        temp_x[i] = 1 / (A[i][i]) * (b[i] - sum_)
    for t in range(3):  # changing the values in x to the next guess
        x[t] = temp_x[t]
    abs_error = 0
    rel_error = 0
    for i in range(3):
        abs_error += abs(solution[i] - x[i])
        rel_error += abs_error/abs(x[i])
    yplt1 = np.append(yplt1, abs_error)
    print(f"""Absolute error for {_} iteration: {abs_error}
Relative error for {_} iteration: {rel_error}""")

plt.scatter(xplt1, yplt1, color='blue')
plt.title("Using (1/2, 1, -1) as starting guess")
plt.show()
