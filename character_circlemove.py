from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0

while(x < 360):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(400+100*math.sin(x/360*10*math.pi),400 + 100*math.cos(x/360*10*math.pi))
    x = x +10
    update_canvas()
    delay(0.1)

close_canvas()
