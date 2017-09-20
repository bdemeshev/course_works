# -*- coding: utf-8 -*-
import urllib2
import re
from BeautifulSoup import BeautifulSoup
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
Data = eval(open("DataParties.txt", "r").readline())
DataER = []
DataKPRF = []
DataLDPR = []
DataSR = []
for i in range(len(Data)):
	if Data[i][2] == 1:
		DataER.append(Data[i][0] + Data[i][1])
	elif Data[i][2] == 2:
		DataKPRF.append(Data[i][0] + Data[i][1])
	elif Data[i][2] == 3:
		DataLDPR.append(Data[i][0] + Data[i][1])
	elif Data[i][2] == 4:
		DataSR.append(Data[i][0] + Data[i][1])
print len(DataER), len(DataKPRF), len(DataLDPR), len(DataSR)
print len(DataER) + len(DataKPRF) + len(DataLDPR) + len(DataSR)
#
print 'Максимум: ЕР --- КПРФ --- ЛДПР --- СР'
print max(DataER), max(DataKPRF), max(DataLDPR), max(DataSR)
print 'Среднее'
print sum(DataER)/len(DataER), sum(DataKPRF)/len(DataKPRF), sum(DataLDPR)/len(DataLDPR), sum(DataSR)/len(DataSR)
#
minimum = 0
maximum = 10000000
p = numpy.arange(minimum, maximum, 10000)
sigma = 100000
pnormER = 0
for h in range(len(DataER)):
	pnormER += mlab.normpdf(p, DataER[h], sigma)
pnormER = pnormER / len(DataER)
pnormKPRF = 0
for h in range(len(DataKPRF)):
	pnormKPRF += mlab.normpdf(p, DataKPRF[h], sigma)
pnormKPRF = pnormKPRF / len(DataKPRF)
pnormLDPR = 0
for h in range(len(DataLDPR)):
	pnormLDPR += mlab.normpdf(p, DataLDPR[h], sigma)
pnormLDPR = pnormLDPR / len(DataLDPR)
pnormSR = 0
for h in range(len(DataSR)):
	pnormSR += mlab.normpdf(p, DataSR[h], sigma)
pnormSR = pnormSR / len(DataSR)
pylab.plot(p, pnormER)
pylab.plot(p, pnormLDPR)
pylab.plot(p, pnormKPRF)
pylab.plot(p, pnormSR, color = 'magenta')
pylab.text(7.35*10**6, 7.50*10**(-7), u'Единая Россия', color = 'blue')
pylab.text(7.35*10**6, 7.20*10**(-7), u'ЛДПР', color = 'green')
pylab.text(7.35*10**6, 6.90*10**(-7), u'КПРФ', color = 'red')
pylab.text(7.35*10**6, 6.60*10**(-7), u'Справедливая Россия', color = 'magenta')
pylab.xlabel(u'Доход')
pylab.ylabel(u'Плотность')
pylab.show()