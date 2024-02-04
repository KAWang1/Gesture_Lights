import cv2
import time
import os
import requests
import HandTrackingModule as htm
import ApiConfig as apic


wCam, hCam = 640, 488

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)


detector = htm.handDetector(detectionCon=0.75)

def thumb_down():
    if lmList[4][1] > lmList[3][1]:
        return True
    else:
        return False

def index_down():
    if lmList[8][2] > lmList[6][2]:
        return True
    else:
        return False

def middle_down():
    if lmList[12][2] > lmList[10][2]:
        return True
    else:
        return False

def ring_down():
    if lmList[16][2] > lmList[14][2]:
        return True
    else:
        return False
def pinky_down():
    if lmList[20][2] > lmList[18][2]:
        return True
    else:
        return False


def zoom_at(img, zoom=3, angle=0):
    cx = lmList[9][1]
    cy = lmList[9][2]
    rot_mat = cv2.getRotationMatrix2D((cx, cy), angle, zoom)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

    return result


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    # print(lmList)

    if len(lmList) != 0:

            if index_down():
                if not middle_down():
                    if not ring_down():
                        if pinky_down():
                            apiCalloff = requests.get(apic.apiOff)
                            print("Light Off")
                            print(apiCalloff)
                            #time.sleep(3)

            if not index_down():
                if middle_down():
                    if ring_down():
                        if not pinky_down():
                            apiCallon = requests.get(apic.apiOn)
                            print("Light On")
                            print(apiCallon)
                            #time.sleep(3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
