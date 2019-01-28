#!/usr/bin/python
#coding:utf-8
from sys import argv
import zbar
import Image
import cv2


input=raw_input()
#图片路径
img_file=input
# 创建一个读取器
scanner = zbar.ImageScanner()
# 配置读取器为启动
scanner.parse_config('enable')
# 读取灰度图像
img=cv2.imread(img_file)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
pil=Image.fromarray(img)
#pil=Image.open(img_file).convert('L')
#大小
width=img.shape[0]
height=img.shape[1]
#width, height = pil.size
#转换成bytes数据
raw=pil.tobytes()
#raw = img.data
#构建zbar图像 Y800代表Gray图像
image = zbar.Image(width, height, 'Y800', raw)
#读取图片
scanner.scan(image)
# 循环所有二维码中的信息
for symbol in image:
    # do something useful with results
    print 'data:', '"%s"' % symbol.data
 
# clean up
del(image)
