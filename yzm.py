#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from PIL import Image,ImageDraw,ImageFont
import random
def random_color():
    return (random.randint(110,255),random.randint(110,255),random.randint(110,255))
def random_color2():
    return (random.randint(0,110),random.randint(0,110),random.randint(0,110))
def random_zm_sz():
    i=random.randint(1,3)
    if i==1:
        return chr(random.randint(65,90))
    elif i==2:
        return chr(random.randint(97,122))
    else:
        return chr(random.randint(48,57))

def draw():
    wigth=30*4
    height=30
    image=Image.new('RGB',(wigth,height),(255,255,255))
    font=ImageFont.truetype('DejaVuSans.ttf',18)
    draw=ImageDraw.Draw(image)
    for x in range(wigth):
        for y in range(height):
            draw.point((x,y),fill=random_color())
    str=[]
    for i in range(4):
        str1=random_zm_sz()
        str.append(str1)
    for j in range(4):
        draw.text((30*j+8,8),str[j],font=font,fill=random_color2())

    image.save('/home/king/Desktop/yhxt/static/picture/yzm.jpg','JPEG')
    return str

if __name__=='__main__':
    list1=draw()