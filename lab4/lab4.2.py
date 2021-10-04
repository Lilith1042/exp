#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import math
from pygame.draw import *

pygame.init()
FPS = 30
screen_x=1200
screen_y=800
screen = pygame.display.set_mode((1200, 800))
screen.fill((255,175,128))

green=(0,104,55)
white=(255,255,255)
black=(0,0,0)

surf1 = pygame.Surface([1200,800], pygame.SRCALPHA, 32)

def makeEllipseWithRotate(x, y, a, b, fi, col=green, dim=1000):
    surface = pygame.Surface([dim,dim], pygame.SRCALPHA, 32)
    pygame.draw.ellipse(surface, col, [(dim - a)//2, (dim - b)//2, a, b])
    surface = pygame.transform.rotate(surface, fi)
    w = surface.get_width()
    surf1.blit(surface, (x - w//2, y - w//2))
    pygame.display.update()

def branch(x=610, y=195, rl=1, sc=5, col=green):
#branch
    x0 = x+10*sc*rl;
    y0 = y+20*sc;
    a = 110*sc;
    b = 70*sc;
    phi_1 = math.pi/10*(3 - rl)
    phi_2 = math.pi/10*(7 - rl)
    pygame.draw.arc(surf1,col,[x0 - a/2*(1+rl), y0 - b/2, a, b], phi_1, phi_2, 3)
#polygon(surf1,(255,0,0),[(x,y),(x,y+10)],10)
#leavs
    makeEllipseWithRotate(x-63*sc*rl, y-6*sc, 3*sc, 14*sc, -20*rl, col)
    makeEllipseWithRotate(x-58*sc*rl, y-7*sc, 3*sc, 14*sc, -20*rl, col)
    makeEllipseWithRotate(x-52*sc*rl, y-8*sc, 3*sc, 14*sc, -20*rl, col)
    makeEllipseWithRotate(x-46*sc*rl, y-8*sc, 3*sc, 14*sc, -20*rl, col)
    makeEllipseWithRotate(x-41*sc*rl, y-7*sc, 3*sc, 14*sc, -20*rl, col)
    makeEllipseWithRotate(x-35*sc*rl, y-6*sc, 3*sc, 14*sc, -20*rl, col)


def bamboo_plant(x=635, y=563, sc=5, col=green):
    polygon(surf1,col,[(x,y),(x,y-26*sc)],6*sc)
    polygon(surf1,col,[(x,y-30*sc),(x,y-60*sc)],6*sc)
    polygon(surf1,col,[(x,y-64*sc),(x+4*sc,y-80*sc)],4*sc)
    polygon(surf1,col,[(x+4*sc,y-84*sc),(x+12*sc,y-107*sc)],3*sc)
    branch(x-4*sc, y-39*sc, 1, sc, col)
    branch(x+4*sc, y-54*sc, -1, sc, col)
    branch(x-2*sc, y-72*sc, 1, sc, col)
    branch(x+8*sc, y-80*sc, -1, sc, col)

bamboo_plant(630, 560, 5)
bamboo_plant(330, 600, 3, (100, 69, 0))

def panda_head(x=825, y=475, fi=20, d=5):
    surface = pygame.Surface([200,200], pygame.SRCALPHA, 32)
    pygame.draw.rect(surface, white, [100-13*d, 100-13*d, 26*d, 26*d],  border_radius=int((4/5)*13*d))
    surface = pygame.transform.rotate(surface, fi)
    w = surface.get_width()
    surf1.blit(surface, (x - w//2, y - w//2))
    pygame.display.update()
    makeEllipseWithRotate(x+12*d, y-4*d, 8*d, 12*d, 20, black)    
    makeEllipseWithRotate(x-4*d, y-12*d, 8*d, 12*d, -70, black)
    makeEllipseWithRotate(x+2*d, y+5*d, 5*d, 5*d, 0, black)
    makeEllipseWithRotate(x-6*d, y, 5*d, 5*d, 0, black)
    makeEllipseWithRotate(x-6*d, y+8*d, 6*d, 5*d, -20, black)
    
    
def panda(x=900, y=500, sc=5):
    makeEllipseWithRotate(x-20*sc, y+11*sc, 12*sc, 30*sc, -10, black)
    pygame.draw.ellipse(surf1, white, [x-25*sc, y-14*sc, 50*sc, 28*sc])
    polygon(surf1,black,[(x,y-14*sc),(x,y+14*sc)],10*sc)
    polygon(surf1,black,[(x,y+14*sc),(x-2*sc,y+22*sc)],10*sc)
    makeEllipseWithRotate(x+16*sc, y+11*sc, 12*sc, 30*sc, -20, black)
    makeEllipseWithRotate(x-4*sc, y+22*sc, 14*sc, 8*sc, 0, black)
    panda_head(x-15*sc, y-5*sc, 20, sc)

panda(900, 500, 6)

screen.blit(surf1, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
pygame.quit()


# In[ ]:





# In[ ]:




