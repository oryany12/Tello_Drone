from Global_params import *
import winwifi
from djitellopy import tello
from KeyboardControl import getKeyboardInput
import time
import cv2


### SETUP ###
winwifi.WinWiFi.connect(TELLO_WIFI)
me = tello.Tello()
me.connect()
lst_tm_img = time.time()
if STREAM_VIDEO: me.streamon()
print(f'Current Battery {me.get_battery()}%.')


def PowerOF():
    if STREAM_VIDEO:
        me.streamoff()
        cv2.destroyWindow(STREAM_NAME)
    if me.is_flying: me.land()


### Running ###
while True:

    key_press, next_cntrl = getKeyboardInput()

    me.send_rc_control(*next_cntrl)

    if STREAM_VIDEO:
        img = me.get_frame_read().frame
        img = cv2.resize(img, (360, 240))
        cv2.imshow(STREAM_NAME, img)
        cv2.waitKey(1)

    if key_press == "q":
        me.land()
        time.sleep(3)
    if key_press == "e": me.takeoff()
    if key_press == "f":
        if me.get_battery() > MIN_BATTERY_FLIP:
            me.flip("f")
            time.sleep(1)
        else:
            print(f'Cant Flip, Battery below {MIN_BATTERY_FLIP}%, Current Battery {me.get_battery()}%.')
    if key_press == "x":
        me.land()
        PowerOF()
        break
    if key_press == "z":  # can take 1 pic per 1 sec
        cur_tm = time.time()
        if cur_tm - lst_tm_img > 1:
            cv2.imwrite(f'Resources/Images/{time.time()}.jpg', me.get_frame_read().frame)
            lst_tm_img = cur_tm

me.end()
winwifi.WinWiFi.connect(HOME_WIFI)
