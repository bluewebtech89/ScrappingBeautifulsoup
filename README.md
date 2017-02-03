# ScrappingBeautifulsoup
At a high level, our web scraping script does three things: (1) Load the inmate listing page and extract the links to the inmate detail pages; (2) Load each inmate detail page and extract inmate data; (3) Print extracted inmate data and aggregate on race and city of residence.

$ python ScrappingWithBeautifulSoup.py

CRAIG ELTON GILLEN, 20 White Male from SPRING HILL, IA Booked at 7/6/2015 11:51 AM

JEREMY MONTEZ AMERISON SMITH, 27 Black Male from CLIVE, IA Booked at 7/6/2015 11:45 AM

ERIC MARCUS STEEN, 28 White Male from DES MOINES, IA Booked at 7/6/2015 10:21 AM

Inmate city distribution {u'WAUKEE, IA': 1, u'DES MOINES, IA': 6, u'CLIVE, IA': 1, u'DES ,MOINES, IA': 1, u'SPRING HILL, IA': 1}

Inmate race distribution {u'White': 7, u'Black': 3}
