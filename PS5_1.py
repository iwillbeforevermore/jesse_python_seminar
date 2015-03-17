from PS2_1 import *
import time
import numpy as np
from matplotlib.pyplot import plot, show
from math import sqrt, pi, exp, cos, sin
from const import E0

k = 1.0 / (4 * pi * E0)

def lamda (theta):
    return (1E-6)/(1+exp(-5*(theta-pi/2)))

def Phi(P):
    t = -pi/2
    circ = pi
    ring = (np.array([0.0,0.0,0.0]),np.array([0.0,2.0,0.0]))
##    x = cos(t)
##    y = sin(t)+1
##    print x, y
##    ringParam = np.array([x,y])
    dt = .1
    phi = 0.0
    for i in xrange(int(circ/dt)):
        dq = lamda(i*dt)*dt
        x = cos(i+t)
        y = sin(i+t)+1
        #print x,y
        pos = (np.array([x,y,0.0]))
        r = np.linalg.norm(P-pos)
        phi += k*dq/r
    return phi

start = time.time()
path = range(50)
V = []
for j in path:
    V.append(Phi(np.array([0.01, j / 20.0, j / 30.0])))

plot(path, V)
print start - time.time()
show()
