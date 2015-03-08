# -*- coding: utf-8 -*-
from PS2_1 import *
from math import sqrt, pi
import time
E0 = 8.854187817e-12
k = 1.0/(4*pi*E0)


##Paola’s child sits at the origin, hugging
#   a ball with a total charge Q =10−6 C on it.
##A blanket with a uniform charge density
#   σ = 10-3 C/m2 faces her from above.
##The blanket is 2m on a side and is
#   centered at (0, 0, 1) m

#flux is component of E perp to surface of
#   blanket times dA

q = 10E-6
sigma = 10E-3
charge = (0,0,0,q)
flux = 0
lengthLoc = -1
widthLoc = -1
dL = .01
dA = dL*dL
dQ = sigma*dA
forceList = [0,0,0]

start = time.time()

while(lengthLoc < 1):
    while(widthLoc < 1):
        eComp = pointChargeField(charge,(widthLoc, lengthLoc,1))
        forceList[0] += eComp[0]*dQ
        forceList[1] += eComp[1]*dQ
        forceList[2] += eComp[2]*dQ
        zComp = pointChargeField(charge,(widthLoc,lengthLoc,1))[2]
        zCompA = zComp*dA
        #print zCompA
        flux = flux + zCompA
        widthLoc = widthLoc + dL
        #print widthLoc
    lengthLoc = lengthLoc + dL
    widthLoc = -1


print ("Using integration, dA= "), (dA), ("we get a flux of: "), (flux)
print ("this took"), (time.time()-start), ("s")
print ""

# A (much) faster way might be to use Gauss's Law
# Gauss's Law states that the flux is equal to
#    charge enclosed divided by E0
# Therefore, total flux = q/E0
# However, we only want the flux through the blanket
#    which is four square meters and floating directly
#    above the point charge
# So, we draw a gaussian box which is a cube, with sides 2m
#    centered at the origin
# The flux through one of these sides (the top one) will
#   be 1/6th of the total flux

start = time.time()

fluxTotal = q/E0
flux2 = fluxTotal / 6
print ("Using gauss's law, we get a flux of: "), (flux2)
print ("this took"), (time.time()-start), ("s")
print ""

print ("The ratio of gauss to integration was: "), (flux2/flux)

#Now as for the force...
#We know that F = E*q
#We know what E is, and we can calculate dQ for each
#   dA by using the sigma area charge density of the blanket
#Then, we just multiply for each component

print ""
print "The force is: "
vectorToString(forceList[0],forceList[1],forceList[2])

# In comparing if the Coulombic force will hold up the
#   blanket, we compare the gravitational force with the
#   calculated Coulombic force
# The gravitational force is simply mass*g, the gravitational
#   acceleration
# For the blanket mass, I make assumptions based on a recently
#   crochet blanket I made. For a blanket about 6ftx5ft, I used
#   5 skeins of yarn. This yarn was 300g per skein. Therefore
#   mass was about 1500g, or 1.5 kg

g = 9.8
m = 1.5

print ("Gravitational force (zDir) is: "), (g*m)
print ("Coulombic force (zDir) is: "), (forceList[2])
print ("The Coulombic force will hold up the blanket!")

