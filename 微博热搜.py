import requests
from bs4 import BeautifulSoup
import re

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        print('error')

def resouParser(html):
    soup = BeautifulSoup(html,'html.parser')
    trs = soup.find_all(name='tr')
    root_url = 'https://s.weibo.com'

    data_1 = ['上升']
    data_1.append(trs[1].a.string)
    data_1.append(0)
    data_1.append(root_url + trs[1].a['href'])
    trs = trs[2:]
    data = [data_1]
    print(data)

    for tr in trs:
        a = [tr.td.string,tr.a.string,int(tr.span.string),root_url + tr.a['href']]
        if(a[1] == None):
            b = re.split('>',str(tr.a))[1]
            c = re.split('<',str(b))[0]
            a[1] = c
            try:
                img_url = tr.find(name = 'img')['src']
                res = requests.get('http:'+ str(img_url))
                a.append(res.url)
                #print(res.content)
            except:
                print('pass')

        print(a)
        pass




resouParser(get_html('https://s.weibo.com/top/summary'))