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




#apiOn = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=buttonon&announcement=Hello%20monkey"
#apiOff = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=buttonoff&announcement=Hello%20monkey"
#apifu = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=fu&announcement=Hello%20monkey"
#api1 = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=1&announcement=Hello%20monkey"
#api2 = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=2&announcement=Hello%20monkey"
#api3 = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=3&announcement=Hello%20monkey"
#api4 = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=4&announcement=Hello%20monkey"
#api5 = "https://api.voicemonkey.io/trigger?access_token=3581003073373c65e2999399ba5aae8e&secret_token=1f9f8395012086e240a4b056dfb33c68&monkey=5&announcement=Hello%20monkey"


# folderPath = "LightImages"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(f'{folderPath}/{imPath}')
#     overlayList.append(image)
# print(len(overlayList))
pTime = 0

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
    # coord = (lmList[9][1], lmList[9][2])
    # cy, cx = [i / 2 for i in img.shape[:-1]] if coord is None else coord[::-1]
    cx = lmList[9][1]
    cy = lmList[9][2]
    rot_mat = cv2.getRotationMatrix2D((cx, cy), angle, zoom)
    result = cv2.warpAffine(img, rot_mat, img.shape[1::-1], flags=cv2.INTER_LINEAR)

    return result


while True:
    success, img = cap.read()
    # gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # (thresh, img) = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    # print(lmList)

    if len(lmList) != 0:
            # img = zoom_at(img)

        # if lmList[8][2] < lmList[6][2]:
        #     print("Index finger open")
        # if lmList[8][2] > lmList[6][2]:
        #     print("Index finger close")

        # if lmList[12][2] < lmList[10][2]:
        #     if lmList[16][2] < lmList[14][2]:
        #         if lmList[8][2] > lmList[6][2]:
        #             if lmList[20][2] > lmList[18][2]:
        #                 apiCalloff = requests.get(apiOff)
                        # print("Light Off")
                        # print(apiCalloff)
        # if lmList[8][2] < lmList[6][2]:
        #     if lmList[20][2] < lmList[18][2]:
        #         if lmList[12][2] > lmList[10][2]:
        #             if lmList[16][2] > lmList[14][2]:
        #                 apiCallon = requests.get(apiOn)
                        # print("Light On")
                        # print(apiCallon)

            if index_down():
                if not middle_down():
                    if not ring_down():
                        if pinky_down():
                            apiCalloff = requests.get(apic.apiOff)
                            print("Light Off")
                            print(apiCalloff)
                            time.sleep(3)

            if not index_down():
                if middle_down():
                    if ring_down():
                        if not pinky_down():
                            apiCallon = requests.get(apic.apiOn)
                            print("Light On")
                            print(apiCallon)
                            time.sleep(3)


            # if index_down():
            #     if not middle_down():
            #         if ring_down():
            #             if pinky_down():
            #                 apiCallfu = requests.get(apifu)
            #                 print("fu")
            #                 print(apiCallfu)

            # # one (vol 3)
            # if not index_down():
            #     if middle_down():
            #         if ring_down():
            #             if pinky_down():
            #                 apiCall1 = requests.get(api1)
            #                 print("Vol 3")
            #                 print(apiCall1)
            #
            # # two (vol 5)
            # if not index_down():
            #     if not middle_down():
            #         if ring_down():
            #             if pinky_down():
            #                 apiCall2 = requests.get(api2)
            #                 print("Vol 5")
            #                 print(apiCall2)
            #
            # # three (vol 7)
            # if not index_down():
            #     if not middle_down():
            #         if not ring_down():
            #             if pinky_down():
            #                 apiCall3 = requests.get(api3)
            #                 print("Vol 7")
            #                 print(apiCall3)

            # # four (prev)
            # if not index_down():
            #     if not middle_down():
            #         if not ring_down():
            #             if not pinky_down():
            #                 if thumb_down():
            #                     apiCall4 = requests.get(api4)
            #                     print("Prev")
            #                     print(apiCall4)
            #
            #
            # # five (next)
            # if not index_down():
            #     if not middle_down():
            #         if not ring_down():
            #             if not pinky_down():
            #                 if thumb_down():
            #                     apiCall5 = requests.get(api5)
            #                     print("Next")
            #                     print(apiCall5)

    # h, w, c = overlayList[0].shape
    # img[0:h, 0:w] = overlayList[0]

#FPS
    # cTime = time.time()
    # fps = 1 / (cTime - pTime)
    # pTime = cTime

    # cv2.putText(img, str(int(fps)), (10, 25), cv2.FONT_HERSHEY_PLAIN, 1,
    #             (0, 128, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
