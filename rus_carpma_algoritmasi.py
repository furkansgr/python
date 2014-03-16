#Birinci çarpan 1 olana kadar 2'ye bölünür.İkinci carpan ise 2 ile 
#carpılır.Sonra birinci carpanın tek değerine karşılık gelen ikinci 
#çarpan değerleri toplanır

#-*- coding: utf-8 -*-

toplam = 0
carpan1 = int(raw_input("Birinci sayıyı giriniz:"))
carpan2 = int(raw_input("İkinci sayıyı giriniz:"))

while carpan1 != 0:
    if (carpan1%2)!=0:
        toplam = toplam + carpan2
    print carpan1,carpan2,toplam
    carpan1 = carpan1 /2
    carpan2 = carpan2 *2
    
print "Sonuc = %s" %(toplam)

