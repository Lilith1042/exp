#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle as t
import time


def number(a):
    t.shape("circle")
    t.speed(1)
    t.penup()
    for i in range(len(a)):
        t.goto(point[a[i][0] - 1][0] + i * 30, point[a[i][0] - 1][1])
        t.pendown()
        for j in range(1, len(a[i])):
            t.goto(point[a[i][j] - 1][0] + i * 30, point[a[i][j] - 1][1])
        t.penup()

    time.sleep(10)


point = [(0, 40), (20, 40), (0, 20), (20, 20), (0, 0), (20, 0)]

l = [(1, 5, 6, 2, 1), (3, 2, 6), (1, 2, 4, 5, 6), (1, 2, 3, 4, 5),
     (1, 3, 4, 6, 2),
     (2, 1, 3, 4, 6, 5), (2, 3, 4, 6, 5, 3), (1, 2, 3, 5),
     (4, 3, 1, 2, 6, 5, 3),
     (5, 4, 2, 1, 3, 4)]

res = [l[1], l[4], l[1], l[7], l[7]]

number(res)


# In[ ]:




