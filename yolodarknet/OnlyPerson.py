import cv2 as cv

net = cv.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')


model = cv.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)


cap = cv.VideoCapture("output.avi")
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    classes, scores, boxes = model.detect(frame, 0.0001, 0.4)
    for (classid, score, box) in zip(classes, scores, boxes):
        color = (255,255,0)

        if(classid == 0):
            cv.rectangle(frame, box, color, 1)
            cv.putText(frame, "person", (box[0], box[1]-10),
                   cv.FONT_HERSHEY_COMPLEX, 0.3, color, 1)
    cv.imshow('frame', frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
