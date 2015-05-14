# -*- coding: cp1254 -*-
# -*- coidng:utf-8 -*-

# Palindrom sayıları (İstediğiniz Hanede)
# Girdiğiniz hane sayısı kadar basamak sayısına
# sahip iki sayı çarpılacak.

haneSayisi = int(raw_input(u"Hane sayısını giriniz: "))


baslangic = 10 ** ( haneSayisi - 1 ) # Taramaya başlanan sayı
bitis = 10 ** ( haneSayisi )         # Taramanın bittiği sayı
bul = 0                              # Polindrom sayı kontrolünde kullanılan değişken.
sonuc = 0                            # Çarpım sonucunda elde edilen değer.
sonucBoyu = 0                        # Çarpım sonucunda elde edilen değerin boyu.
liste = []                           # Palindrom sayılarının tutulduğu liste.

for i in range(baslangic , bitis):
    for j in range(baslangic, bitis):
        sonuc = i * j;
        sonucBoyu = len(str(sonuc))
        if(sonucBoyu % 2 == 0):
            for k in range(sonucBoyu):
                if(str(sonuc)[k] != str(sonuc)[sonucBoyu - k - 1]):
                    bul = 1
            if bul == 0:       
                liste.append(sonuc)
            bul = 0

print max(liste)
