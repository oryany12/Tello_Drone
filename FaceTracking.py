import cv2
import numpy as np
from Global_params import *
import math


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


def trackFace(center, area, img, cntrl_pError):
    cx, cy = center
    fb = 0
    ud = 0
    error_ud = 0
    error_fb = 0
    error_lr = cx - img.shape[0] // 2
    yv = PID[0] * error_lr + PID[1] * (error_lr - cntrl_pError[3])
    yv = int(np.clip(yv, -aSpeed_track, aSpeed_track))

    if area > FACE_SIZE_RANGE[1]:
        fb = -fSpeed_track
    elif area < FACE_SIZE_RANGE[0]:
        fb = fSpeed_track

    # else:
    #     error_ud = cy - img.shape[1] // 2
    #     ud = PID[0] * error_ud + PID[1] * (error_ud - cntrl_pError[2])
    #     ud = int(np.clip(ud, -zSpeed_track, zSpeed_track))

    return [0, error_fb, error_ud, error_lr], [0, fb, ud, yv]

# cap = cv2.VideoCapture(0)
# pError_lr = 0
# while True:
#     _, img = cap.read()
#     center, face_size = findFace(img)
#     pError_lr, _ = trackFace(center, face_size, pError_lr)
#     cv2.imshow("WebCame", img)
#     cv2.waitKey(1)
