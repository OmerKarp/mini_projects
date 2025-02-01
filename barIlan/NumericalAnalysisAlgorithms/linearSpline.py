import random
import matplotlib.pyplot as plt
import numpy as np


def linearSpline(nodes, x):
    for i in range(int(nodes.size / 2)):
        if i != nodes.size / 2:
            if nodes[i, 0] <= x <= nodes[i + 1, 0]:
                lowNode = nodes[i]
                highNode = nodes[i + 1]
                break
        else:
            lowNode = nodes[i - 1]
            highNode = nodes[i]
    sx = ((x - highNode[0]) * lowNode[1]) / (lowNode[0] - highNode[0]) + ((x - lowNode[0]) * highNode[1]) / (
                highNode[0] - lowNode[0])
    return sx


nodes = np.array([])
for i in range(10):
    nodes = np.append(nodes, [i * 3, random.randint(-2, 5)])
nodes = nodes.reshape((10, 2))

x = np.arange(0, 27, 0.5)
y = np.array([])
print(nodes)
for i in range(int(x.size)):
    y = np.append(y, linearSpline(nodes, x[i]))

plt.plot(x, y, color='r', label='linearSpline', marker='^')
plt.scatter(nodes[:, 0], nodes[:, 1], color='b', label='nodes')

plt.axhline(0, color='b', linestyle="--", linewidth=1)
plt.axvline(0, color='b', linestyle="--", linewidth=1)
plt.legend()
plt.show()
