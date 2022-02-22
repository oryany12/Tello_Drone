import KeyPressModule as kp
from Global_params import *

kp.init()
def getKeyboardInput():
    lr, fb, ud, yv, key_press = 0, 0, 0, 0, None

    if kp.getKey("LEFT"):
        lr = -SPEED
    elif kp.getKey("RIGHT"):
        lr = SPEED

    if kp.getKey("UP"):
        fb = SPEED
    elif kp.getKey("DOWN"):
        fb = -SPEED

    if kp.getKey("w"):
        ud = SPEED
    elif kp.getKey("s"):
        ud = -SPEED

    if kp.getKey("a"):
        yv = -SPEED
    elif kp.getKey("d"):
        yv = SPEED

    if kp.getKey("q"): key_press = "q"
    if kp.getKey("e"): key_press = "e"
    if kp.getKey("f"): key_press = "f"
    if kp.getKey("x"): key_press = "x"
    if kp.getKey("z"): key_press = "z"

    return key_press, [lr, fb, ud, yv]

