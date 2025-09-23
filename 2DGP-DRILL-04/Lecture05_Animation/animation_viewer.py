from pico2d import *

open_canvas()

character = load_image('run_axe.png')

from pico2d import *

open_canvas()
character = load_image('run_axe.png')

frame_count = 6
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

run_attack = load_image('run&attack_axe.png')
run_attack_frame_count = 4
run_attack_frame_width = run_attack.w // run_attack_frame_count
run_attack_frame_height = run_attack.h

run_attack_frame = 0
for x in range(100, 200):
    clear_canvas()
    run_attack.clip_draw(run_attack_frame * run_attack_frame_width, 0, run_attack_frame_width, run_attack_frame_height, x, 90)
    update_canvas()
    run_attack_frame = (run_attack_frame + 1) % run_attack_frame_count
    delay(0.05)

attack_2 = load_image('attack_2_axe.png')
attack_2_frame_count = 4
attack_2_frame_width = attack_2.w // attack_2_frame_count
attack_2_frame_height = attack_2.h

attack_2_frame = 0
for x in range(200, 300):
    clear_canvas()
    attack_2.clip_draw(attack_2_frame * attack_2_frame_width, 0, attack_2_frame_width, attack_2_frame_height, x, 90)
    update_canvas()
    attack_2_frame = (attack_2_frame + 1) % attack_2_frame_count
    delay(0.05)

walk = load_image('walk_axe.png')
walk_frame_count = 8
walk_frame_width = walk.w // walk_frame_count
walk_frame_height = walk.h

walk_frame = 0
for x in range(300, 400):
    clear_canvas()
    walk.clip_draw(walk_frame * walk_frame_width, 0, walk_frame_width, walk_frame_height, x, 90)
    update_canvas()
    walk_frame = (walk_frame + 1) % walk_frame_count
    delay(0.05)

close_canvas()
