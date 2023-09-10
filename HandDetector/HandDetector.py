import cv2
import mediapipe as mp


mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.75,
    max_num_hands = 2)

cap = cv2.VideoCapture(0)
counter = 0
printlist = []
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        if len(results.multi_handedness) == 2:
            for hand_landmarks in results.multi_hand_landmarks:
                for ids, landmrk in enumerate(hand_landmarks.landmark):
                    counter = counter + 1
                    if counter == 3 or counter == 21:
                        cx, cy = landmrk.x, landmrk.y
                        printlist.append((cx * cap.get(cv2.CAP_PROP_FRAME_WIDTH), cy * cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                print(int(printlist[1][0]))
                img = cv2.rectangle(img, (int(printlist[0][0]), int(printlist[0][1])),
                                    (int(printlist[1][0]), int(printlist[1][1])), (222, 0, 0), 5)
                counter = 0
                printlist = []

        else:
            hand_landmarks = results.multi_hand_landmarks[0]
            for ids, landmrk in enumerate(hand_landmarks.landmark):
                counter = counter+1
                if counter == 3 or counter == 21:
                    cx, cy = landmrk.x, landmrk.y
                    printlist.append((cx*cap.get(cv2.CAP_PROP_FRAME_WIDTH),cy*cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            print(int(printlist[1][0]))
            img = cv2.rectangle(img,(int(printlist[0][0]),int(printlist[0][1])),(int(printlist[1][0]),int(printlist[1][1])), (222,0,0),5)
            counter = 0
            printlist = []


    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
