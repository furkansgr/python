#-*- coding:utf-8 -*-
#Karekök 2 sayısının bulunuşu. 
from __future__ import division

Z1 = 2+(1/3)
Z2 = 0
n = 0

while n < 20:
    Z2 = 1+(1/(2+1/Z1))
    Z1 = Z2
    n += 1

print Z2
 
