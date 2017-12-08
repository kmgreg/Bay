import matplotlib.pyplot as plt
import math as math
import numpy as np

# magic number list
px = 13.6821049679
r = 6.81504915679406

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

def goodlog(value):
    return value + 5000

def rsum(m):
    sum = 0
    val = 0.005
    for x in range(0,int(1/val)):
        sum = sum + (loglikelihood(x*val,m)* val)
        #print(sum)
    return sum

def lcdf(l,m):
    return np.power(np.e,loglikelihood(l,m) + np.log(r) - np.log(px))

ne = np.vectorize(evaluate)
nl = np.vectorize(loglikelihood)
vl = np.vectorize(lcdf)
c = np.arange(-5,5, .05)
l = np.arange(0.05,1,.05)
m = np.arange(0,1,.05)
#plt.title('ln L vs lambda', fontsize=20)
#plt.xlabel('Value of Lambda')
#plt.ylabel('Log Likelihood')
#plt.plot(c,ne(c,.9,3))
#plt.plot(l,nl(l,3))
#plt.plot(m,vl(m,3))
#plt.show()
print(rsum(3))