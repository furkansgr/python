#-*- coding:utf-8 -*-
#Kök içinde kök 1'in sonsuz terimini toplama.
#Sonucunda altın oran çıkıyor.
from __future__ import division

from math import *

sayi = 1
Z1 = sqrt(1+sqrt(1))

for i in range(20):
    Z2 = sqrt(1+Z1)
    Z1 = Z2
    print Z2    
