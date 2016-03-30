#encoding=utf-8
"""

"""
import urllib
import re
import os

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def get_img(html):
    reg = r'src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    filename='C:\\Users\\X250\\Desktop\\image'
    if  not os.path.exists(filename):
       os.makedirs(filename)

    i = 0
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl, filename+'\\%s.jpg'%i)
        i+=1
html = get_html('http://tieba.baidu.com/p/4417244123')
print get_img(html)