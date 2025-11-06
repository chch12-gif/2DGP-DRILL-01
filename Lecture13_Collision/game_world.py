world = [[] for _ in range(4)]

def add_object(o, depth = 0):
    world[depth].append(o)


def add_objects(ol, depth = 0):
    world[depth] += ol


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_collision_object(o):
    for pairs in collision_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    global world

    for layer in world:
        layer.clear()


def collide(a, b):
    left_a , bottom_a, right_a, top_a = a.get_bb()
    left_b , bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True
collision_pairs = {}

def add_collision_pairs(group, a, b):
    # 그룹이 없으면 초기화
    if group not in collision_pairs:
        collision_pairs[group] = [[], []]

    # a가 리스트/튜플이면 확장하고, 아니면 단일 객체로 추가
    if a is not None:
        if isinstance(a, (list, tuple)):
            collision_pairs[group][0] += list(a)
        else:
            collision_pairs[group][0].append(a)

    # b가 리스트/튜플이면 확장하고, 아니면 단일 객체로 추가
    if b is not None:
        if isinstance(b, (list, tuple)):
            collision_pairs[group][1] += list(b)
        else:
            collision_pairs[group][1].append(b)
    # Debug: 추가 후 그룹 상태 출력
    print(f"[DEBUG] add_collision_pairs: group={group} left={len(collision_pairs[group][0])} right={len(collision_pairs[group][1])}")

def handle_collisions():
    for group, pairs in list(collision_pairs.items()):
        lefts = list(pairs[0])
        rights = list(pairs[1])
        for a in lefts:
            if a not in pairs[0]:
                continue
            for b in rights:
                if b not in pairs[1]:
                    continue
                # 안전하게 get_bb 호출
                try:
                    _ = a.get_bb()
                    _ = b.get_bb()
                except Exception:
                    continue
                if collide(a, b):
                    print(f"[DEBUG] COLLIDE group={group} a={type(a).__name__} b={type(b).__name__}")
                    # 충돌 시 각 객체의 핸들러 호출 (group 전달)
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
