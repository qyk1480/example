import urllib.request

#response=urllib.request.urlopen('http://placekitten.com/g/400/500')#()既可以是字符串，也可以是request的对象
req=urllib.request.Request('http://placekitten.com/g/400/500')
response=urllib.request.urlopen(req)

cat_img=response.read()

with open('520.jpg','wb') as f:
    f.write(cat_img)

'''
import urllib.request
response = urllib.request.urlopen('http://www.fishc.com')
html = response.read()
html = html.decode('utf-8')
print(html)
response.geturl()
response.info()
response.getcose()
'''
