# -*- coding:utf-8 -*-
from collections import OrderedDict  #Sozlugu eklediğimiz sırada tutmak için.

sozluk = OrderedDict([])
soru = ""
liste = ["apple","banana","orange"]
liste2 = ["elma","muz","portakal"]

for i in range(len(liste)):
    sozluk[liste[i]] = liste2[i]
print 
print "---------Sözlük--------","\n"
print sozluk,"\n"

soru = raw_input("Eklemek istediginiz kelime var mı?(E/H)")
if soru=="E" or soru == "e":
     deger = int(raw_input("Kaç tane kelime ekleyeceksiniz :"))
     for i in range(deger):
         ing = raw_input("İngilizce kelimeyi giriniz:")
         turk = raw_input("Girilen kelimenin Türkçesiniz giriniz:")
         sozluk[ing] = deger
     print "\n","--------Yeni Sözlük--------","\n"
     print sozluk,"\n"
else:
     print
     print "------Hoşçakalın-----"


    

