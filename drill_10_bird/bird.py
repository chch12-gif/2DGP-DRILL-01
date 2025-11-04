from pico2d import *
import random
import time

CANVAS_W, CANVAS_H = 1280, 720

BIRD_W= 180
BIRD_H= 168

BIRD_KMPH = 10.0
PIXEL_PER_METER = (BIRD_H/ 0.3) # 168px= 30cm
METER_PER_SEC = (BIRD_KMPH * 1000.0 / 3600.0)
BIRD_SPEED_PPS = (METER_PER_SEC * PIXEL_PER_METER)

FRAMES_PER_SEC = 5
TIME_PER_FRAME = 1.0 / FRAMES_PER_SEC

SPRITE_COLS = 5
SPRITE_ROWS = 3
TOTAL_FRAMES = 14

class Bird:
    sprite_sheet = None

    def __init__(self):
        if Bird.sprite_sheet is None:
            Bird.sprite_sheet = load_image('bird_animation.png')

            