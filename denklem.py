#-*- coding: utf-8 -*-

from __future__ import division

print """
Denklemleri aşağıdaki şekilde yazınız:
2x+5y=10
"""

d1 = raw_input("Birinci denklemi giriniz:")
d2 = raw_input("İkinci denklemi giriniz :")
d3 = []     #Katsayılar.
bul=0
bul_a = 0
toplam = ""

#1.denklem başı sayı olan
if d1[0].isdigit():
    for i in d1:
        if i.isdigit():
             bul +=1
        else:
             break
    for i in range(bul):
        toplam = toplam + d1[i] 
    d3.append(toplam)
    toplam = ""
    bul_a = bul+2
    for i in d1[bul_a:]:
        if i.isdigit():
             bul_a +=1
        else:
             break
    for i in range(bul+1,bul_a):
        toplam = toplam + d1[i]
    if bul_a == 3:
        d3.append(toplam+'1')
    else:
        d3.append(toplam)
    d3.append(d1[bul_a+2:])

#1. denklemin başı sayı olmayan
else:
    if d1[0].isalpha():
        d3.append(1)
        bul_a = bul+2
        for i in d1[bul_a:]:
            if i.isdigit():
                bul_a +=1
            else:
                break
        for i in range(bul+1,bul_a):
            toplam = toplam + d1[i]
        if bul_a == 2:
            d3.append(toplam+'1')
        else:
            d3.append(toplam)
        d3.append(d1[bul_a+2:])
    else:
        for i in d1[1:]:
           if i.isdigit():
               bul +=1
           else:
               break
        for i in range(bul+1):
            toplam = toplam + d1[i] 
        if bul == 0:
           d3.append(toplam+'1')
        else:
           d3.append(toplam)
        toplam = ""
        bul_a = bul+3
        for i in d1[bul_a:]:
            if i.isdigit():
                bul_a +=1
            else:
                break
        for i in range(bul+2,bul_a):
            toplam = toplam + d1[i]
        if bul_a == 3:
            d3.append(toplam+'1')
        else:
            d3.append(toplam)
        d3.append(d1[bul_a+2:])
bul = 0
bul_a = 0
toplam = ""    

#2. denklem başı sayı olan
if d2[0].isdigit():
    for i in d2:
        if i.isdigit():
             bul +=1
        else:
             break
    for i in range(bul):
        toplam = toplam + d2[i] 
    d3.append(toplam)
    toplam = ""
    bul_a = bul+2
    for i in d2[bul_a:]:
        if i.isdigit():
             bul_a +=1
        else:
             break
    for i in range(bul+1,bul_a):
        toplam = toplam + d2[i]
    if bul_a == 3:
        d3.append(toplam+'1')
    else:
        d3.append(toplam)
    d3.append(d2[bul_a+2:])

#2. denklemin başı sayı olmayan.
else:
    if d2[0].isalpha():
        d3.append(1)
        bul_a = bul+2
        for i in d2[bul_a:]:
            if i.isdigit():
                bul_a +=1
            else:
                break
        for i in range(bul+1,bul_a):
            toplam = toplam + d2[i]
        if bul_a == 2:
            d3.append(toplam+'1')
        else:
            d3.append(toplam)
        d3.append(d2[bul_a+2:])
    else:
        for i in d2[1:]:
           if i.isdigit():
               bul +=1
           else:
               break
        for i in range(bul+1):
            toplam = toplam + d2[i] 
        if bul == 0:
           d3.append(toplam+'1')
        else:
           d3.append(toplam)
        toplam = ""
        bul_a = bul+3
        for i in d2[bul_a:]:
            if i.isdigit():
                bul_a +=1
            else:
                break
        for i in range(bul+2,bul_a):
            toplam = toplam + d2[i]
        if bul_a == 3:
            d3.append(toplam+'1')
        else:
            d3.append(toplam)
        d3.append(d2[bul_a+2:])    

for i in range(len(d3)):
    d3[i] = float(d3[i])

if (d3[0]/d3[3]) == (d3[1]/d3[4]):
    if (d3[2]/d3[5]) == (d3[1]/d3[4]):
        print "Sonsuz çözümü vardır."
    else:
        print "Ortak çözümü yoktur."
else:
    kat = (-d3[0]/d3[3])
    y = (d3[2]+d3[5]*kat)/(d3[1]+d3[4]*kat)
    x = (d3[2]-d3[1]*y)/d3[0]

    kontrol = (d3[3]*x+d3[4]*y)
    if kontrol == d3[5]:
        print "x=%s" %(x)
        print "y=%s" %(y)
    else:
        print "Ortak çözümü yoktur."
