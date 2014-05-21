#-*- coding:utf-8 -*-

######################################
#  Dizinin içinde tekrarlı sayılar   #
#   olduğunda kullanılan sıralama    #
######################################

dizi = [1,3,5,2,3,1,5,2,1]
sayi_dizi = []
yeni_dizi = []
son_dizi = []
sayi = 0
bul = 0


for i in range(0,len(dizi)):
    for j in range(i+1,len(dizi)):
        if dizi[i] == dizi[j]:
            sayi += 1
    for l in range(0,len(yeni_dizi)):
        if yeni_dizi[l] == dizi[i]:
            bul = 1
    if bul == 0:
        yeni_dizi.append(dizi[i])
        sayi_dizi.append(sayi+1)
        bul = 0
    sayi = 0

for i in range(0,len(yeni_dizi)-1):
    minimum = i
    for j in range(i+1,len(yeni_dizi)):
        if yeni_dizi[j] < yeni_dizi[minimum]:
            minimum = j
    yeni_dizi[i],yeni_dizi[minimum] = yeni_dizi[minimum],yeni_dizi[i]

for i in range(0,len(yeni_dizi)):
    for j in range(0,sayi_dizi[i]):
        son_dizi.append(yeni_dizi[i])

print dizi
print yeni_dizi
print sayi_dizi
print son_dizi

 

     
