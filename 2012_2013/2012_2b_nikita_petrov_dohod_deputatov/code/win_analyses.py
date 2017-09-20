# -*- coding: utf-8 -*-
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
Data = eval(open("DataW.txt", "r").readline())
sigma = 0.1
maxd = max(Data)
p = numpy.arange(0, maxd, 0.01)
pnorm = 0
for h in range(len(Data)):
	pnorm += mlab.normpdf(p, Data[h], sigma)
pnorm = pnorm / len(Data)
#ML_ expon
expon = []
DataN = []
for i in range(len(Data)):
	if Data[i] <= 5:
		DataN.append(Data[i])
print DataN
for r in range(len(p)):
	expon.append(0)
lam = float(sum(DataN)) / len(DataN)
print lam
lam = 1 / lam
for r in range(len(p)):
	expon[r] = lam * math.exp(-lam*p[r])
pylab.plot(p, pnorm)
pylab.plot(p, expon)
pylab.xlabel(u'Величина ставки')
pylab.ylabel(u'Плотность')
pylab.show()
pylab.plot(Data)