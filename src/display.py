import pygame as pg


class Display:
    def __init__(self,width,height,color=(0,0,0)) -> None:
        self.width = width
        self.height = height
        self.screen_surf = pg.display.set_mode((width,height))
        self.color = color
        

    def fill(self):
        self.screen_surf.fill(self.color)

    def flip(self):
        pg.display.flip()


    def draw(self, drawables):
        for d in drawables:
            surf = d.surface
            source_rect = d.srect
            dest_rect = d.drect
            self.screen_surf.blit(surf,dest_rect,area=source_rect)