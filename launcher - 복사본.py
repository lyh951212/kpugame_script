# -*- coding: utf-8 -*-
"""
Created on Mon May 30 00:44:18 2016

@author: yeonheelee
"""
loopFlag = 1
from openxml import *

def printMenu():
    print("\nWelcome! data.co.kr Manager Program (xml version)")
    print("========Menu==========")
    print("Load xml:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    print("========Menu==========")

def launcherFunction(menu):
    if menu ==  'l':
        one()
    elif menu == 'q':
        keyword = str(input ('input keyword to search :'))
        searchTitle(keyword)
   # elif menu == 'p':
       # PrintDOMtoXML()
    elif menu == 'b':
        two()
    else:
        print ("error : unknow menu key")
##run###############################################        
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
