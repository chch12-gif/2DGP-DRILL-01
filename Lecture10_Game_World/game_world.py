world = []

def add_object(o):
     world.append(o)


def remove_object(o):
    if o in world:
        world.remove(o)


def update():
    for o in world:
        o.update()

def render():
    for o in world:
        o.draw()