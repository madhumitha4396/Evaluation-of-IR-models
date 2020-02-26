# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 22:16:32 2019

@author: Madhu
"""

# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request 
#import urllib2

url = "http://3.17.153.68:8983/solr/"
core = "DFR"
url_remain = "/select?defType=dismax&mm=3&q="
#url_remain = "/select?q="
url_tail = "&fl=id%2Cscore&qf=text_en%5E1.8%20text_de%5E1.8%20text_ru%5E1.2&wt=json&ps=3&indent=true&rows=20"
#url_tail = "&fl=id%2Cscore&wt=json&indent=true&rows=20"
outf = open("DFRfinalfinal.txt", 'a+')

with open("test_queries.txt","r", encoding="utf-8") as f:
    for line in f:
        splitted = line.split(" ",1)
        qid = splitted[0]
        query = splitted[1]
        query = query.replace(":","")
        query = "("+query+")"
        finalUrl = url+core+url_remain+"text_en%3A"+urllib.parse.quote(query)+"+"+"text_de%3A"+urllib.parse.quote(query)+"+"+"text_ru%3A"+urllib.parse.quote(query)+url_tail
        print(finalUrl)
        data = urllib.request.urlopen(finalUrl)
        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
            outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + core + '\n')
            rank += 1

outf.close()
