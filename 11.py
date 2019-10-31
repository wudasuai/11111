import requests
from bs4 import BeautifulSoup  
import multiprocessing as mp
import time

t1=time.time()
r=requests.get('https://car.autohom.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0-1.html')


c=r.text


soup=BeautifulSoup(c,'html.parser')
page_div=soup.find('div',{'class':'page'})
page=page_div.find_all('a')[-2].text
cars=[]
urls=['https://car.autohom.com.cn/price/list-0-3-0-0-0-0-0-0-0-0-0-0-0-0-0-'+str(i)+'.html' for i in range(1,11)]

def crawl_page(url):
    p_r=requests.get(url)
    p_c=p_r.text
    p_soup=BeautifulSoup(p_c,'html.parser')
    p_content=p_soup.find_all('div',{'class':'list-cont'})
    pandCar=[]
    for car in p_content:
        carDic={}
        carDic['piUrl']=car.find('div',{'class':'list-cont-img'}).find('img')['src']
        carDic['name']=car.find('div',{'class':'list-cont-main'}).find('a').text
        try:
            carDic['score']=car.find('span',{'class':'score-number'}).text
        except Exception:
            carDic['score']=''

            pandCar.append(carDic)
    return pandCar
pool=mp.Pool()
f=soup.find('ul',{'class':'filter-ret clear'})
items =f.find_all('li',{'class':'fl clear'})
for (i,item)in enumerate(items):
    title=item.find('h3').find('a').text
    intro=item.find('div',{'class':'d2'}).text
    img=item.find('img')['src']
    print(i,title,'\t',intro,img)
