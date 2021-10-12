#!/usr/bin/env python
# coding: utf-8

# In[1]:


#3ex1
import turtle
from random import randint,
t = turtle.Turtle()
t.speed(100)
for i in range(1000):
    t.left(randint(-90, 90))
    t.forward(randint(0,15))

