from math import pi
from const import E0
k = 1 / (4 * pi * E0)

class capacitor:
    def __init__(self, capacitance, ref):
        self.capacitance = float(capacitance)               # This will be in Farads
        self.q = 0.0

    def charge(self, voltage):
        self.q = self.capacitance * voltage                 # This will be in Coulombs
        self.ref[self] = self.q

class sph_cyl_cap(capacitor):
    def __init__(self, cylHeight, cylRadius,
                 sphRadius, sep, ref):                     # ref is not necessarily a
        steps
        find E of cylinder and sphere using Gauss
        integrate E of cylinder with ds from cylRadius to sep-sphRadius
        integrate E of sphere with ds from sphRadius to sep-sphRadius
        



        self.area = float(area)                             #   named dict, just a dict
        self.sep = float(sep)
        self.ref = ref                                      # We can refer to ref as an
        self.capacitance = E0 * area / sep                  #   attribute of self
        self.q = 0.0

