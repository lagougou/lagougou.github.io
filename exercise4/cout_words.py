# -*- coding: utf-8 -*-

""" 
python实现任一个英文的纯文本文件，统计其中的单词出现的个数、行数、字符数 
"""  

import re

file_name = 'words.txt'

lines_count = 0
words_count = 0
chars_count = 0

with open(file_name, 'r') as f:
    for line in f:
        lines_count = lines_count + 1
        chars_count  = chars_count + len(line)
        #找到只含字母或数字的单词
        match = re.findall(r'[a-zA-Z0-9]+', line)
        for i in match:
            words_count+=1


print 'words_count is', words_count
print 'lines_count is', lines_count
print 'chars_count is', chars_count