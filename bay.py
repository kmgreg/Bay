import matplotlib.pyplot as plt
import math as math
import numpy as np

def evaluate(x,l,m):
    term1 = (l*(1/math.sqrt(2*math.pi))*(math.pow(math.e,(-(math.pow(x,2))/2))))
    term2 = ((1 - l)*(1/(math.sqrt(2*math.pi*(.1*.1))))*(math.pow(math.e,(-((x-m)*(x-m))/(2*(.1*.1))))))
    return term1 + term2



print(evaluate(5,.9,3))
c = np.arrange(-5, 5, .1)
plt.plot(c,evaluate(c,.9,3))
plt.show()