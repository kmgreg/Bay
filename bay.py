import matplotlib.pyplot as plt
import math as math
import numpy as np

# magic number list
px = -10875.331581
r = 6.81504915679406

ancient = 0
ancientl = 0

#the original function, using x, lambda(l) and mu (m)
def evaluate(x,l,m):
    term1 = (l*(1/math.sqrt(2*math.pi))*(math.pow(math.e,(-(math.pow(x,2))/2))))
    term2 = ((1 - l)*(1/(math.sqrt(2*math.pi*(.1*.1))))*(math.pow(math.e,(-((x-m)*(x-m))/(2*(.1*.1))))))
    return term1 + term2

#evaluates the likelihood for a given lambda
def loglikelihood(l,m):
    old = 1
    with open("problem_data.dat") as d:
        for line in d:
            new = evaluate(float(line),l,m)
            if (new > 0):
                old = old + np.log(new)
    #print(np.power(np.e,goodlog(old) + np.log(r) - np.log(px)),' ', l)
    return goodlog(old)
    #return np.power(np.e,goodlog(old))


#the offset to reduce underflow
def goodlog(value):
    return value + 5000

#a left reimann sum of the loglikehood
def rsum(m):
    list = []
    sum = 0
    val = 0.01
    for x in range(0,int(1/val)):
        sum = sum + (loglikelihood(x*val,m)* val)
        list.append(sum/px)
    return list

ne = np.vectorize(evaluate)
nl = np.vectorize(loglikelihood)
r = np.vectorize(rsum)
m = np.arange(0,1,.01)
#range(-5,5, .05)
l = np.arange(0.05,1,.05)
plt.title('CDF of Lambda', fontsize=20)
plt.xlabel('Value of Lambda')
plt.ylabel('CDF')
#plt.plot(c,ne(c,.9,3))
#plt.plot(l,nl(l,3))
plt.plot(m,r(3))
plt.show()
#print(rsum(3))