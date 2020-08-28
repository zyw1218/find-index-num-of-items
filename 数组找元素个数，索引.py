# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 10:42:00 2020

@author: Administrator
"""
item=72


#找索引
a=[72, 56, 76, 72, 80, 88]
print(a.index(72))#返回第一个索引
print(list(enumerate(a)))
print([i for i,x in enumerate(a) if x==72])
#数个数
cnt=a.count(item)