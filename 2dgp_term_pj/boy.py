from pico2d import *

# Boy 클래스 정의
class Boy:
    def __init__(self):
        self.x = 400
        self.y = 90
        self.frame = 0
        self.dir = 0  # -1: 왼쪽, 1: 오른쪽, 0: 정지
        self.image_stay = load_image('stay.jpg')
        self.image_run = load_image('run.jpg')

    def update(self):
        if self.dir != 0:
            self.x += self.dir * 5
            self.x = clamp(0, self.x, 800)
            self.frame = (self.frame + 1) % 8
        else:
            self.frame = 0

    def draw(self):
        if self.dir == 0:
            self.image_stay.draw(self.x, self.y)
        else:
            if self.dir == 1:
                self.image_run.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
            else:
                self.image_run.clip_composite_draw(self.frame * 100, 0, 100, 100, 0, 'h', self.x, self.y, 100, 100)

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.dir += 1
            elif event.key == SDLK_LEFT:
                self.dir -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.dir -= 1
            elif event.key == SDLK_LEFT:
                self.dir += 1
