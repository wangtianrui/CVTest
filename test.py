import cv2
import numpy as np
import PIL as Image


def readImage(imagePath):
    image = cv2.imread(imagePath)
    return image

def showImage(image):
    cv2.imshow("image",image)

imagePath = "image/faceopen.jpg"
#读取
image = readImage(imagePath)
#resize
image = cv2.resize(image,(512,512))
#转灰度
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#gray = image
#转二值图
'''
threshold(src, thresh, maxval, type, dst=None)
src:image
thresh:阈值
maxval:在二元阈值THRESH_BINARY和逆二元阈值THRESH_BINARY_INV中使用最大值
type:使用的阈值类型
'''
ret,image = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

#边缘检测（划出边缘）
edged = cv2.Canny(image, 35, 125)
image = edged

#获取轮廓
contours,hierarchy,_=cv2.findContours(image,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image,contours,-1,(0,0,255),3)

#高斯模糊
#gaussianblur = cv2.GaussianBlur(image,(5,5),0)
#showImage(gaussianblur)

#showImage(contours)
#cv2.waitKey(0)
#showImage(image)
#showImage(contours[5])
print(len(contours))


for i in range(len(contours)):
    cnt = contours[i]
    print(cnt.shape)
    #cv2.imshow("image",cnt)
    #cv2.waitKey(0)
    #print(cv2.contourArea(cnt))

