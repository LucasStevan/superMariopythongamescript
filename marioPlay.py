import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller

#jogo do mario
#https://www.jogosfas.com/jogo/super-mario-world-eua

kb = Controller()
cap = cv2.VideoCapture(0)

pp=mp.solutions.pose
pose = mp.solutions.pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)

mpDwaw = mp.solutions.drawing_utils

while True:
    cap.set(10, 175)
    success, img = cap.read()
    frameRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(frameRGB)
    points = results.pose_landmarks
    h, w, _ = img.shape

    if points:
        mpDwaw.draw_landmarks(img,points,pp.POSE_CONNECTIONS)

        cotoveloL = points.landmark[pp.PoseLandmark.LEFT_ELBOW].y*h
        maoL = points.landmark[pp.PoseLandmark.LEFT_INDEX].y * h

        cotoveloR = points.landmark[pp.PoseLandmark.RIGHT_ELBOW].y*h
        maoR = points.landmark[pp.PoseLandmark.RIGHT_INDEX].y * h

        for id, lm in enumerate(points.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)

            #print(f'mao: {mao}')
            #print(f'cotovelo: {cotovelo}')

            #cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
            #abaixando
            if id ==0 and cy < (h/2):
                #print('normal')
                kb.release(Key.down)
                #continue
            if id == 0 and cy > (h/2):
                #print('abaixou')
                kb.press(Key.down)
                #continue
            #pulando
            if id == 24 and cy < ((h/2)+130):
                #print('pulou')
                kb.press('x')
                #continue
            if id == 24 and cy > ((h/2)+130):
                #print('normal')
                kb.release('x')
                #continue
            #andando braço esquerdo
            if maoL > cotoveloL:
                #print('normal')
                kb.release(Key.right)
                #continue
            if maoL < cotoveloL:
                #print('andando')
                kb.press(Key.right)
                #continue
            # andando braço esquerdo
            if maoR > cotoveloR:
                #print('normal')
                kb.release(Key.right)
                #continue
            if maoR < cotoveloR:
                #print('andando')
                kb.press(Key.right)
                #continue

    cv2.line(img, (0, int(h/2)), (w, int(h/2)), (255, 0, 255),1) #linha meia tela
    cv2.line(img, (0, int(h / 2)+130), (w, int(h / 2)+130), (0, 0, 255), 1) #linha para pular
    #cv2.line(img, (0, int(h / 2) + 230), (w, int(h / 2) + 230), (0, 0, 255), 1)  # linha para andar

    cv2.imshow("Results",img)
    cv2.waitKey(1)

# if id ==20:
#     mao = cy
#     #cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
#     #print(f'mao: {cy}')
# if id ==14:
#     cotovelo = cy
#     #cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
#     #print(f'cotovelo: {cy}')
#


# if id ==19:
#     mao = cy
#     print(f'mao: {mao}')
# if id ==13:
#     cotovelo = cy
#     print(f'cotovelo: {cotovelo}')