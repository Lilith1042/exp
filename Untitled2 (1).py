#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t
import numpy as np


def star(r, n):
    a = 90 - 540/n
    api = np.pi*(0.5 - 3 / n)
    for i in range(n):
        t.forward(2*r*np.cos(api))
        t.left(180 - 2*a)
        
star(100, 5)


# In[ ]:




