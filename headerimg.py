#!usr/bin/python
#coding=utf-8

import qrcode
import PIL
import datetime

if __name__ == '__main__':
    blog_url = 'fku'

    #初始化二维码生成器  version 代表大小  1为12*12 每大1表示加4像素 qrcode.constants.ERROR_CORRECT_H为校正级别  这里是30%
    code_maker = qrcode.QRCode(version=5,error_correction=qrcode.constants.ERROR_CORRECT_H)
    #填入在二维码中保存的数据
    code_maker.add_data(blog_url)
    #fit为true时，不设定version可以自动设置大小
    code_maker.make(fit=True)
    #创建图像
    code_image = code_maker.make_image()
    #转成RGB图像
    code_image = code_image.convert('RGBA')
    #打开头像图片
    face_image = PIL.Image.open('img.jpg')

    #获取头像图片大小
    code_width, code_height = code_image.size
    #缩放，并打开抗锯齿
    face_image = face_image.resize((100,100), PIL.Image.ANTIALIAS)

    #将头像嵌入二维码当中
    code_image.paste(face_image, ((code_width-100)/2, (code_height-100)/2))
    now_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code_image.save(now_time+'.png')
