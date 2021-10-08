#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
t.speed(0)
colors=["red","purple","blue","green","yellow","orange"]
t.bgcolor("black")
for i in range(360):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(110)


# In[ ]:





# In[ ]:




