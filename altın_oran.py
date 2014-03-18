#-*- coding:utf-8 -*-
#Altın oran hesabı.
from __future__ import division
import math

Z1 = 1+0.5
Z2 = 0
n = 0

while n < 20:
    Z2 = 1+(1/Z1)
    Z1 = Z2
    n = n+1
print Z2

