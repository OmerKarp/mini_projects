import matplotlib.pyplot as plt
import numpy as np

def ljx(j, x, arrayOfPoints):
    answer = 1
    for i in range(0, len(arrayOfPoints)):
        if (i != j):
            top = x - arrayOfPoints[i, 0]
            bot = arrayOfPoints[j, 0] - arrayOfPoints[i, 0]
            answer *= top / bot
    return answer


def px(x, arrayOfPoints):
    answer = 0
    for i in range(0, len(arrayOfPoints)):
        answer += (ljx(i, x, arrayOfPoints) * arrayOfPoints[i, 1])
    return answer

points=np.array([])
xpoints=np.array([])
n=int(input("enter how many points: "))
for i in range(n+1):
    xpoints=np.append((2*i)/n-1,xpoints)

    #gets the x values

ypoints=1/(xpoints**2+1)

    #gets y values

for i in range(len(xpoints)):
    points=np.append(xpoints[i],points)
    points=np.append(ypoints[i],points)
points=np.flip(points)
points=points.reshape((len(xpoints),2))

    #puts everything in the points array

x = np.arange(-1, 1.1, 0.1)
plt.plot(x, px(x, points), label="P(x)", marker='.')
plt.plot(x,1/(x**2+1),label="1/(x^2+1)",marker='.')
plt.legend()
plt.show()