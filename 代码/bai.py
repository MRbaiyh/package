import urllib.request
import urllib.parse
import json
#方法get_data()
def get_data(words):
    #定义字典data，将要翻译的内容words放入其中
    data = {}
    data["type"] = "AUTO"
    data["i"] = words
    data["doctype"] = "json"
    data["xmlVersion"] = "1.8"
    data["keyfrom:fanyi"] = "web"
    data["ue"] = "UTF-8"
    data["action"] = "FY_BY_CLICKBUTTON"
    data["typoResult"] = "true"
    #利用urllib.parse.urlencode()对data进行处理，将其变成url编码格式
    data = urllib.parse.urlencode(data).encode('utf-8')
    return data
#方法url_open() 
def url_open(url, data):
    #利用urllib.request发送请求，打开网址传入数据data
    req = urllib.request.Request(url, data)
    #定义一个header进行浏览器伪装
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36")
    #获取request的结果
    response = urllib.request.urlopen(req)
    #对获取的内容进行读取
    html = response.read()
    #对获取内容解码
    html = html.decode("utf-8")
    return html
#方法get_json_data
def get_json_data(html,words):
    #运用模块json的函数loads对html进行解码，将其转换为python可读的字段
    result = json.loads(html)
    #获取result中translateResult对应的内容
    result = result['translateResult']
    #查看此时result，方便对翻译的内容进行获取
    #print(result)
    r1 = ''
    #查看result发信翻译内容可能被分割成几段，所以运用循环将其逐一获取，运用字符串连接连接在一起
    for i in range(len(result[0])):
        r1 = r1 + result[0][i]['tgt']
    result = r1    
    #返回最后的翻译内容
    return result
#方法main()输入翻译内容，设定url
def main():
    words = input("请输入要翻译的内容: ")
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"
    #调用方法get_data
    data = get_data(words)
    #调用方法url_open
    html = url_open(url, data)
    #调用方法get_json_data
    result = get_json_data(html,words)
    #输出结果
    print("翻译结果为: %s" % result)

main()