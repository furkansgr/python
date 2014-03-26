#-*- coding:utf-8 -*-
#Matris oluşturma.

satir = 0
sutun = 0
matris = []

satir = int(raw_input("Matrisin satır sayısını giriniz:"))
sutun = int(raw_input("Matrisin sütun sayısını giriniz:"))

for i in range(satir):           # Kullanıcının istediği boyutta matris oluşturuyor.
        matris += [[0] *sutun]

for i in range(satir):           #Kullanıcıdan matrise değer atanıyor.
    for j in range(sutun):
        sayi = int(raw_input("%s. satir %s. sütun elemanını giriniz:" %(i+1,j+1)))
        matris[i][j] = sayi


for i in range(satir):           #Matris ekrana yazdırılıyor.
    for j in range(sutun):
        print matris[i][j],
    print
