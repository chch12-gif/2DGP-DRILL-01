from pico2d import load_image
import random
import common
import game_world

class Ball:
    def __init__(self, x=None, y=None):
        self.image = load_image('ball21x21.png')
        # 경기장 범위 내 랜덤 위치
        if x is None:
            self.x = random.randint(0, common.court.w)
        else:
            self.x = x
        if y is None:
            self.y = random.randint(0, common.court.h)
        else:
            self.y = y
        self.radius = 10

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius

    def handle_collision(self, group, other):
        # 보이와 충돌하면 제거되고 점수 증가
        if group == 'boy:ball' and other is common.boy:
            common.score += 1
            game_world.remove_object(self)

