#encoding=utf-8
"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
def convertWords(filename):
    content=[]
    enter=raw_input('Enter your words:')
    with open(filename) as f:
        for line in f:
            line=line.decode('utf8')
            word1=re.compile(u'[\u4e00-\u9fa5]+')
            word2=re.compile(r'[a-zA-Z]+')
            words=word1.findall(line)+word2.findall(line)
            for x in words:
                content.append(x)

    for x in content:
        if x in enter:
            return 'Freedom'

    return   'HumanRights'

if __name__=="__main__":
  print convertWords('words.txt')
