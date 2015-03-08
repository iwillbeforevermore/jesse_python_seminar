##import matplotlib.pyplot as plt
##x = [1,2,3,4,5]
##y = [1., .25, 1./9, 1./16,1./25]
##plt.plot(x,y)
##plt.show()

import matplotlib.pyplot as plt
from math import sqrt, pi, exp
import numpy as np

E0 = 8.854187817e-12
k = 1.0/(4*pi*E0)

def lamda(d):
        return exp(-(d-.5)**2/(0.01))
def Phi(P):
    
    rod1 = np.array([0,0,0])
    rod2 = np.array([0,1,0])
    L = np.linalg.norm(rod2-rod1)

    rod = rod2-rod1
    rod = rod/L
    dy = 1.0e-3

    phi = 0.0

    for i in xrange(int(L/dy)):
        dq = lamda(i)*dy
        pos = np.array([0,rod1[0] + rod[1]*i*dy,0])
        r = np.linalg.norm(P-pos)
        phi += k*dq / r

    return phi

V = []
path = range(100)
for step in path:
    A = np.array([1+(step/1e3),2-(3*step/1e3),2-(step/500.0)])
    V.append(Phi(A))

plt.plot(path,V)
plt.show()
