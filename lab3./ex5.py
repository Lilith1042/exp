#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle as t
import random as rnd

def start():
    t.speed(100)
    t.penup()
    t.goto(-0.5 * length, -0.5 * length)
    t.pendown()
    t.goto(-0.5 * length, 0.5 * length)
    t.goto(0.5 * length, 0.5 * length)
    t.goto(0.5 * length, -0.5 * length)
    t.goto(-0.5 * length, -0.5 * length)
    t.penup()
    t.goto(0, 0)
    t.ht()


length = 500
step = 2

start()

pool = [t.Turtle(shape='circle', visible=False) for i in range(40)]
for unit in pool:
    unit.speed(100)
    unit.turtlesize(0.3)
    unit.penup()
    unit.goto(rnd.randint(-0.5 * length, 0.5 * length), rnd.randint(-0.5 * length, 0.5 * length))
    unit.left(rnd.randint(-180, 180))
    unit.turtlesize(0.3)
    unit.st()


for i in range(500):
    for unit in pool:
        pos = unit.position()
        angle = unit.heading()
        if(pos[0] > length*0.5) and ((angle < 90 and angle > 0) or (angle > 270 and angle < 360)):
            unit.setheading(180 - angle)
        if(pos[0] < -length*0.5) and (angle > 90 and angle < 270):
            unit.setheading(180 - angle)
        if(pos[1] > length*0.5) and (angle > 0 and angle < 180):
            unit.setheading(360 - angle)
        if(pos[1] < -length*0.5) and (angle > 180 and angle < 360):
            unit.setheading(360 - angle)
        unit.forward(step)
        

