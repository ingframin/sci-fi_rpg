import pygame as pg
from display import Display
from drawable import Drawable

pg.init()

WW, WH = (1280,720)
disp = Display(WW,WH)
clock = pg.time.Clock()
drw = Drawable('drone.png','drone')
running = True

while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Usually wise to be able to close your program.
            running = False

    disp.fill()
    
    disp.draw([drw])
    # pg.display.update()
    clock.tick(60)
    disp.flip()

pg.quit()
