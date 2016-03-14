#encoding:utf-8
"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
import re

def count_lines(filename):
    total_line=0
    space_white_line=0
    description_line=0
    with open(filename) as f:
        for line in f:
            print line
            total_line=total_line
            if line=='\n':
                space_white_line+=1
            if "#" in line:
                description_line+=1


    print "common_line is ",total_line
    print "space_white_line is ",space_white_line
    print "description_line is",description_line

count_lines('test.py')
