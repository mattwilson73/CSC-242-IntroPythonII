# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:14:00 2020

@author: Matt
"""

from urllib.request import Request, urlopen
from html.parser import HTMLParser

url = 'http://zoko.cdm.depaul.edu/csc242/helloworld.html'

content = urlopen(url).read().decode()

parser= HTMLParser()

parser.feed(content)





#response = urlopen('https://www.cdm.depaul.edu')
#html = response.read()
#html = str(html)
#print(html)
