# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

print("welcome-----------------")

url="https://www.humnews.pk/"

mydata=requests.get(url)
mydata1=BeautifulSoup(mydata.content,'lxml')
menu=mydata1.find_all(class_='menu-mobile-text')
for items in menu:
    #print(items.prettify())
    catagories=items.find(class_='menu-item')
    print(catagories)