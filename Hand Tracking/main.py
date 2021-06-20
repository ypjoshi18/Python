import cv2
import mediapipe as mp
import time



cap = cv2.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils

# Frame Per Second
pTime = 0
cTime = 0

while True:
    ret, img = cap.read()
    imgBGR = cv2.cvtColor(img, cv2.COLOR_Luv2RGB)
    results = hands.process(imgBGR)
    print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)

                if id == 4:
                    cv2.circle(img, (cx, cy), 20,(255, 0, 255), cv2.FILLED )

            mpDraw.draw_landmarks(img, handlms, mphands.HAND_CONNECTIONS)


    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) == 13:
        break
cv2.destroyWindow()
