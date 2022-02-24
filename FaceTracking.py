import cv2
import numpy as np
from Global_params import *


def findFace(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imgGray, 1.2, 8)

    if len(faces) == 0:
        center = (img.shape[0] // 2, img.shape[1] // 2)
        face_size = FACE_SIZE
        return center, face_size

    max_area = 0
    indx = -1
    for i, (x, y, w, h) in enumerate(faces):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        if w * h > max_area:
            indx = i
            max_area = w * h

    x, y, w, h = faces[indx]
    center = (x + w // 2, y + h // 2)
    face_size = w * h
    cv2.circle(img, center, 5, (0, 255, 0), cv2.FILLED)

    return center, face_size


def trackFace(center, area, pError, img):
    cx, cy = center
    fb = 0
    error = cx - img.shape[0] // 2
    yv = PID[0] * error + PID[1] * (error - pError)
    yv = int(np.clip(yv, -20, 20))
    if area > FACE_SIZE_RANGE[1]:
        fb = -15
    elif area < FACE_SIZE_RANGE[0]:
        fb = 15

    return pError, [0, fb, 0, yv]


# cap = cv2.VideoCapture(0)
# pError = 0
# while True:
#     _, img = cap.read()
#     center, face_size = findFace(img)
#     pError, _ = trackFace(center, face_size, pError)
#     cv2.imshow("WebCame", img)
#     cv2.waitKey(1)
