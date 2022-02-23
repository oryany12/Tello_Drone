import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    cv2.imshow("WebCame", img)
    cv2.waitKey(1)


def findFace(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')