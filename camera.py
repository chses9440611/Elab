#!/usr/bin/python
import cv2 as CV
import cv2.cv as cv
import time

cv.NamedWindow("camera", 1)
capture = cv.CaptureFromCAM(0)

#set solution of camera
cv.SetCaptureProperty(capture, 3, 400)
cv.SetCaptureProperty(capture, 4, 300)

while True:
    img = cv.QueryFrame(capture)

    #smooth 
    cv.Smooth(img, img, cv.CV_BLUR, 3)
    #hue_img = cv.CreateImage(cv.GetSize(img), 8 , 3)
    rows, cols = cv.GetSize(img)
    tmp_image = cv.fromarray(img)
    rotate_img = cv.GetRotationMatrix2D((cols / 2, rows / 2), 90, 1, tmp_image)
    #rotate_img = CV.warpAffine(,tmp_img, (cols,rows))
    #cv.CvtColor(img, hue_img, cv.CV_BGR2HSV)
    #threshold_img = cv.CreateImage(cv.GetSize(hue_img), 8 ,1)
    #cv.InRangeS(hue_img, (38,120,60), (75,255,255), threshold_img)


    cv.ShowImage("camera_origin", img)
    cv.ShowImage("Threshold", rotate_img)
    #as put ESC end the program
    if cv.WaitKey(10) == 27:
        break
cv.DestroyAllWindows()
