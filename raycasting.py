import pygame
import numpy as np
import time
import random
import sys
from sklearn.preprocessing import scale
from sklearn.preprocessing import normalize



class Boundary:

    def __init__(self,x1,y1,x2,y2,screen):
        self.a = np.array([x1,y1])
        self.b = np.array([x2,y2])
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen,(255,255,255),(self.a),(self.b))


class Ray():

    def __init__(self,x,y,screen):
        self.pos = np.array([x,y])
        self.dir = np.array([500,300])
        self.mouse = [0,0]
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen,(255,0,0),(self.pos),(self.mouse),)

    def lookAt(self,x,y):
        self.dir[0] = x - self.pos[0]
        self.dir[1] = y - self.pos[1]
        self.mouse = [x,y]
        #self.dir = self.dir / np.max(np.abs(self.dir),axis=0)

    def cast(self,wall):
        x1 = wall.a[0]
        y1 = wall.a[1]
        x2 = wall.b[0]
        y2 = wall.b[1]
        x3 = self.pos[0]
        y3 = self.pos[1]
        x4 = self.pos[0] + self.dir[0]
        y4 = self.pos[1] + self.dir[1]
        den = (x1-x2)*(y3-y4) - (y1-y2) * (x3-x4)
        if den == 0:
            return
        t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
        u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
        if t > 0 and t<1 and u >0:
            pt = [0,0]
            pt[0] = int(x1+t*(x2-x1))
            pt[1] = int(y1+t*(y2-y1))
            return pt
        else:
            return

def main():
    screen = pygame.display.set_mode((600,600))
    screen.fill((0,0,0))
    walls = []
    for i in range(0,10):
        walls.append(Boundary(random.randint(0,600),random.randint(0,600),random.randint(0,600),random.randint(0,600),screen))
    ray = Ray(300,300,screen)

    while True:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mousex,mousey = pygame.mouse.get_pos()
        screen.fill((0,0,0))
        ray.lookAt(mousex,mousey)
        for i in range(0,len(walls)):
            walls[i].show()
            pt = ray.cast(walls[i])
            if pt:
                pygame.draw.circle(screen,(255,255,255),(pt[0],pt[1]),5)
        ray.show()       
        pygame.display.update()

main()
