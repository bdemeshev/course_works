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
expon = []
lam = []
counter = 0
st = 0 #стартовый аукцион
an = 29 #последний аукционов
sigma = 0.03
general_list = []
winners = []
winner_numbers = []
for a in range(st, an):
	lam.append(0)
# парсинг
items = BeautifulSoup(urllib2.urlopen("http://www.uniquebidhomes.com/lub/results.php"))
q0 = len(items.find("table", {"class" : "content_table"}).findAll("img", {"width" : "120"}))
for i in range(st, an):
	expon.append([])
	item_url = "http://www.uniquebidhomes.com/lub/" + items.find("table", {"class" : "content_table"}).findAll("a")[i]["href"]
	print str(i+1) + ")"
	print item_url
	list = []
	page = BeautifulSoup(urllib2.urlopen(item_url))
	q = len(page.find("div", {"id" : "mem_table_rows"}).findAll("td", {"align" : "right"}))
	for x in range(0, q - 1):
		bid = page.find("div", {"id" : "mem_table_rows"}).findAll("td", {"align" : "right"})[x].text
		if bid.count("&nbsp;") == 2:
			bid = bid.replace("&nbsp;", "")
			bid = bid.replace(" ", "")
			bid = bid.replace("$", "")
			bid = float(bid)
			winner = bid
			winner_number = x
		else:
			bid = bid.replace("&nbsp;", "")
			bid = bid.replace(" ", "")
			bid = bid.replace("$", "")
			bid = float(bid)
		list.append(bid)
	print list
	print "winner " + str(winner)
	general_list.append(list)
	winners.append(winner)
	winner_numbers.append(winner_number)
print winner_numbers
print winners
print "general"
print general_list
for t in range(st, an):
	maxt = max(general_list[t])
	print maxt
	if maxt > 5:
		maxt = 5
	else:
		maxt = maxt
	p = numpy.arange(0, maxt, 0.01)
	pt = []
	ptnorm = 0
	for h in range(len(general_list[t])):
		ptnorm += mlab.normpdf(p, general_list[t][h], sigma)
	ptnorm = ptnorm / len(general_list[t])
	#ML
	for r in range(len(p)):
		expon[t].append(0)
	lam[t] = float(sum(general_list[t])) / len(general_list[t])
	print lam[t]
	lam[t] = 1 / lam[t]
	for r in range(len(p)):
		expon[t][r] = lam[t] * math.exp(-lam[t]*p[r])
	matplotlib.pyplot.clf()
	pylab.plot(p, ptnorm)
	pylab.plot(p, expon[t])
	pylab.xlabel(u'Величина ставки')
	pylab.ylabel(u'Плотность')
	pylab.show()
	