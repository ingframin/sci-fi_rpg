import pygame as pg

class Drawable:
    def __init__(self,path,name,size=None):
        self.name = name
        self.surface = pg.image.load(path).convert_alpha()
        self.drect = self.surface.get_rect()
        self.srect = self.surface.get_rect()
        if size is not None:
            self.drect.inflate_ip(size[0],size[1])
            self.srect.inflate_ip(size[0],size[1])
        
        
    def move(self,dx,dy):
        self.drect.move_ip(dx,dy)

class AnimatedDrawable(Drawable):
    def __init__(self, path:str, name:str,frames:int,offset:tuple[int,int]):
        super().__init__(path, name)
        self.frames = frames
        self.offset = offset
        self.cur_frame = 0
        self.srect = pg.Rect

    def next(self):
        self.cur_frame += 1
        self.srect.move_ip(self.offset[0]*self.cur_frame,self.offset[1]*self.cur_frame)

