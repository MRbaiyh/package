import urllib.request
import requests
from bs4 import BeautifulSoup
import re
'''
def GetHTML(url,headers):
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    html = html.decode('gbk')
    f = open('yuanma.txt','wt')
    f.write(html)
'''


url= "http://www.aigaogao.com/tools/history.html?s="+input("查询的股票代码：")+"#04/"  #目标网址
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
t = requests.get(url)
t = t.text
soup = BeautifulSoup(t,'html.parser')
print(soup)

    