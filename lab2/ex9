#!/usr/bin/env python
# coding: utf-8

# In[2]:


#9
import turtle
import math
turtle.shape('turtle')
n=3
r=10 
def more_agles(n,m): 
    q=360/n
    while n>0:
        
        turtle.left(q)
        turtle.forward(m)
        n-=1
while n<13:
    m=2*r*math.sin(math.pi/n)
    x=(180-360/n)/2
    turtle.left(x)
    
    more_agles(n,m)
    turtle.right(x)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    n+=1
    r+=10


# In[ ]:




