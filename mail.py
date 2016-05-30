# -*- coding: cp949 -*-
from openxml import *
#from http.client import HTTPConnection
#from http.server import BaseHTTPRequestHandler, HTTPServer

##global
#conn = None
#regKey = 'znVUfN19h13joo2Gts8KcA5nRmrQqROMDrbS2MhHLoKqKj48y6gGrYVz4HzLtZbxHJWWqG%2BpTmvFAegtC7aNsA%3D%3D&numOfRows=10&pageSize=10&pageNo=1&startPage=1'

# 네이버 OpenAPI 접속 정보 information
#server = "openapi.data.go.kr"

# smtp 정보
host = "smtp.gmail.com" # Gmail SMTP 서버 주소.
port = "587"


def sendMain():
    global host, port
    #html = ""
    title = str(input ('Title :'))
    senderAddr = str(input ('sender email address :'))
    recipientAddr = str(input ('recipient email address :'))
    msgtext = str(input ('write message :'))
    passwd = str(input (' input your password of gmail account :'))
    msgtext = str(input ('Do you want to include book data (y/n):'))
    #if msgtext == 'y' :
        #keyword = str(input ('input keyword to search:'))
      #  html = searchTitle(keyword)
    
    import smtplib
    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    
    #Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    #set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    
    msgPart = MIMEText(msgtext, 'plain')
 #   bookPart = MIMEText(html, 'html', _charset = 'UTF-8')
    
    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
  #  msg.attach(bookPart)
    
    print ("connect smtp server ... ")
    s = smtplib.SMTP(host,port)
    #s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)    # 로긴을 합니다. 
    s.sendmail(senderAddr , [recipientAddr], msg.as_string())
    s.close()
    
    print ("Mail sending complete!!!")

