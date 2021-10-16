from djitellopy import tello
import KeyPressModule as kp
import cv2
import time
import winwifi
import numpy as np

###### PARAMETERS ######
fSpeed = 117 / 10  # Forward Speed in cm/s (15cm/s)
aSpeed = 360 / 10  # Angular Speed Degrees/s
interval = 0.25

dInterval = fSpeed * interval
aInterval = aSpeed * interval
########################


winwifi.WinWiFi.connect("TELLO-60679B")

kp.init()
me = tello.Tello()
me.connect()
me.streamon()
print(me.get_battery())

global img
global lst_tm
lst_tm = time.time()


def getKeyboardInput():
    lr, fb, ud, yv, end = 0, 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed

    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -speed
    elif kp.getKey("d"):
        yv = speed

    if kp.getKey("q"): me.land(); time.sleep(3); end = 1
    if kp.getKey("e"): me.takeoff()

    if kp.getKey("f"):
        if me.get_battery() > 50:
            me.flip("f")
        else:
            print("Cant Flip, Battery below 50%, Current Battery {}%.".format(me.get_battery()))

    if kp.getKey("z"):  # can take 1 pic per 1 sec
        cur_tm = time.time()
        global lst_tm
        if cur_tm - lst_tm > 1:
            cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
            lst_tm = cur_tm
    return [lr, fb, ud, yv, end]


def drawPoints():
    cv2.circle(img, (300, 500), 20, (0, 0, 255), cv2.FILLED)


while True:
    vals = getKeyboardInput()
    if vals[4] == 1: break
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000, 1000, 3), np.uint8)
    drawPoints()
    cv2.imshow("Output", img)
    cv2.waitKey(1)

winwifi.WinWiFi.connect("Diralhaskir")
