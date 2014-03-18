#-*- coding:utf-8 -*-
#Faktöriyel hesabı.

def faktoriyel(n):
    if n == 0:
        return 1
    else:
        sonuc = 1
        for i in range(1,n+1):
            sonuc = sonuc*i
        return sonuc

for i in range(10):
    print "%s! = %s" %(i,faktoriyel(i))
