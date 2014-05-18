#-*- coding:utf-8 -*-

###########################################
#   Asalların bulunması sezgisel yöntem   #
###########################################

dizi = []
asal = []
buyuk = 0
n = 0
a = 0

N = int(raw_input("Hangi sayıyı kadar asallar bulunsun:"))

buyuk = int( (N-1) / 2 )
k = buyuk ** 0.5

for i in range(1,buyuk):
    dizi.append(i)

for i in range(1,int(k)):
    if dizi[i] != 0:
        n = 2 * i + 1
        a = int((n**2)/2)
     
        for j in range(a , buyuk , n):
            dizi[j] = 0

for i in range(len(dizi)):
    if dizi[i] != 0:
        i = 2*i+1
        asal.append(i)

print asal
