# -*- coding: utf-8 -*-
"""
Created on Sun May 08 16:49:13 2016

@author: WYh
"""

f = open('skymodel.txt','r')

l = f.readlines()
a = []
b = []
for i in l:
    a.append(i.split(' ')[0:2])
#a.remove('')
for i in range(len(a)):
    temp=[]
    for j in range(len(a[i])):
        temp.append(float(a[i][j]))
    b.append(temp)
pixelArray = []
for i in range(len(b)):
    tv1 = round((b[i][0]-115)*512.0/30,2)
    tv2 = round((b[i][1]+50)*512.0/30,2)
    pixelArray.append([tv1,tv2])
f.close()
