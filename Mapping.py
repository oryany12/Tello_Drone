import math
from Global_params import *
import cv2
import numpy as np


class Map:
    def __init__(self):
        self.x, self.y = MAP_SIZE[0] // 2, MAP_SIZE[1] // 2
        self.x_start, self.y_start = MAP_SIZE[0] // 2, MAP_SIZE[1] // 2
        self.a = 0  # angle
        self.yaw = 0
        self.Points = [(self.x, self.y)]

    def drawPoints(self):
        map_img = np.zeros(MAP_SIZE, np.uint8)
        for point in self.Points:
            cv2.circle(map_img, point, RADIUS_POINT, COLOR_POINT, cv2.FILLED)
        cv2.circle(map_img, self.Points[-1], RADIUS_LEAD_POINT, COLOR_LEAD_POINT, cv2.FILLED)
        cv2.putText(map_img, f'({(self.Points[-1][0]-self.x_start) / 100},{(self.Points[-1][0]-self.y_start) / 100}m',
                    (self.Points[-1][0] + 10, self.Points[-1][1] + 30), cv2.FONT_HERSHEY_PLAIN, 1,
                    COLOR_TEXT, 1)
        return map_img

    def next_position(self, key_press):
        d = 0  # distance
        if "LEFT" in key_press:
            d = dInterval
            self.a = -180

        elif "RIGHT" in key_press:
            d = -dInterval
            self.a = 180

        if "UP" in key_press:
            d = dInterval
            self.a = 270

        elif "DOWN" in key_press:
            d = -dInterval
            self.a = -90

        if "a" in key_press:
            self.yaw -= aInterval
        elif "d" in key_press:
            self.yaw += aInterval

        self.a += self.yaw
        self.x += int(d * math.cos(math.radians(self.a)))
        self.y += int(d * math.sin(math.radians(self.a)))
        if self.Points[-1] != (self.x, self.y):
            self.Points.append((self.x, self.y))
