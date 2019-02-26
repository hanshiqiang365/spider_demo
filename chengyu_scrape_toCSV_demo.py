#author: hanshiqiang365 （微信公众号）
import requests
from bs4 import BeautifulSoup
import pandas as pd

all_url = 'http://chengyu.t086.com/'


#http请求头
Hostreferer = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)','Referer':'http://chengyu.t086.com/'}

word=['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']

chengyu_list = []

for w in word:
    for n in range(1,100):
        url=all_url+'list/'+w+'_'+str(n)+'.html'
        start_html = requests.get(url,headers = Hostreferer)
        if(start_html.status_code==404):
            break
        start_html.encoding='gbk'
        soup = BeautifulSoup(start_html.text,"html.parser")

        listw = soup.find('div',class_='listw')
        
        lista = listw.find_all('a')
        for p in lista:
            print(p.text)
            chengyu_list.append(p.text)

result = pd.DataFrame(chengyu_list, columns = ['成语'])

result.to_csv("chengyu.csv",encoding="utf_8_sig", index=False)

print(result)
