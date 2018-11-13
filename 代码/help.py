import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

#方法url_open() 
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")

    response = urllib.request.urlopen(req)
    html = response.read()
    return html
def get_data(html):
    soup = BeautifulSoup(html,'html.parser')
    file = open('GP.txt','wt')
    file.write(soup.find('a').text)
def main():
    url = "http://www.aigaogao.com/tools/history.html?s="+input("查询的股票代码：")+"#04/"
    html = url_open(url)
    get_data(html)
    #输出结果
    #print("翻译结果为: %s" % result)

main()
