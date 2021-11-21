# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:02:04 2021

@author: Pc
"""

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~''' 
my_str = "Hello!!!, he said ---and went."
no_punct=''
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)

