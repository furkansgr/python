# -*- coding: cp1254 -*-
# -*- coidng:utf-8 -*-

# Palindrom say�lar� (�stedi�iniz Hanede)
# Girdi�iniz hane say�s� kadar basamak say�s�na
# sahip iki say� �arp�lacak.

haneSayisi = int(raw_input(u"Hane say�s�n� giriniz: "))


baslangic = 10 ** ( haneSayisi - 1 ) # Taramaya ba�lanan say�
bitis = 10 ** ( haneSayisi )         # Taraman�n bitti�i say�
bul = 0                              # Polindrom say� kontrol�nde kullan�lan de�i�ken.
sonuc = 0                            # �arp�m sonucunda elde edilen de�er.
sonucBoyu = 0                        # �arp�m sonucunda elde edilen de�erin boyu.
liste = []                           # Palindrom say�lar�n�n tutuldu�u liste.

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
