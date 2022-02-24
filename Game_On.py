from Global_params import *
import winwifi
from djitellopy import tello
from KeyboardControl import getKeyboardInput
import time
import cv2
from Mapping import Map
from FaceTracking import findFace, trackFace

### SETUP ###
winwifi.WinWiFi.connect(TELLO_WIFI)
me = tello.Tello()
me.connect()
print(f'Current Battery {me.get_battery()}%.')
lst_tm_img = time.time()
if STREAM_VIDEO: me.streamon()
if SHOW_MAP: map_obj = Map()
tracking = False
pError = 0


def PowerOF():
    if STREAM_VIDEO:
        me.streamoff()
        cv2.destroyWindow(STREAM_NAME)
    if me.is_flying: me.land()


### Running ###
while True:
    stream = me.get_frame_read().frame
    stream = cv2.resize(stream, STREAM_SIZE)
    key_press, next_cntrl = getKeyboardInput()

    if tracking and len(key_press) == 0:
        center, face_size = findFace(stream)
        pError, next_cntrl = trackFace(center, face_size, pError, stream)

    me.send_rc_control(*next_cntrl)
    print(next_cntrl)

    if STREAM_VIDEO:
        cv2.imshow(STREAM_NAME, stream)
        cv2.waitKey(1)

    if SHOW_MAP:  # TODO: change this section so it will show changes in the map also for facetrack
        # TODO: (propably only the func "next_potion" deliover to the func velocity and not key_press
        map_obj.next_position(key_press)
        map_img = map_obj.drawPoints()
        cv2.imshow(MAP_NAME, map_img)
        cv2.waitKey(1)

    time.sleep(INTERVAL)

    if "q" in key_press:
        me.land()
        time.sleep(3)
    if "e" in key_press:
        me.takeoff()
        time.sleep(1)
    if "f" in key_press:
        if me.get_battery() > MIN_BATTERY_FLIP:
            me.flip("f")
            time.sleep(1)
        else:
            print(f'Cant Flip, Battery below {MIN_BATTERY_FLIP}%, Current Battery {me.get_battery()}%.')
    if "z" in key_press:  # can take 1 pic per 1 sec
        cur_tm = time.time()
        if cur_tm - lst_tm_img > 1:
            cv2.imwrite(f'Resources/Images/{time.time()}.jpg', me.get_frame_read().frame)
            lst_tm_img = cur_tm
    if "x" in key_press:
        PowerOF()
        break
    if "b" in key_press: print(f'Current Battery {me.get_battery()}%.')
    if "r" in key_press:
        if SHOW_MAP:
            map_obj.x, map_obj.y = map_obj.x_start, map_obj.y_start
            map_obj.Points = [(map_obj.x, map_obj.y)] * TRAIL
            map_obj.a = map_obj.yaw = 0
    if "t" in key_press:
        tracking = not tracking
        if tracking: print("Tracking is ON")
        else: print("Tracking is OFF")
        time.sleep(1)
me.end()
winwifi.WinWiFi.connect(HOME_WIFI)
