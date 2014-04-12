#-*- coding:utf-8 -*-

#Demetler listelerle hemen hemen aynı
#özelliklere sahiptir.Ama temel farkları
#demetler değiştirilemezler.

demet = ([],6,7,8)
sayi = 0

for i in range(5):
    sayi = int(raw_input("Bir sayi giriniz:"))
    demet[0].append(sayi)

#Açıklama satırı yaptığım kod parçacığı hataya yol açar.
#Çünkü demetin yapısını değiştirmeye çalışıyoruz.
#for i in range(5):               
#    sayi = int(raw_input("Bir sayi giriniz:")) 
#    demet.append(sayi)


for i in range(len(demet)):
    print demet[i]

