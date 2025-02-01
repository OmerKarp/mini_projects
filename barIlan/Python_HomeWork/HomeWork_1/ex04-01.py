import numpy
import numpy as np
def fun(n):
    return (3 * n ** 2 - n) / 2
n = 1
arr = numpy.array([])
flag = True
lowest=0
while (True):
    if(fun(n)-fun(n-1)<lowest and not flag):
        print(f"the lowest number is {int(fun(n)-fun(n-1))} which is",int(fun(n)),"minus",int(fun(n-1)))
        break
    x = (3 * n ** 2 - n) / 2
    arr = np.append(arr, x)
    for y in arr:
        z = x - y
        for item in arr:
            if (item == z ):
                lowest=z
                flag=False
    n += 1
