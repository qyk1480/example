#re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])','192.168.1.1')
import urllib.request
import os

def url_open(url):
    req=urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')
    response=urllib.request.urlopen(req)
    html=response.read()

    print(url)
    return html

def get_page(url):
    html=url_open(url).decode('utf-8')

    a=html.find('current-comment-page')+23
    b=html.find(']',a)

    print(html[a:b])

    return html[a:b]



def find_imgs(url):
    html=url_open(url).decode('utf-8')
    img_addrs =[]

    a = html.find('img src=')
    
    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            addr=html[a+9:b+4]
            img_addrs.append(addr)
        else:
            b = a + 9
    
        a = html.find('img src=',b)
    
    for each in img_addrs:
        print(each) 

    return img_addrs


def save_imgs(folder,img_addrs):
    for each in img_addrs:
        filename=each.split('/')[-1]
        with open(filename,'wb') as f:
            img=url_open(each)
            f.write(img)


def down_mm(folder='MM',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url='http://jandan.net/ooxx/'
    
    page_num=int(get_page(url))

    for i in range(pages):
        page_num -=i
        page_url=url+'page-'+str(page_num) + '#comments'
        img_addrs=find_imgs(page_url)
        save_imgs(folder,img_addrs)

if __name__=='__main__':
    down_mm()




