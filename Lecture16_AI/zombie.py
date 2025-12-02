from pico2d import *

import random
import math
import game_framework
import game_world
from behavior_tree import BehaviorTree, Action, Sequence, Condition, Selector


# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk', 'Idle']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombie/" + name + " (%d)" % i + ".png") for i in range(1, 11)]
            Zombie.font = load_font('ENCR10B.TTF', 40)
            Zombie.marker_image = load_image('hand_arrow.png')


    def __init__(self, x=None, y=None):
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)
        self.load_images()
        self.dir = 0.0      # radian 값으로 방향을 표시
        self.speed = 0.0
        self.frame = random.randint(0, 9)
        self.state = 'Idle'
        self.ball_count = 0


        self.tx, self.ty = 0, 0
        self.build_behavior_tree()

        self.patrol_locations = [(43, 274), (1118, 274), (1050, 494), (575, 804), (235, 991), (676, 804), (1050, 494), (1118, 274)]
        self.loc_no = 0

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        # 행동 트리 실행
        if hasattr(self, 'bt') and self.bt:
            self.bt.run()

        # 상태 결정: 목표와 현재 위치 차이가 작으면 Idle, 아니면 Walk
        if self.distance_less_than(self.x, self.y, self.tx, self.ty, 1.0):
            self.state = 'Idle'
        else:
            self.state = 'Walk'


    def draw(self):
        if math.cos(self.dir) < 0:
            Zombie.images[self.state][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            Zombie.images[self.state][int(self.frame)].draw(self.x, self.y, 100, 100)
        self.font.draw(self.x - 10, self.y + 60, f'{self.ball_count}', (0, 0, 255))
        Zombie.marker_image.draw(self.tx+25, self.ty-25)



        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def handle_collision(self, group, other):
        if group == 'zombie:ball':
            self.ball_count += 1


    def set_target_location(self, x=None, y=None):
        # 주어진 좌표가 있으면 설정, 없으면 실패로 처리
        if x is not None and y is not None:
            self.tx, self.ty = x, y
            return BehaviorTree.SUCCESS
        # 기본 동작: 무작위 위치 설정
        self.tx = random.randint(100, 1180)
        self.ty = random.randint(100, 924)
        return BehaviorTree.SUCCESS


    def distance_less_than(self, x1, y1, x2, y2, r):
        dx = x2 - x1
        dy = y2 - y1
        return (dx * dx + dy * dy) <= (r * r)


    def move_little_to(self, tx, ty):
        dx = tx - self.x
        dy = ty - self.y
        dist = math.hypot(dx, dy)
        if dist == 0:
            return True
        self.dir = math.atan2(dy, dx)
        step = RUN_SPEED_PPS * game_framework.frame_time
        if dist <= step:
            self.x = tx
            self.y = ty
            return True
        else:
            self.x += math.cos(self.dir) * step
            self.y += math.sin(self.dir) * step
            return False


    def move_to(self, r=0.5):
        # 목표가 없다면 실패
        if (self.tx, self.ty) == (0, 0):
            return BehaviorTree.FAIL
        # 이미 도달했는지 검사
        if self.distance_less_than(self.x, self.y, self.tx, self.ty, r):
            return BehaviorTree.SUCCESS
        # 조금 이동
        reached = self.move_little_to(self.tx, self.ty)
        if reached:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING


    def set_random_location(self):
        self.tx = random.randint(100, 1180)
        self.ty = random.randint(100, 924)
        return BehaviorTree.SUCCESS


    def if_boy_nearby(self, distance):
        # game_world에서 Boy 객체를 찾아 거리 검사
        boy_obj = None
        for layer in game_world.world:
            for o in layer:
                if o.__class__.__name__ == 'Boy':
                    boy_obj = o
                    break
            if boy_obj:
                break
        if not boy_obj:
            return BehaviorTree.FAIL
        if self.distance_less_than(self.x, self.y, boy_obj.x, boy_obj.y, distance):
            return BehaviorTree.SUCCESS
        return BehaviorTree.FAIL


    def move_to_boy(self, r=0.5):
        # Boy를 찾아서 목표로 설정하고 이동
        boy_obj = None
        for layer in game_world.world:
            for o in layer:
                if o.__class__.__name__ == 'Boy':
                    boy_obj = o
                    break
            if boy_obj:
                break
        if not boy_obj:
            return BehaviorTree.FAIL
        self.tx, self.ty = boy_obj.x, boy_obj.y
        return self.move_to(r)


    def get_patrol_location(self):
        if not hasattr(self, 'patrol_locations') or len(self.patrol_locations) == 0:
            return BehaviorTree.FAIL
        loc = self.patrol_locations[self.loc_no % len(self.patrol_locations)]
        self.tx, self.ty = loc
        self.loc_no = (self.loc_no + 1) % len(self.patrol_locations)
        return BehaviorTree.SUCCESS


    def build_behavior_tree(self):
        a1 = Action('Set target location', self.set_target_location, 500, 50)
        a2 = Action('Move to', self.move_to)
        move_to_target_location = Sequence('Move to Target Location', a1, a2)

        a3 = Action('Set random location', self.set_random_location)
        wander = Sequence('Wander', a3, a2)

        c1 = Condition('소년이 근처에 있는가?', self.if_boy_nearby, 7)
        a4 = Action('접근', self.move_to_boy)
        chase_boy = Sequence('소년을 추적', c1, a4)

        a5 = Action('순찰 위치 가져오기', self.get_patrol_location)
        patrol = Sequence('순찰', a5, a2)

        root = Selector('추적 또는 순찰 또는 배회', chase_boy, patrol, wander)
        self.bt = BehaviorTree(root)
        return self.bt
