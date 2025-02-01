import time
import pandas as pd


def calc(data, key1, key2):
    avr = 0
    numbersForAvr = 0
    trueAvr = 0
    flag = False
    thereIsNoMax = True
    for dic in data:
        for item in dic:
            if (item == key1):
                avr += dic[item]
                numbersForAvr += 1
    trueAvr = avr / numbersForAvr
    for dic in data:
        flag = False
        for item in dic:
            if (item == key1):
                if (dic[key1] > trueAvr):
                    flag = True
        if (flag):
            for item in dic:
                if (item == key2):
                    if (thereIsNoMax):
                        max = max = dic[key2]
                        thereIsNoMax = False
                    elif (dic[key2] > max):
                        max = dic[key2]
    return max


data = [{'A': 20, 'B': 30.5}, {'A': 15, 'B': 140}, {'A': 24, 'B': 26.25}]
print(calc(data, 'A', 'B'))

# pandas way

filedata = pd.DataFrame(data)


def pandascalc(filedata, key1, key2):
    avr = filedata[key1].mean()
    bigA = filedata.loc[filedata[key1] > avr]
    return bigA[key2].max()


print(pandascalc(filedata, 'A', 'B'))

# the time difference

time1=time.time()
for i in range(10000):
    calc(data,'A','B')
time2=time.time()
print(f"the time for the first way (without pandas) is {time2-time1}")
time1=time.time()
for i in range(10000):
    pandascalc(filedata,'A','B')
time2=time.time()
print(f"the time for the second way (using pandas) is {time2-time1}")
