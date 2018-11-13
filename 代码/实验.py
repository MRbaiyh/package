class Tj:
    def __init__(self, text):
        for i in text:
            char = {',','.','/','(',')','/n'}
            if i in char:
                text = text.replace(i, '')
        self.new = text
    def textsplit(self):
        wordlist = self.new.split( )
        print(wordlist)
        dcnum = len(wordlist)
        print('该文本中的单词数为：%d'%(dcnum))
        norepwordl = list(set(wordlist))
        for i in range(len(norepwordl)):
            wordnum = wordlist.count(norepwordl[i])
            print('%s-在文本中出现的次数为:%d'%(norepwordl[i], wordnum))

stop = ''
content = ''
for i in iter(input,stop):
    content += i + '\n'
a = Tj(content)
a.textsplit()

import urllib.request
import urllib.parse
import json
 
def get_data(words):
    data = {}
    data["type"] = "AUTO"
    data["i"] = words
    data["doctype"] = "json"
    data["xmlVersion"] = "1.8"
    data["keyfrom:fanyi"] = "web"
    data["ue"] = "UTF-8"
    data["action"] = "FY_BY_CLICKBUTTON"
    data["typoResult"] = "true"
    data = urllib.parse.urlencode(data).encode('utf-8')
    return data
 
def url_open(url, data):
    req = urllib.request.Request(url, data)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    response = urllib.request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    return html
 
def get_json_data(html,words):
    result = json.loads(html)
    result = result['translateResult']
    print(result)
    list = words.split('.')
    print(list)
    r1 = ''
    for i in range(len(list)-1):
        r1 = r1 + result[0][i]['tgt']
    result = r1    
    return result
 
def main():
    words = input("请输入要翻译的内容: ")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"
 
    data = get_data(words)
    html = url_open(url, data)
    result = get_json_data(html,words)
    print("翻译结果为: %s" % result)

main()

stop = ''
str = ''
for i in iter(input,stop):
    str += i + '\n'
     