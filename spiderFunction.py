import requests
from bs4 import BeautifulSoup
import re


def get_response(url):
    headers = {
        'User-Angent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    try:
        respone = requests.get(url,headers = headers)
        respone.raise_for_status()
        respone.encoding = respone.apparent_encoding
        return respone
    except:
        print("error")

def get_html(head_url,page):
    url = str(head_url) + '&page='+ str(page)
    response = get_response(url)
    return  response.text

def get_url_list(html):
    soup = BeautifulSoup(html,'html.parser')
    list = []
    regex = re.compile('blk_result')
    for div in soup.find_all(name='div',attrs={'class':'box-result clearfix'}):
        try:
            if(regex.match(div[u'data-sudaclick'])):
                list.append(div.h2.a['href'])
        except:
            pass
    return list

def get_url_set(html):
    soup = BeautifulSoup(html,'html.parser')
    my_set = set()
    regex = re.compile('blk_result')
    for div in soup.find_all(name='div',attrs={'class':'box-result clearfix'}):
        try:
            if(regex.match(div[u'data-sudaclick'])):
                my_set.add(div.h2.a['href'])
        except:
            pass
    print('爬取数：'+ str(my_set.__len__()))
    print(my_set)
    return my_set
def newsParser(url):
    res = get_response(url)
    soup = BeautifulSoup(res.text,'html.parser')

    try:
        title = re.search(r'<h1 class="main-title"></i>(.)+</h1>',res.text)
        if title != None:
            title = re.split(r'</i>',str(title))[1]
            title = re.split(r'>',title)[0]
            try:
                title = re.sub(r'<.{0,3}$','',title)
            except:
                pass
        else:
            title = soup.find('h1',{'class':'main-title'}).string
        if title == None:
            print('title is null')


        time = soup.find(name='span',attrs={'class':'date'}).string
        #print(time)
        print(title)
        s = ''
        for p in soup.find_all('p'):
            try:
                s+=p.string
                #print(p.string)
            except:
                pass
        print(s)
        oneNews = [title,time,s]
        return oneNews
    except:

        print('parser_pass'+ '  '+ url)
        return None


def main():
    head_url = 'https://search.sina.com.cn/?q=%CA%B3%C6%B7%B0%B2%C8%AB&range=title&c=news&sort=time&col=&source=&from=&country=&size=&time=&a=&pf=2131425434&ps=2134309112&dpc=1'
    page_range = 5
    url_list = []
    url_set = set()
    for i in range(1,page_range+1):
        html = get_html(head_url,i)
        my_list = get_url_list(html)
        my_set = get_url_set(html)
        url_set.update(my_set)
        url_list.extend(my_list)
        print("第"+str(i)+"页的url爬取完成")
    for item in list(url_set):
        print(item)
    print('共爬取'+ str(url_set.__len__()) + "条url")
    print('----------------------------------------')
    for item in url_list:
        print(item)
    print('共爬取' + str(url_list.__len__()) + "条url")


    print("列表重复率" + str(1-(set(url_list).__len__()/url_list.__len__())))
    news = []
    for u in list(url_set):
        one_new = newsParser(u)
        if one_new != None:
            news.append(one_new)
            print(one_new)
main()
#newsParser('http://dl.sina.com.cn/news/2019-03-06/detail-ihrfqzkc1551167.shtml')