# -*- coding: utf-8 -*-

from __future__ import division
#float tanım yapmadan sayıları küsüratlı bölmemizi saglar.

print """
1)Toplama
2)Çıkarma
3)Çarpma
4)Bölme
5)Üs alma
6)Mod alma
7)Çıkış
"""
secenek = 0
while secenek != 7 :
    secenek = int(raw_input("Seçiminizi giriniz:"))
    
    if secenek == 7:
        print "Çıkış yaptınız. Hoşçakalın :D "
        exit()
    
    sayac = 1
    bul = 0
    while sayac < 7:
        if sayac == secenek:
            bul += 1
        sayac += 1   
    if bul == 0:
        print "Hatalı değer girdiniz!!!"
        exit()
    
    if secenek != 5 and secenek != 6:
        sayi1 = int(raw_input("1. sayıyı giriniz:"))
        sayi2 = int(raw_input("2. sayıyı giriniz:"))
         
    if secenek == 1:
        print "Toplam = ",sayi1+sayi2
    elif secenek == 2:
        print "Fark = ",sayi1-sayi2
    elif secenek == 3:
        print "Çarpım = ",sayi1*sayi2
    elif secenek == 4:
        print "Bölüm = ",sayi1/sayi2
    elif secenek == 5:
        sayi1 = int(raw_input("Üs alınacak sayıyı giriniz:"))
        sayi2 = int(raw_input("Üssü giriniz giriniz:"))
        print "Üs = ", sayi1**sayi2
    elif secenek ==6:
        sayi1 = int(raw_input("Mod alınacak sayıyı giriniz:"))
        sayi2 = int(raw_input("Kaca modu alınsın:"))
        print "Üs = ", sayi1%sayi2


    
    


    
    
