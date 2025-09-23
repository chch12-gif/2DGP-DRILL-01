from pico2d import *

open_canvas()

character = load_image('run_axe.png')

from pico2d import *

open_canvas()
character = load_image('run_axe.png')

frame_count = 8
frame_width = character.w // frame_count
frame_height = character.h

frame = 0
x = 400

for x in range(100):
    clear_canvas()
    character.clip_draw(frame * frame_width, 0, frame_width, frame_height, x, 90)
    update_canvas()
    frame = (frame + 1) % frame_count
    delay(0.05)

run_attack = load_image('run&attack.png')
run_attack_frame_count = 4
run_attack_frame_width = run_attack.w // run_attack_frame_count
run_attack_frame_height = run_attack.h



close_canvas()
