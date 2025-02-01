import scipy.misc

n=123456789
#need approximation of 0.0000001

def f(x):
    return x**3-123456789

def splitMehthod(f,a,b):
    count=0
    guess=0
    while abs(guess-497.9338592)>0.0000001:
        count+=1
        guess = (a + b) / 2
        if (f(guess)< 0):
            a=(a+b)/2
        else:
            b=(a+b)/2
    return guess ,count

approximation , count =splitMehthod(f,0,n)
print(f"Split method gave as {approximation} after {count} iterations.")

#סעיף ב'

def newtonMethod(f,x):
    count=0
    while abs(x - 497.9338592) > 0.0000001:
        x=x-(f(x)/scipy.misc.derivative(f,x,dx=1e-6))
        count+=1
    return x,count

approximation2,count2=newtonMethod(f,n/2)
print(f"Newton method gave as {approximation2} after {count2} iterations.")

#Advanteges and Disatvanteges of the methods:
#Newton method was a lot easier to code, took less iterations and overall better in every way.
#I would think that my calculator is using Newton method if it uses one of those two methods...
#The split method was easier to understand at first and more intuitive.