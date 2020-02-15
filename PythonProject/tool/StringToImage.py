# -*- coding: utf-8 -*-
# @Time : 2020/2/13 17:46
# @Author : jjh
# @File : ImagePython.py
# @Software: PyCharm
# @contact: 469672930@qq.com
# -*- 功能说明 -*-
# 字符转图片
# -*- 功能说明 -*-
#pillow

from PIL import Image, ImageDraw, ImageFont
import os

font_size = 20
text = "我爱你哟!"
curPath = os.getcwd()
img_path = curPath + "//my.jpg"
img_our_path = curPath + "//save.jpg"

img_raw = Image.open(img_path)
img_array = img_raw.load()

img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)

def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

img_new.convert('RGB').save(img_our_path)