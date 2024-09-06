import cv2
import mediapipe as mp
import time

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture("video1.mp4")

pTime = 0

while True:
    succes, img = cap.read()
    if not succes:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)


            if id in (13, 14):
                cv2.circle(img, (cx, cy), 9, (0, 255, 175), cv2.FILLED)


    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, "Fps :" + str(int(fps)), (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))

    cv2.imshow("img", img)
    k = cv2.waitKey(33) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
