import re
import requests
import json


html = requests.get('http://so.news.cn/getNews?keyword=%E9%A3%9F%E5%93%81%E5%AE%89%E5%85%A8&curPage=4&sortField=0&searchFields=1&lang=cn').text
print(html)
regex = re.compile(r'^"url"')
list = re.findall(regex,html)
print(list)
j = json.loads(html)
for obj in j['content']['results']:
    print(obj['title']+'  '+obj['url'])
print(j)