#-*- coding:utf-8 -*-

#############################
#     Tkinter ilk örnek     #
#############################

from Tkinter import *
from random import *

seed(None)   #Programı her çalıştırdığımızda farklı sayılar üretmek için

liste = []
sayi = 0

pencere = Tk()
pencere.geometry("200x200+700+400")  #boyut = 200x200 ,soldan sağa 700.pozisyon ,yukarıdan aşağıya 400. pozisyon 
pencere.resizable(width=FALSE,height=FALSE) #Arayüzün boyutunu degiştirmeyi kısıtlıyor

etiket = Label(fg="blue",bg="#01A9DB",font = "TimesNewRoman 18 italic",cursor = "bottom_side")
etiket.pack()

baslik = pencere.title("Rasgele 6 sayi")


while len(liste) != 6:
    sayi = randint(1,100)
    if sayi%2 == 0:
        pass
    else:
        if sayi not in liste:
            liste.append(sayi)
        else:
            pass
 
etiket["text"] = liste     #Sözlük yapısı gibi düşün içindeki bir anahtarın değerini değiştirdik.
mainloop()

