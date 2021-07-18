import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent as ua
url='https://www.ptt.cc/bbs/Food/index.html'
ua1=ua().random
headers = {'User-Agent':"".format(ua1)}
import time
import random
import pandas as pd


columns=['標題', '網址', '內文','推','噓', '分數','作者','時間']
data=[]

ss=requests.session()


for l in range(0,1):
    res =None 
    while True:
        try:
            res =ss.get(url,headers = headers)
            break
        except:
            pass
    soup = BeautifulSoup(res.text,'html.parser')

    titletag = soup.select('div.title')

    for i in titletag:
        try:
            title =i.select('a')[0].text
            arturl= "https://www.ptt.cc/"+i.select('a')[0]['href']
            ua2=ua().random
            headers = {'User-Agent':"".format(ua2)}
            artres=ss.get (arturl,headers= headers)
            artsoup = BeautifulSoup(artres.text,'html.parser')
            conten = artsoup.select('div[id="main-content"]')[0].text.split('※ 發信站')[0]
            ats=artsoup.select('span[class="article-meta-value"]')[0].text
            t2=artsoup.select('span[class="article-meta-value"]')[2].text
            tt=artsoup.select('span[class="article-meta-value"]')[3].text
            up=len(artsoup.select('span[class="hl push-tag"]'))
            down=len(artsoup.select('span[class="f1 hl push-tag"]'))
            if up > down :
                sour=up-down
            elif up < down:
                sour=-(down-up)
            
            else:
                sour=0
     
            
            rdata=[title,arturl,conten,up,down,sour,ats,tt]
            data.append(rdata)
            time.sleep(random.randint(1,5))
            
        except IndexError as e:
            print(i)
        
df =pd.DataFrame(data=data,columns=columns)
df    
