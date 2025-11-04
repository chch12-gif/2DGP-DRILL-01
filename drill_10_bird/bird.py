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

            self.x = random.randint(100, CANVAS_W - 100)
            self.y = random.randint(400, 650)

            self.dir = random.choice([-1, 1])

            self.speed = BIRD_SPEED_PPS

            self.frame = random.randint(0, TOTAL_FRAMES - 1)
            self.frame_timer = 0.0

    def update(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= TIME_PER_FRAME:
            self.frame = (self.frame + 1) % TOTAL_FRAMES
            self.frame_timer = 0.0

        self.x += self.dir * self.speed * dt

        padding = BIRD_W // 2
        if self.x > CANVAS_W - padding:
            self.x = CANVAS_W - padding
            self.dir = -1

        elif self.x < padding:
            self.x = padding
            self.dir = 1

    def draw(self):
        frame_x = self.frame % SPRITE_COLS
        frame_y = self.frame // SPRITE_COLS

