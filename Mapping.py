from djitellopy import tello
import KeyPressModule as kp
import cv2
import time
import winwifi
import numpy as np
import math

###### PARAMETERS ######
fSpeed = 117 / 10  # Forward Speed in cm/s (15cm/s)
aSpeed = 360 / 10  # Angular Speed Degrees/s
interval = 0.25
x, y = 500, 500
a = 0
yaw = 0
points = [(0, 0)]
dInterval = fSpeed * interval
aInterval = aSpeed * interval
########################


winwifi.WinWiFi.connect("TELLO-60679B")

kp.init()
me = tello.Tello()
me.connect()
# me.streamon()
print(me.get_battery())

global img
global lst_tm_img
lst_tm_img = time.time()


def getKeyboardInput():
    lr, fb, ud, yv, end = 0, 0, 0, 0, 0
    speed = 15
    aspeed = 50
    d = 0
    global x, y, yaw, a

    if kp.getKey("LEFT"):
        lr = -speed
        d = dInterval
        a = -180
    elif kp.getKey("RIGHT"):
        lr = speed
        d = -dInterval
        a = 180

    if kp.getKey("UP"):
        fb = speed
        d = dInterval
        a = 270

    elif kp.getKey("DOWN"):
        fb = -speed
        d = -dInterval
        a = -90

    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed

    if kp.getKey("a"):
        yv = -aspeed
        yaw -= aInterval
    elif kp.getKey("d"):
        yv = aspeed
        yaw += aInterval

    if kp.getKey("q"): me.land(); time.sleep(3);
    if kp.getKey("e"): me.takeoff()

    if kp.getKey("f"):
        if me.get_battery() > 50:
            me.flip("f");
            time.sleep(1)
        else:
            print("Cant Flip, Battery below 50%, Current Battery {}%.".format(me.get_battery()))

    if kp.getKey("x"): me.land(); time.sleep(3); end = 1

    if kp.getKey("z"):  # can take 1 pic per 1 sec
        cur_tm = time.time()
        global lst_tm
        if cur_tm - lst_tm > 1:
            cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
            lst_tm = cur_tm

    time.sleep(interval/2)
    a += yaw
    x += int(d * math.cos(math.radians(a)))
    y += int(d * math.sin(math.radians(a)))
    return [lr, fb, ud, yv, end]


def drawPoints(img, points):
    for point in points:
        cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, points[-1], 8, (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'({(points[-1][0] - 500)/ 100},{-1*(points[-1][1] - 500) / 100})m',
                (points[-1][0] + 10, points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 1)


while True:
    vals = getKeyboardInput()
    if vals[4] == 1:
        break
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    # img = me.get_frame_read().frame
    # img = cv2.resize(img, (240, 160))
    img = np.zeros((1000, 1000, 3), np.uint8)
    if points[-1] != (x, y):
        points.append((x, y))
    drawPoints(img, points)
    cv2.imshow("circle", img)
    cv2.waitKey(1)

# me.streamoff()
cv2.destroyWindow("Image")
winwifi.WinWiFi.connect("Diralselno")
# winwifi.WinWiFi.connect("yehezkel")
