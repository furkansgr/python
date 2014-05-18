#-*- coding:utf-8 -*-

################################
#    İki sayının Ebobunun      #
#   bulunması algoritması-1    #
################################

fark = 0

buyuk = int(raw_input("Büyük sayıyı giriniz:"))
kucuk = int(raw_input("Küçük sayıyı giriniz:"))

if buyuk < 0:
    buyuk = (-1) * buyuk
if kucuk < 0:
    kucuk = (-1) * kucuk

while buyuk != kucuk:
    fark = buyuk - kucuk
    if fark < kucuk:
        buyuk = kucuk
        kucuk = fark
    else:
        buyuk = fark

print buyuk 
