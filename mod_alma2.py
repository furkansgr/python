#-*- coding:utf-8 -*-

##################################################
#   Yüksek sayıların modunu alma algoritması-2   #
##################################################

dizi = []
tut = 1
mod = 0

sayi = int(raw_input("Sayıyı giriniz:"))
us = int(raw_input("Üssü giriniz:"))
mod_deger = int(raw_input("Mod değerini giriniz:"))

while us != 0:
    if us % 2 == 0:
        dizi.append(0)
        us = us / 2
    else:
        dizi.append(1)
        us = (us-1) / 2


for i in range(len(dizi)):
    if dizi[i] == 1:
        mod = sayi % mod_deger
        tut = tut * mod
        tut = tut % mod_deger
    else:
        mod = sayi % mod_deger
    
    sayi = mod 
    sayi = sayi ** 2

print tut
  

