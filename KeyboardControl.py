import KeyPressModule as kp
from Global_params import *

kp.init()


def getKeyboardInput():
    lr, fb, ud, yv, key_press = 0, 0, 0, 0, set()

    if kp.getKey("LEFT"):
        lr = -fSpeed
        key_press.add("LEFT")
    elif kp.getKey("RIGHT"):
        lr = fSpeed
        key_press.add("RIGHT")

    if kp.getKey("UP"):
        fb = fSpeed
        key_press.add("UP")
    elif kp.getKey("DOWN"):
        fb = -fSpeed
        key_press.add("DOWN")

    if kp.getKey("w"):
        ud = zSpeed
        key_press.add("w")
    elif kp.getKey("s"):
        ud = -zSpeed
        key_press.add("s")

    if kp.getKey("a"):
        yv = -aSpeed
        key_press.add("a")
    elif kp.getKey("d"):
        yv = aSpeed
        key_press.add("d")

    if kp.getKey("q"): key_press.add("q")
    if kp.getKey("e"): key_press.add("e")
    if kp.getKey("f"): key_press.add("f")
    if kp.getKey("x"): key_press.add("x")
    if kp.getKey("z"): key_press.add("z")
    if kp.getKey("b"): key_press.add("b")
    if kp.getKey("r"): key_press.add("r")



    return key_press, [lr, fb, ud, yv]
