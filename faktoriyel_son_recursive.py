#-*- coding:utf-8 -*-
#Son recursive'lik ile faktoriyel hesabı.

def faktoriyel(n,f):
    if n == 0:
        return 1
    else:
        return n*faktoriyel(n-1,n*f)

for i in range(10):
    print "%s! = %s" %(i,faktoriyel(i,1))
