#-*- coding:utf-8 -*-
#Permutasyon ve Kombinasyon hesabının yapılması.

from __future__ import division

def faktoriyel(sayi):
    if sayi <= 1:
        return 1
    else:
        return sayi*faktoriyel(sayi-1)

n = 0
r = 0
secim = 0
sonuc = 0
sonuc2 = 0

print"""
Hoşgeldiniz...

Permutasyon                = 1 P(n,r)
Kombinasyon                = 2 C(n,r)
Permutasyon ve Kombinasyon = 3 P(n,r) C(n,r)
Çıkış                      = -1
"""
secim = int(raw_input("Seçiminizi yapınız:"))

if secim == -1:
    print "İşlem yapmadan çıkış yaptınız!!!"
    exit()

while secim != -1:
    n = int(raw_input("n sayısını giriniz:"))
    r = int(raw_input("r sayısını giriniz:"))
    if secim == 1:
        sonuc = faktoriyel(n)/faktoriyel(n-r)
        print "P(%s,%s) = %s" %(n,r,sonuc)
    elif secim == 2:
        if r > n/2:
            r = n-r
            sonuc = faktoriyel(n)/(faktoriyel(n-r)*faktoriyel(r))
        else:
            sonuc = faktoriyel(n)/(faktoriyel(n-r)*faktoriyel(r))
        print "c(%s,%s) = %s" %(n,r,sonuc)
    elif secim == 3:
        sonuc = faktoriyel(n)/faktoriyel(n-r)
        sonuc2 = sonuc/faktoriyel(r)
        print "P(%s,%s) = %s" %(n,r,sonuc)
        print "c(%s,%s) = %s" %(n,r,sonuc2)
    elif secim == -1:
        break
    else:
        print "Hatalı değer girdiniz!!!"
    secim = int(raw_input("Seçiminizi yapınız:"))

print """
Çıkış yapılıyor...
Hoşçakalın.
"""
        
  
    
