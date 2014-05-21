#-*- coding:utf-8 -*-

#############################
#    Kabarcık Sıralama      #
#  Büyük elemanlar dizinin  # 
#      sonuna itilir.       #
#############################

dizi = [5,4,3,2,1]
boyut = len(dizi)
karsilastirma = 0
degistirme = 0

for i in range(boyut,1,-1):
    for j in range(0,i-1):
        if dizi[j] > dizi[j+1]:
            dizi[j],dizi[j+1] = dizi[j+1],dizi[j]
            degistirme += 1
        karsilastirma += 1

print "Karşılaştırma sayısı : %s" %(karsilastirma)
print "Değiştirme sayısı : %s" %(degistirme)
print dizi
