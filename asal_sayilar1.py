#-*- coding:utf-8 -*-

###########################################
#       Girilen sayıya kadar olan         #
#   asal sayıları bulan en basit yöntem   #
###########################################

bul = 0
asal = []

N = int(raw_input("Hangi sayıya kadar asal sayışar bulunsun?\n"))

for i in range(2,N):
    for j in range(2,i):
        if i % j == 0:
            bul = 1
    if bul == 0:
        asal.append(i)
    else:
        bul = 0

print asal
