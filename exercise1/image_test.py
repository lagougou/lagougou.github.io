#coding='utf8'
from PIL import Image,ImageDraw,ImageFont

image=Image.open('origin.jpeg')                    #打开图片，获取图片对象
width,height=image.size                         #获取图片大小
draw=ImageDraw.Draw(image)                      #获得draw实例
fillColor='#ff0000'                             #设置颜色
font=ImageFont.truetype('C:/windows/fonts/Arial.ttf',30)   #设置字体格式和大小
draw.text((width-35,0),'99',fill=fillColor,font=font)          #设置文本内容和位置
image.save('result.jpg','jpeg')                                #保存图片



