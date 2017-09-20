# -*- coding: utf-8 -*-
import math
import urllib2
import pylab
import numpy
import matplotlib.mlab as mlab
import math
import matplotlib
#русские буквы осей
from matplotlib import rc
rc('font',**{'family':'serif'})
rc('text', usetex=True)
rc('text.latex',unicode=True)
rc('text.latex',preamble='\usepackage[utf8]{inputenc}')
rc('text.latex',preamble='\usepackage[russian]{babel}')
#
DataS = eval(open("DataSolely.txt", "r").readline())
DataNS = eval(open("DataNotSolely.txt", "r").readline())
DataB = eval(open("DataBoth.txt", "r").readline())
maximum = 10000000
p = numpy.arange(0, maximum, 1000)
sigma = 100000
pnormS = 0
for h in range(len(DataS)):
	pnormS += mlab.normpdf(p, DataS[h], sigma)
pnormS = pnormS / len(DataS)
pnormNS = 0
for h in range(len(DataNS)):
	pnormNS += mlab.normpdf(p, DataNS[h], sigma)
pnormNS = pnormNS / len(DataNS)
pnormB = 0
for h in range(len(DataB)):
	pnormB += mlab.normpdf(p, DataB[h], sigma)
pnormB = pnormB / len(DataB)
pylab.plot(p, pnormS)
pylab.plot(p, pnormNS)
pylab.plot(p, pnormB)
pylab.annotate(u'Семьи, где зарабатывает только депутат', xy=(2.10*10**6, 4.2*10**(-7)), xytext=(3.10*10**6, 5.2*10**(-7)),
            arrowprops=dict(facecolor='blue', shrink=0.1),
            )
pylab.annotate(u'Семьи, где зарабатывает и депутат, и супруга/супруг', xy=(2.43*10**6, 3.37*10**(-7)), xytext=(3.10*10**6, 4.2*10**(-7)),
            arrowprops=dict(facecolor='green', shrink=0.1),
            )
pylab.annotate(u'Все типы семей', xy=(2.53*10**6, 2.66*10**(-7)), xytext=(3.10*10**6, 3.2*10**(-7)),
            arrowprops=dict(facecolor='red', shrink=0.1),
            )
pylab.xlabel(u'Доход')
pylab.ylabel(u'Плотность')
pylab.show()