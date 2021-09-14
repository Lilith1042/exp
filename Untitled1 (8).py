#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11
import turtle
n=10
for j in range(10):
    for i in range(24):
        turtle.forward(n)
        turtle.left(15)
    turtle.left(180)
    for i in range(24):
        turtle.forward(n)
        turtle.left(15)
    n=n+2

