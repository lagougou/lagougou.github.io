#encoding=utf-8
"""
第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，
则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""
import sys,re
reload(sys)
sys.setdefaultencoding("utf-8")

def replace_sensitive_words(filename):
    content=[]
    enter=unicode(raw_input('Enter your words:'))
    word1=re.compile(u'[\u4e00-\u9fa5]+')
    word2=re.compile(r'[a-zA-Z]+')
    with open(filename) as f:
        for line in f:
            line=line.decode('utf8')
            words=word1.findall(line)+word2.findall(line)
            for x in words:
                content.append(x)

    for x in content:
        a=0
        if x in enter:
            while True:
                index=enter.find(x,a)
                if index!=-1:
                    enter=enter[:index]+'*'*len(x)+enter[index+len(x):]   #一个汉字三个字节
                    a=a+1
                else:
                    break
            return enter
    return enter


if __name__=='__main__':
    print replace_sensitive_words('words.txt')

f=open('words.txt')
print f.read().split("\n")