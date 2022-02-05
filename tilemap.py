import pygame as pg
from settings import *

def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
                
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
        
class Camera:
    def __init__(self, width, height, xx, yy):
        self.camera = pg.Rect(0,0, width, height)
        self.width = width
        self.height = height
        self.x = xx
        self.y = yy
        
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        self.x = -target.rect.centerx + int(WIDTH / 2) 
        self.y = -target.rect.centery + int(HEIGHT / 2)
        
        self.xx = self.x
        self.yy = self.y

        self.x = min(0, self.x)
        self.y = min(0, self.y)
        self.x = max(-(self.width - WIDTH), self.x)
        self.y = max(-(self.height - HEIGHT), self.y)
        self.camera = pg.Rect(self.x, self.y, self.width, self.height)