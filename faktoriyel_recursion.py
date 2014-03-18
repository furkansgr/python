#-*- coding:utf-8 -*-
#Recursion ile faktöriyel hesabı

def faktoriyel(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*faktoriyel(n-1)

for i in range(10):
    print "%s! = %s" %(i,faktoriyel(i))
