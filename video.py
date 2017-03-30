import time
import cv2
fourcc = cv2.cv.CV_FOURCC(*'XVID')
flag = 0
camera = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (320,240))
camera.set(3,320)
camera.set(4,240)

firstFrame = None
skipFrame = 0
task = "test1"
while True:
    (grabbed, frame) = camera.read()
    text ="Unoccupied"

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        if skipFrame > 15:
            firstFrame = gray

        text = "waiting"
        cv2.putText(frame, "RoomStatus: {}".format(text), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
        cv2.imshow(task, frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        skipFrame += 1
        continue

    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 25,255, cv2.THRESH_BINARY)[1]
    cv2.imshow('test4', thresh)
    thresh = cv2.dilate(thresh, None, iterations = 2)
    (contours, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 500:
            continue
        else:
            flag = 1
            task = "Recording"
        (x,y,w,h) = cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0),2)
        text = "Occupied"
    if flag  == 1:
        out.write(frame)
    cv2.putText(frame, "Room Status: {}".format(text), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    cv2.imshow(task, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
out.release()
cv2.destroyAllWindows()

