#author: hanshiqiang365 （微信公众号）
import requests
from bs4 import BeautifulSoup
import sqlite3
import uuid

conn = sqlite3.connect("chengyu.db3")  #创建sqlite.db数据库
print ("open database success")
conn.execute("drop table IF EXISTS chengyu")
query = """create table IF NOT EXISTS chengyu(id VARCHAR(50),word VARCHAR(50));"""
conn.execute(query)
print ("Table created successfully")

all_url = 'http://chengyu.t086.com/'

#http请求头
Hostreferer = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)','Referer':'http://chengyu.t086.com/'}

word=['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']

for w in word:
    for n in range(1,100):
        url=all_url+'list/'+w+'_'+str(n)+'.html'
        start_html = requests.get(url,headers = Hostreferer)
        if(start_html.status_code==404):
            break
        start_html.encoding='gb2312'
        soup = BeautifulSoup(start_html.text,"html.parser")

        listw = soup.find('div',class_='listw')
        
        lista = listw.find_all('a')
        for p in lista:
            print(p.text)
            ids=str(uuid.uuid1())
            query = "insert into chengyu (id,word) values ('"+ids+"','"+p.text+"');"
            conn.execute(query)
            conn.commit()
