#-*- coding:utf-8 -*-

###########################################
#     Girilen sayıya kadar olan asal      #
#    sayıları bulan Eratosthenes Eleği    #
###########################################

dizi = []
asal = []


N = int(raw_input("Hangi sayıya kadar asallar bulunsun:"))

for i in range(1,N+1):
    dizi.append(i)

k = N ** 0.5
i = 2

while dizi[i] <= k:
    if dizi[i] != 0:
        for j in range(i**2,N,i):
            dizi[j] = 0
    i = i + 1

for i in range(2,N):
    if dizi[i] != 0:
        asal.append(i)

print asal

