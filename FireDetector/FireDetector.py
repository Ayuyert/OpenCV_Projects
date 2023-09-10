import cv2
import numpy as np

video = cv2.VideoCapture("ates.mp4")

while True:

    ret, frame2 = video.read()
    if ret == False:
         break
    frame = cv2.resize(frame2, (1280,720))
    blur = cv2.GaussianBlur(frame, (15,15),0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
    upper = [10,255,255]
    lower = [0,50,50]
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv,lower,upper)

    output = cv2.bitwise_and(frame,hsv, mask= mask)
    no_red = cv2.countNonZero(mask)
    cv2.imshow("output", output)

    if no_red > 200000:
        print("Fire detected")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
video.release()
