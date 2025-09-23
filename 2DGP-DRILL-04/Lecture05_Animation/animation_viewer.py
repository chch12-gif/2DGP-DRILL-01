from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('alxe_sprite_sheets_final_png.png')

from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('run_axe.png')

frame_count = 8
frame_width = character.w // frame_count
frame_height = character.h

frame = 0
x = 400

for x in range(100):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * frame_width, 0, frame_width, frame_height, x, 90)
    update_canvas()
    frame = (frame + 1) % frame_count
    delay(0.05)

close_canvas()
