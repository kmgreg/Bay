import matplotlib.pyplot as plt
import math as math
import numpy as np



def evaluate(x,l,m):
    term1 = (l*(1/math.sqrt(2*math.pi))*(math.pow(math.e,(-(math.pow(x,2))/2))))
    term2 = ((1 - l)*(1/(math.sqrt(2*math.pi*(.1*.1))))*(math.pow(math.e,(-((x-m)*(x-m))/(2*(.1*.1))))))
    return term1 + term2

#evaluates the likelihood for a given lambda
def loglikelihood(l,m):
    old = 1
    for k in range(0,200):
        old = old * evaluate((-5 + (0.05*k)),l,m)
    #return math.log(old,math.e)
    return old

print(evaluate(5,.9,3))
ne = np.vectorize(evaluate)
nl = np.vectorize(loglikelihood)
c = np.arange(-5,5, .05)
l = np.arange(-5,5,1)
#plt.plot(c,ne(c,.9,3))
plt.plot(l,nl(l,3))
plt.show()