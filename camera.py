#!usr/bin/python
#coding=utf-8

#导入库
import cv2
import pyzbar.pyzbar as pyzber

camera=cv2.VideoCapture(0)
def getdata(gray,image):
    #读取器读取二维码
    datalist=pyzber.decode(gray)
    for i in datalist:
        #获取定位
        (x,y,w,h)=i.rect
        #画框
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        #获取数据及类型
        data=i.data.decode("utf-8")
        datatype=i.type
        print "data:%s,type:%s"%(data,datatype)
        #写字
        cv2.putText(image,data,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),3)
    return image

while(True):
    _,img=camera.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=getdata(gray,img)
    cv2.imshow("img",img)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
camera.release()
cv2.destroyAllWindows()
