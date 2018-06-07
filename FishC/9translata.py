import urllib.request
import urllib.parse
import json

content=input("翻译内容：")

url='http://fanyi.youdao.com/translate'
#url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
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

response=urllib.request.urlopen(url,data)
html=response.read().decode('utf-8')

target=json.loads(html)
print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
