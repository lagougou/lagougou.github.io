#encoding:utf-8
"""
第 0008 题：一个HTML文件，找出里面的正文。
"""
from bs4 import BeautifulSoup
import urllib


f=urllib.urlopen('http://www.vistastory.com/a/201603/47965.html')
soup=BeautifulSoup(f,"html.parser")
print soup.get_text()
for i in soup.find_all('a'):
    print i['href']
