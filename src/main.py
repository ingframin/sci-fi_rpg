import pygame as pg
from display import Display

pg.init()

WW, WH = (1280,720)
disp = Display(WW,WH)
clock = pg.time.Clock()

running = True

while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:  # Usually wise to be able to close your program.
            running = False

    disp.fill()
    # pg.display.update()
    clock.tick(60)
    disp.flip()

pg.quit()
