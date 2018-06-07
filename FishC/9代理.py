import urllib.request
import random
url='http://www.whatismyip.com.tw'

iplist=['221.224.166.2:8080','59.110.221.78:80','116.52.134.5:9999']
proxy_support=urllib.request.ProxyHandler({'http':random.choice(iplist)})

opener=urllib.request.build_opener(proxy_support)
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')

print(html)
