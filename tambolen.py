#Bir sayinin tam bölündüğü sayıları bulan program.
# -*- coding: utf-8 -*-

sayi = int(raw_input("Bir sayi giriniz:"))

for i in range(1,sayi):
    if sayi%i == 0:
        print i
