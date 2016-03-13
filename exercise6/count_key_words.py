import os
import re
from collections import Counter

def count_key_word(filepath):
    words_count=dict()
    for root,dirs,filenames in os.walk(filepath):
        for filename in filenames:
            c=Counter()
            if filename.endswith('txt'):
                f=open(os.path.join(root,filename))
                for line in f:
                    math=re.findall(r'[a-zA-Z\-]+',line)
                    for word in math:
                        c[word]=c[word]+1
            words_count[filename]=c
        return words_count

if __name__=="__main__":
    print count_key_word('diary')