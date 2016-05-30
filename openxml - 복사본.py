# -*- coding: utf-8 -*-
"""
Created on Sat May 28 20:22:21 2016

@author: yeonheelee
"""
req=None
cLen=None
strxml=None
import http.client
def one():
    global strxml
    conn = http.client.HTTPConnection("openapi.data.go.kr")
    conn.request("GET", "http://openapi.data.go.kr/openapi/service/rest/PortalOpenApiService/getOpenapiList?ServiceKey=znVUfN19h13joo2Gts8KcA5nRmrQqROMDrbS2MhHLoKqKj48y6gGrYVz4HzLtZbxHJWWqG%2BpTmvFAegtC7aNsA%3D%3D&numOfRows=999&pageSize=999&pageNo=1&startPage=1")
    req = conn.getresponse()
    print(req.status,req.reason)
 #   cLen = req.getheader("Content-Length")
    if int(req.status)==200:
        print("openapi data downloading complete!")
        strxml=req.read(cLen)
       # return two(req.read(cLen))
    else:
        print("openapi request has been failed!!")
        #return None
def two():
    global strxml
    from xml.etree import ElementTree
    tree=ElementTree.fromstring(strxml)
    itemElements=tree.getiterator("item")
    for item in itemElements:
        station=item.findtext('oprtinNm')
        print(station)
        
def searchTitle(keyword):
     #get Book Element
    global strxml
    from xml.etree import ElementTree
    tree=ElementTree.fromstring(strxml)
    bookElements = tree.getiterator("item")  # return list type
    for item in bookElements:
        strTitle = item.find("oprtinNm")
        print(strTitle.findtext(keyword))
          