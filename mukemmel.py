# -*- coding: utf-8 -*-
#1000'e kadar olan mükemmel sayıları bulan program.
liste = []
toplam = 0
for j in range(1,1000):
    for i in range(1,j):
        if j%i == 0:
            liste.append(i)
    for i in range(len(liste)):
        toplam = toplam + liste[i]
    if toplam == j:
        print j
    liste = []
    toplam = 0
