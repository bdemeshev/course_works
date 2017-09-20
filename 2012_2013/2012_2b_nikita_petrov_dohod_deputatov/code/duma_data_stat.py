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
Data = eval(open("Data.txt", "r").readline())
print 'Количество семей депутатов, у которых указан доход'
print len(Data)
print 'Количество депутатов, у которых не указан доход'
print 447 - len(Data)
#Составление двух списков: депутаты --- супруги
Data1 = [] #депутаты
Data2 = [] #супруги
Data3 = [] #доходы всех (одномерно)
for i in range(len(Data)):
	Data1.append(Data[i][0])
for i in range(len(Data)):
	Data2.append(Data[i][1])
for i in range(len(Data)):
	Data3.append(Data[i][0])
	Data3.append(Data[i][1])
print 'Доходы депутатов'
print Data1
print 'Доходы супруг/супругов депутатов'
print Data2
print 'Минимальные значения'
print min(Data1), min(Data2)
print 'Максимальные значения'
print max(Data1), max(Data2)
print 'Средние значения: все доходы --- доходы депутата -- доходы супруги'
print sum(Data3)/len(Data3), sum(Data1)/len(Data1), sum(Data2)/len(Data2)
print sorted(Data3)
pylab.plot(sorted(Data3))
pylab.ylabel(u'Доход депутата/супруги')

DataNotSolely = []
for i in range(len(Data)):
	if Data[i][1] != 0:
		DataNotSolely.append(Data[i][0] + Data[i][1])
DataSolely = []
for i in range(len(Data)):
	if Data[i][1] == 0:
		DataSolely.append(Data[i][0])
DataBoth = []
for i in range(len(Data)):
	DataBoth.append(Data[i][0] + Data[i][1])
print 'notSolely'
print len(DataNotSolely)
print DataNotSolely
print 'Solely'
print DataSolely
print len(DataSolely)
print 'Both'
print DataBoth




