#encoding:utf-8
"""
第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""
import os
import random
from PIL import Image
import shutil

def resetsize(filename):
    iphone_with=random.randint(500,640)
    iphone_height=random.randint(900,1136)
    listnames= os.listdir(filename)
    dirpath=os.path.abspath(filename)
    
    for im in listnames:
        path=os.path.join(dirpath,im)
        image=Image.open(path)
        image.resize((iphone_with,iphone_height),Image.ANTIALIAS)
        image.save('iphone5_'+im,'jpeg')
        shutil.move(dirpath.replace(os.path.basename(filename),'')+'\\iphone5_'+im,dirpath+'\\')

if __name__=='__main__':
    resetsize('iphone')
