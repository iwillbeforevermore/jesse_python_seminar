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
        dq = lamda(i*dt)*dt # Great! You might even start with theta = i * dt
        x = cos(i*dt+t) # This only works because R = 1
        y = sin(i*dt+t)+1 # Generally, use x = R * cos(theta)
        #print i*dt+t # I'll trust that this shift by t is correct.
        #print x,y # Offhand, it looks reasonable...
        pos = (np.array([x,y,0.0]))
        r = np.linalg.norm(P-pos)
        phi += k*dq/r
    return phi # Looks right to me.

start = time.time()
path = range(50)
V = []
for j in path:
    V.append(Phi(np.array([0.01, j / 20.0, j / 30.0])))

plot(path, V)
print "it took this long:" , (time.time()-start)
show()



##now, we do this along the path of z axis from 0..2
##this is because i accidentally used x and y in the
##first part...whoops.

# Couldn't you just set pos = np.array((x, 0.0, y)) in Phi(P)?

def PhiForY(y):
    totalLamda = 0
    for i in range(50):
        totalLamda += lamda(i/pi)
    phi =  k*totalLamda*1*pi/sqrt(1+y**2)
    #print phi
    return phi

path2 = range(50)
Vy = []
err = []
for j in path2:
    num = Phi(np.array([0.0, j / 2.0, 1.0]))
    theo = PhiForY(j/2.0)
    Vy.append(num)
    err.append((num-theo)/float(theo))
    print err
plot(path, Vy)
plot(path,err)
show()

##i know my PhiForY function is wrong somewhere...
##but i've been sick all weekend and have an awful headache...

# Correcting PhiForY isn't easy.
# I might've recommended office hours at this point...



