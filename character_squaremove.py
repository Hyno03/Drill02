from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x = 0
y = 0

for x in range(1,7):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x*100 ,90)
    update_canvas()
    delay(0.1)
for y in range(1,8):
     clear_canvas()
     grass.draw_now(400,30)
     character.draw_now(700 ,90 + y*50)
     update_canvas()
     delay(0.1)
for x in range(1,6):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(700 - x*100 ,490)
    update_canvas()
    delay(0.1)
for y in range(1,8):
     clear_canvas()
     grass.draw_now(400,30)
     character.draw_now(100 ,490 - y*50)
     update_canvas()
     delay(0.1)    
for x in range(1,5):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x*100 ,90)
    update_canvas()
    delay(0.1)                    
            


#close_canvas()
