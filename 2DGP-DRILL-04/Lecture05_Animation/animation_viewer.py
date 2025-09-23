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
frame_height = character.h //

frame = 0
x = 400

for x in range(0,50, 903):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
