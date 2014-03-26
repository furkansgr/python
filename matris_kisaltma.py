#-*- coding:utf-8 -*-
#Secilen elemanın satır ve sütununu matristen silme.

matris = []
indis_satir = 0
indis_sutun = 0
 
satir = int(raw_input("Matrisin satır sayısını giriniz:"))
sutun = int(raw_input("Matrisin sütun sayısını giriniz:"))

for i in range(satir):
    matris.append([0]*sutun)

for i in range(satir):
    for j in range(sutun):
        sayi = int(raw_input("Matrisin %s. satır %s. sütun elemanının giriniz:" %(i+1,j+1)))
        matris[i][j] = sayi

for i in range(satir):
    for j in range(sutun):
        print matris[i][j],
    print 

print

indis_satir = int(raw_input("Matriste silinecek elemanın satır sayısını giriniz:")) - 1
indis_sutun = int(raw_input("Matriste silinecek elemanın sütun sayısını giriniz:")) - 1

del(matris[indis_satir])  

for j in range(indis_satir-1):
    del(matris[j][indis_sutun])

for i in range(satir-1):
    for j in range(sutun-1):
        print matris[i][j],
    print 


