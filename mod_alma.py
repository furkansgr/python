#-*- coding:utf-8 -*-

##########################################################
#   Yüksek dereceli sayıların modunu alma algoritması-1  #
##########################################################

tut = 1
mod = 0

sayi = int(raw_input("Sayıyı giriniz:"))
us = int(raw_input("Üssü giriniz:"))
mod_deger = int(raw_input("Mod değerini giriniz:"))

while us != 1:
    if us % 2 == 0:
        sayi = sayi**2
        us = us / 2
        mod = sayi % mod_deger
    else:
        tut = tut * sayi
        us = us - 1
        sayi = sayi**2
        us = us / 2
        mod = sayi % mod_deger
     
if tut == 0:
    print mod
else:
    mod = mod*tut
    mod = mod % mod_deger
    print mod
