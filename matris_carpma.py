#-*- coding:utf-8 -*-
#İki matrisin çarpımı.

satir1 = 0
sutun1 = 0
satir2 = 0
sutun2 = 0
deger = 0
matris1 = []
matris2 = []
sonuc = []


satir1 = int(raw_input("1. matrisin satır sayısını giriniz:"))
sutun1 = int(raw_input("1. matrisin sütun sayısını giriniz:"))

satir2 = int(raw_input("2. matrisin satır sayısını giriniz:"))
sutun2 = int(raw_input("2. matrisin sütun sayısını giriniz:"))

if sutun1 != satir2:
    print "Bu matrisler çarpılamaz!!!"
    exit(); 

for i in range(satir1):           
        matris1 += [[0] *sutun1]

for i in range(satir1):           
    for j in range(sutun1):
        sayi = int(raw_input("1. matrisin %s. satir %s. sütun elemanını giriniz:" %(i+1,j+1)))
        matris1[i][j] = sayi

for i in range(satir2):           
        matris2 += [[0] *sutun2]

for i in range(satir2):           
    for j in range(sutun2):
        sayi = int(raw_input("2. matrisin %s. satir %s. sütun elemanını giriniz:" %(i+1,j+1)))
        matris2[i][j] = sayi

for i in range(satir1):           
        sonuc += [[0] *sutun2]

for i in range(satir1):
    for j in range(sutun2):
        for k in range(satir2):
           deger += matris1[i][k]*matris2[k][j]
           sonuc[i][j] = deger
        deger = 0

for i in range(satir1):           
    for j in range(sutun1):
       print sonuc[i][j],
    print



