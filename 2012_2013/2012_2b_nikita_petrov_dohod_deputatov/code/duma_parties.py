# -*- coding: utf-8 -*-
import re
from BeautifulSoup import BeautifulSoup
import pylab
import urllib2
inc = []
inc_alt = []
list_page=BeautifulSoup(urllib2.urlopen\
("http://www.duma.gov.ru/structure/deputies/?letter=%D0%92%D1%81%D0%B5"))
for i in range(0,447):
	dep_link = "http://www.duma.gov.ru" +\
	list_page.find("table", {"id" : "lists_list_elements_35"}).findAll("img")[i].parent["href"]
	dep_page = BeautifulSoup(urllib2.urlopen(dep_link)) 
	if dep_page.find("td") is None:
		print "No Data"
		continue
	else:
		dep_party = dep_page.find("div", {"class" : "deputat-info-right"}).find("p", {"class" : "deputat-info-intro"}).text
		dep_party = dep_party.replace(u'Депутат Государственной Думы избран в составе федерального списка кандидатов, выдвинутого Политической партией &laquo;','')
		dep_party = dep_party.replace('&raquo;', '')
		dep_party = dep_party.replace(u'Депутат Государственной Думы избран в составе федерального списка кандидатов, выдвинутого Всероссийской политической партией &laquo;', '')
		dep_party = dep_party.replace(u'Депутат Государственной Думы избран в составе федерального списка кандидатов, выдвинутого Политической партией ', '')
		#1 - edro, 2 - kprf, 3 - ldpr, 4 - spravros
		if dep_party == u'ЕДИНАЯ РОССИЯ':
			dep_par = 1
		elif dep_party == u'Коммунистическая партия Российской Федерации':
			dep_par = 2
		elif dep_party == u'Либерально - демократическая партия России':
			dep_par = 3
		elif dep_party == u'СПРАВЕДЛИВАЯ РОССИЯ':
			dep_par = 4
		dep_inc1 = dep_page.find("table", \
		{"class" : "data-2 data-2-has-even"}).findAll("td")[1].text
		dep_inc1 = dep_inc1.replace(" ", "")
		dep_inc1 = dep_inc1.replace(",", ".")
		dep_inc1 = float(dep_inc1)
		if len(dep_page.find("table", {"class" : \
		"data-2 data-2-has-even"}).findAll("td")) != 2:
			if dep_page.find("table", {"class" : \
			"data-2 data-2-has-even"}).findAll("td")[2].text != u"Ребенок":
				dep_inc2 = dep_page.find("table", \
				{"class" : "data-2 data-2-has-even"}).findAll("td")[3].text
				dep_inc2 = dep_inc2.replace(" ", "")
				dep_inc2 = dep_inc2.replace(",", ".")
				dep_inc2 = float(dep_inc2)
			else:
				dep_inc2 = 0
		else:
			dep_inc2 = 0
	inc.append([dep_inc1, dep_inc2, dep_par])
	inc_alt.append(dep_inc1)
	inc_alt.append(dep_inc2)
	print dep_inc1, dep_inc2, dep_party, dep_par
print inc
print "-------"
print inc_alt
