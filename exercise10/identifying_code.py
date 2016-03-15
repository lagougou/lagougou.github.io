#encoding=utf-8
"""
第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

"""
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

def random_char():
    return chr(random.randint(65,90))

def random_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def random_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def generate_code():
    width=60*4
    height=60

    image=Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('C:/windows/fonts/Arial.ttf', 40)

    draw=ImageDraw.Draw(image)

    for i in range(width):
        for j in range(height):
            draw.point((i,j),fill=random_color())

    for x in range(4):
        draw.text((x*height+15,10),random_char(),fill=random_color2(),font=font)

    image=image.filter(ImageFilter.BLUR)
    image.save('code.jpg','jpeg')

if __name__=='__main__':
    generate_code()

