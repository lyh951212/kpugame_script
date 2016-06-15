# -*- coding: utf-8 -*-
"""
Created on Mon May 30 00:44:18 2016

@author: yeonheelee
"""
loopFlag = 1
from openxml import *
from mail import *

def printMenu():
    print("\nWelcome! data.co.kr Manager Program (xml version)")
    print("========Menu==========")
    print("메일보내기: p")
    print("키워드로 주제찾기:   q")
    print("서비스 설명:   d")
    print("전체출력: b")
    print("========Menu==========")

def launcherFunction(menu):
    if menu ==  'l':
        one()
    elif menu == 'q':
        keyword = str(input ('input keyword to search :'))
        searchTitle(keyword)
    elif menu == 'p':
        sendMain()
    elif menu == 'b':
        two()
    elif menu == 'd':
        keyword2 = str(input ('설명을 볼 openapi주제명 :'))
        descrip(keyword2)
    else:
        print ("error : unknow menu key")
##run###############################################     
one()
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
