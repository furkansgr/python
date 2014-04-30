#-*- coding:utf-8 -*-

##########################
#   Tkinter Menu aracı   #
##########################

from Tkinter import *

#Ana Ekranın oluşturulması.
pencere = Tk()
pencere.geometry("300x300+400+300")
pencere.resizable(width = FALSE , height = FALSE)
pencere["bg"] = "blue"
baslik = pencere.title("Ana Ekran")

#Ana Menu(tablo)
tablo = Menu(pencere)
pencere.config(menu = tablo)
tablo["bg"] = "white"

#Ana menuye bağlı menu(dosya)
dosya = Menu(tablo,tearoff = 0)
tablo.add_cascade(label = "Dosya" , menu = dosya)
dosya.add_command(label = "Aç")
dosya.add_command(label = "Kaydet")
dosya.add_command(label = "Farklı Kaydet")
dosya.add_command(label = "Çıkış" , command = pencere.quit)
dosya["bg"] = "red"

#Dosya menusune bağlı menu(yeni)
yeni = Menu(dosya , tearoff = 0)   #Alt menuye bakmak istediğimizde oluşan çizgiyi yok eder. 
dosya.add_cascade(label = "Yeni" , menu = yeni )
yeni.add_command(label = "Metin belgesi")
yeni.add_command(label = "Resim belgesi")
yeni["bg"] = "red"

#Ana menuye bağlı menu(dosya2)
dosya2 = Menu(tablo , tearoff = 0)
tablo.add_cascade(label = "Düzen" , menu = dosya2)
dosya2["bg"] = "red"

mainloop()


