import urllib.request
import urllib.parse
import json
import time

while True:
    content=input("翻译内容('q!为退出)：")
    if content=='q!':
        break
    
    url='http://fanyi.youdao.com/translate'
    #url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
    '''
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    '''
    #修改headers
    data={}
    data['i']=content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    #data['salt']='1503919127021'
    #data['sign']='b62cc2896bec22f3ed3acacdaf108ace'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLICKBUTTION'
    data['typoResult']='true'
    data=urllib.parse.urlencode(data) .encode('utf-8')

    req=urllib.request.Request(url,data)
    #修改headers
    #req=urllib.request.Request(url,data，head)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')

    response=urllib.request.urlopen(req)
    html=response.read().decode('utf-8')

    target=json.loads(html)
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
    
    time.sleep(5)
