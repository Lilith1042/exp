#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t

dt = 0.02 
k = 0.8
v_x = 20
v_y = 60
g = -10
x = -300
y = 0

t.speed(150)
t.shape('circle')
t.color('black')
t.penup()
t.goto(x, y)
t.pendown()
t.goto(-x, y)
t.goto(x, y)
t.shape('circle')
t.color('black')

for i in range(3000):
    x += v_x*dt
    y += v_y*dt + g*dt**2/2
    v_y += g*dt
    if y <= 0 and v_y < 0:
        v_y = -k*v_y
        v_x = k*v_x
    t.goto(x,y)


# In[ ]:




