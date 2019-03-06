import requests
from urllib import parse
from bs4 import BeautifulSoup
import re
def xinglang(index,page):
    print(parse.quote(index))
    print(parse.unquote(parse.quote(index)))
    print(parse.unquote('%CA%B3%C6%B7%B0%B2%C8%AB'))
    try:
        #url ='https://search.sina.com.cn/?q='+ parse.quote(index)+ 'A8&c=news&from=channel&ie=utf-8'
        url = 'https://search.sina.com.cn/?q=%CA%B3%C6%B7%B0%B2%C8%AB&range=title&c=news&sort=time&col=&source=&from=&country=&size=&time=&a=&page='+str(page)+'&pf=2131425434&ps=2134309112&dpc=1'
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'gb2312'
        url_map = {}
        html = response.text
        get_url_map(url_map,html)

        #print(response.text)
    except:
        print('error')
def get_url_map(map,html):
    soup = BeautifulSoup(html,'html.parser')
    divs = soup.find_all(name='div',attrs={'class':'box-result clearfix'})
    print(divs)
    regex = re.compile('blk_result')
    for div in divs:
        try:
            if (regex.match(div[u'data-sudaclick'])):
               # print(div.h2.a['href'] + div.h2.a.name)
                map[div.h2.a] = div.h2.a['href']
                #list.append(div.h2.a['href'])
                #print(div.h2.a.name)
        except:
            pass
    for key,value in map.items():
        print(key)
        print(value)

#xinglang('食品安全',page=3)
from spiderFunction import get_html,get_response
def tag():
    url = 'http://tags.finance.sina.com.cn/%E9%A3%9F%E5%93%81%E5%AE%89%E5%85%A8'
    response = get_response(url)
    html = response.text
    print(html)
    soup =BeautifulSoup(html,'html.parser')
    for li in soup.find_all(name = 'li'):
        try :
            print(li['bid'])
        except:
            pass
tag()
