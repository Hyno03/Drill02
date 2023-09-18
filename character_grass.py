from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


x = 0
y = 0
"""while(x<400):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(400+x ,90+y)
    x = x + 10
    update_canvas()
    delay(0.1)
    if(400+x == 760):
        while(y<500):
            clear_canvas()
            grass.draw_now(400,30)
            character.draw_now(400+x ,90+y)
            y = y + 10
            update_canvas()
            delay(0.1)
            if(90+y == 400):
                while(x == 0):
                    clear_canvas()
                    grass.draw_now(400,30)
                    character.draw_now(400+x ,90+y)
                     x = x - 10
                    update_canvas()
                    delay(0.1)
"""
for x in range(1,8):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x*100 ,90)
    update_canvas()
    delay(0.1)
for y in range(1,8):
     clear_canvas()
     grass.draw_now(400,30)
     character.draw_now(800 ,y*70)
     update_canvas()
     delay(0.1)
for x in range(1,8):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(800 - x*100 ,560)
    update_canvas()
    delay(0.1)
for y in range(1,8):
     clear_canvas()
     grass.draw_now(400,30)
     character.draw_now(0 ,560 -  y*70)
     update_canvas()
     delay(0.1)    
for x in range(1,5):
    clear_canvas()
    grass.draw_now(400,30)
    character.draw_now(x*100 ,90)
    update_canvas()
    delay(0.1)                    
            


#close_canvas()
