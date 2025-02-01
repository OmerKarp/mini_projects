import time


def minDivaiderOtef(a,b):
    return minDivaider(a,b,2)

def minDivaider(a,b,num):
    if(num%a==0 and num%b==0):
        return num
    return minDivaider(a,b,num+1)

while(True):
    try:
        a = float(input("Please enter the first number :"))
        b = float(input("Please enter the second number :"))
        print(minDivaiderOtef(a,b))
        break
    except Exception:
        print("Please enter another 2 numbers\n")

# The way from HomeWork 2 Q1

def func(x,y):
    z=1
    flag=True
    while(flag):
        if(z%x==0 and z%y==0):
            flag=False
            break
        z=z+1
    return z

# time.time() check for speed

time1=time.time()
for i in range(10000):
    func(54,33)
time1close=time.time()

time2=time.time()
for i in range(10000):
    minDivaiderOtef(54,33)
time2close=time.time()

print(f"the way WITHOUT recursion took {time1close-time1} for running 10,000 times \n"
      f"the way WITH recursion took {time2close-time2} for running 10,000 times \n"
      f"the way WITHOUT recursion was {(time2close-time2)/(time1close-time1)*100}%   more efficient.")