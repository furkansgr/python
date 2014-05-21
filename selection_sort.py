#-*- coding:utf-8 -*-

#############################
#     Seçmeli Sıralama      # 
# En basit sıralama yöntemi #
#############################

dizi = [4,3,2,1]
minimum = 0
boyut = len(dizi)
degistirme = 0
karsilastirma = 0

for i in range(boyut-1):
    minimum = i 
    for j in range(i+1,boyut):
        if dizi[j] < dizi[minimum]:
            minimum = j 
        karsilastirma += 1
    dizi[i],dizi[minimum] = dizi[minimum],dizi[i]
    degistirme += 1

print "Karşılaştırma sayısı: %s" %(karsilastirma)
print "Degiştirme sayısı: %s" %(degistirme)
print dizi     

