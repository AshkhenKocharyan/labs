__author__ = 'student'
import math
import pylab
from matplotlib import mlab

kmin = -20.0
kmax = 20.0
dk = 0.01
klist = mlab.frange (kmin, kmax, dk)

a=0

pylab.ion()

for t in range (50):
    xlist=[math.sin(t + a) for t in klist]
    ylist=[math.cos(2 * t) for t in klist]
    pylab.clf()
    pylab.plot (xlist, ylist)
    pylab.draw()
    a +=0.5
pylab.pause(5)

pylab.close()