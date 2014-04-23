#-*- coding:utf-8 -*-

########################
#     Button Örnek     #
########################

from Tkinter import *
from random import *

seed = None

#Sayı üretme fonksiyonu.
def uret():
    liste = []
    sayi = 0;
    while len(liste) != 6:
        sayi = randint(1,100)
        if sayi % 2 == 0:
             pass 
        else:
             liste.append(sayi)
    etiket["text"] = liste

#Arayüzden çıkış fonksiyonu
def cikis():
    exit()

#Pencere oluşturma
pencere = Tk()
pencere.geometry("300x100+600+300")
pencere.resizable(width = FALSE ,height = FALSE)

#Başlık oluşturma
baslik = pencere.title("Sayi Makinası")

#Arayüze yazacağımız yazının yada sayıların özelliklerinin belirlenmesi
etiket = Label(text = "Hazırsan başlayalım." , fg = "black", bg = "white")
etiket["font"] = "Times 20 italic"
etiket["cursor"] = "bottom_side"
etiket.pack()

#Sayı üreten buttonun özelliklerinin belirlenmesi
dugme = Button(text = "Sayi üret" , command = uret , cursor = "bottom_side")
dugme["fg"] = "black"
dugme["bg"] = "white"
dugme["font"] = "Times 12 bold"
dugme.pack()

#Arayüzden çıkış yapmamızı sağlayan buttonun özelliklerinin belirlenmesi
dugme2 = Button(text = "Çıkış" , command = cikis ,cursor = "bottom_side")
dugme2["fg"] = "black"
dugme2["bg"] = "white"
dugme2["font"] = "Times 12 bold"
dugme2.pack()

mainloop()
