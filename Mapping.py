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
        self.Points = [(self.x, self.y)] * TRAIL
        self.Points_colors = [tuple(map(lambda x: i * x / TRAIL, COLOR_POINT)) for i in range(TRAIL)]

    def drawPoints(self):
        map_img = np.zeros(MAP_SIZE, np.uint8)
        cv2.circle(map_img, (self.x_start, self.y_start), RADIUS_ORIGIN_POINT, COLOR_ORIGIN_POINT, cv2.FILLED)
        for i, point in enumerate(self.Points[-TRAIL:]):
            color = self.Points_colors[i]
            cv2.circle(map_img, (int(point[0]), int(point[1])), RADIUS_POINT, color, cv2.FILLED)
        cv2.circle(map_img, (int(self.Points[-1][0]), int(self.Points[-1][1])),
                   RADIUS_LEAD_POINT, COLOR_LEAD_POINT, cv2.FILLED)
        x_cord = round((self.Points[-1][0] - self.x_start) / 100, 2)
        y_cord = round((self.Points[-1][1] - self.y_start) / 100, 2)
        cv2.putText(map_img, f'({x_cord},{y_cord})m',
                    (int(self.Points[-1][0]) + 10, int(self.Points[-1][1]) + 30),
                    cv2.FONT_HERSHEY_PLAIN, 1, COLOR_TEXT, 1)
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
        self.x += d * math.cos(math.radians(self.a))
        self.y += d * math.sin(math.radians(self.a))

        self.Points.append((self.x, self.y))

    def next_position_test(self, lr, fb, ud, yv):
        sign = lambda x: 0 if not x else int(x / abs(x))
        d = 0
        if lr:
            d = lr * INTERVAL * (-1)
            self.a = 180 * sign(lr) * (-1)

        if fb:
            d = fb * INTERVAL
            self.a = 360 * sign(fb) + 270

        if yv:
            self.yaw += yv * INTERVAL

        self.a += self.yaw
        self.x += d * math.cos(math.radians(self.a))
        self.y += d * math.sin(math.radians(self.a))

        self.Points.append((self.x, self.y))
