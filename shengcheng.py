#!usr/bin/python3
#coding=utf-8

import qrcode
import cv2
import datetime

print "Speak You will tell's talk"
#get input
txt=raw_input();
#write into image
img=qrcode.make(txt)
#save the image
now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
img.save("./"+now_time+".png")
img=cv2.imread("./"+now_time+".png")
#不要用中文  你会后悔的。。
cv2.imshow("img",img)
cv2.waitKey(0)
