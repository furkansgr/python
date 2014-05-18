#-*- coding:utf-8 -*-

######################################
#   iki sayının ebobunun bulunması   #
#  algoritması-2(euclid algoritması) #
######################################

kalan = 0

buyuk = int(raw_input("Büyük sayıyı giriniz:"))
kucuk = int(raw_input("Küçük sayıyı giriniz:"))

if buyuk < 0:
    buyuk = (-1) * buyuk
if kucuk < 0:
    kucuk = (-1) * kucuk

while kucuk != 0:
    kalan = buyuk % kucuk
    buyuk = kucuk
    kucuk = kalan
       
print buyuk
   
    

