###########################
# Title: Electric Field   #
#       (Point Charge)    #
#       -Visualization-   #
# Filename: PS2_2.py      #
# Author: Jesse Chang     #
###########################
from PS2_1 import *
from visual import *
from math import sqrt, pi

scalefactor = .5

#function to return the total field due to the dipole;
#   uses function pointChargeField and adds results
#   from charge1 and charge2, which works because
#   superposition principle applies to e-fields

def dipoleChargeField(charge1, charge2, location):
    field1 = pointChargeField(charge1, location)
    field2 = pointChargeField(charge2, location)
    fieldTotX = field1[0] + field2[0]
    fieldTotY = field1[1] + field2[1]
    fieldTotZ = field1[2] + field2[2]
    print ("at ") , (location) , (" the field is:")
    vectorToString(fieldTotX, fieldTotY, fieldTotZ)
    print ""
    return (fieldTotX, fieldTotY, fieldTotZ)

#define distance between dipoles
a =.5

#define charges and their locations
charge1 = (0,a,0,4*pi*E0)
charge2 = (0,-a,0,4*pi*E0)

#define test locations
loc0 = (0,0,0)
loc1 = (a,0,0)
loc2 = (0,0,-a)
loc3 = (-a,0,0)
loc4 = (0,0,a)

#calculate electric field components at test locations
axis0 = dipoleChargeField(charge1, charge2, loc0)
axis1 = dipoleChargeField(charge1, charge2, loc1)
axis2 = dipoleChargeField(charge1, charge2, loc2)
axis3 = dipoleChargeField(charge1, charge2, loc3)
axis4 = dipoleChargeField(charge1, charge2, loc4)

#draw charges
q1 = sphere(pos = vector(charge1[0],charge1[1], charge1[2]), radius = .1, color = color.blue)
q2 = sphere(pos = vector(charge2[0],charge2[1], charge2[2]), radius = .1, color = color.red)

#draw electric field vectors
e0 = arrow(pos = loc0, axis = axis0, color = color.orange)
e1 = arrow(pos = loc1, axis = axis1, color = color.orange)
e2 = arrow(pos = loc2, axis = axis2, color = color.orange)
e3 = arrow(pos = loc3, axis = axis3, color = color.orange)
e4 = arrow(pos = loc4, axis = axis4, color = color.orange)



