TELLO_WIFI = "TELLO-60679B"
HOME_WIFI = "Diralselno"

MIN_BATTERY_FLIP = 50

GAME_PAD_SIZE = (400, 400)

STREAM_VIDEO = True
STREAM_NAME = "Stream Video"
STREAM_SIZE = (360, 240)

SHOW_MAP = True
MAP_SIZE = (1000, 1000, 3)
MAP_NAME = "Map"

INTERVAL = 0.1  # second

### MAPPING ###
fSpeed = 25  # 15cm/s
aSpeed = 50  # 50degrees/s
zSpeed = 50

dInterval = fSpeed * INTERVAL
aInterval = aSpeed * INTERVAL


TRAIL = 200  # points
RADIUS_POINT = 5
COLOR_POINT = (0, 0, 255)
RADIUS_LEAD_POINT = 8
COLOR_LEAD_POINT = (0, 255, 0)
COLOR_TEXT = (255, 0, 255)
RADIUS_ORIGIN_POINT = 7
COLOR_ORIGIN_POINT = (142, 142, 142)

### FACE TRACKING ###
FACE_SIZE = 6500  # pixels
FACE_SIZE_RANGE = [6200, 6800]
PID = [0.4, 0.4, 0]

fSpeed_track = 15  # 15cm/s
aSpeed_track = 20  # 50degrees/s
zSpeed_track = 10


