import requests
def translate(str):
    url = 'https://fanyi.baidu.com/#en/zh/'+ str
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        html = response.text
        print(html)
    except:
        print("连接错误")
def weiboImg():

    print( requests.get('//img.t.sinajs.cn/t4/appstyle/expression/ext/normal/a1/2018new_doge02_org.png').content)

def new():
    res = requests.get('http://dl.sina.com.cn/news/2019-03-06/detail-ihrfqzkc1551167.shtml')
    res.encoding = res.apparent_encoding
    html = res.text
    print(html)
new()