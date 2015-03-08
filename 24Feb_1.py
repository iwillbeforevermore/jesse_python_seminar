from PS2_1 import *
from visual import *
from math import pi, sqrt

rod = cylinder(pos = (4,0,0),
               axis = (-8,0,0),
               radius = .05,
               color = color.red,
               opacity = 0.6)
gauss = cylinder(pos = (1,0,0),
                 axis = (-2,0,0),
                 radius = .5,
                 opacity = 0.5)

def gaussElectricField(density, rg, lg):
    dA = 2*pi*rg*lg
    rhs = density*lg/E0
    return rhs/dA

def gaussFlux(density, lg):
    return density*lg/E0

def cylToCart(r, theta, x):
    return (x, r*cos(theta),r*sin(theta))

##def drawElectricFieldVector(r):
##    magnitude = gaussElectricField()

scalefactor = .000005
density = 10**(-5)
l = 8
lg = 1.0/2
rg = 1.0/2
magnitude = gaussElectricField(density, rg, lg)
flux = gaussFlux(density, lg)
axis0 = cylToCart(scalefactor*magnitude, 0, 0)
pos0 = cylToCart(rg,0,0)
e0 = arrow(pos = pos0,
           axis = axis0,
           opacity = 0.3,
           color = color.orange)
label(pos = axis0, text = "arrow of e-field vector")

print ("magnitude is: "), (magnitude)
print ("flux is: "), (flux)


xAxis = arrow(pos = (0,0,0),
              axis = (1,0,0),
              color = color.blue,
              opacity = .7)
yAxis = arrow(pos = (0,0,0),
              axis = (0,1,0),
              color = color.blue,
              opacity = .7)
zAxis = arrow(pos = (0,0,0),
              axis = (0,0,1),
              color = color.blue,
              opacity = 1)
