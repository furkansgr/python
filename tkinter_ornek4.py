#-*- coding:utf-8 -*-

#######################
#  Pencere Araçları   #
#       Frame         #
#######################

from Tkinter import *

#Dosya oluşturma fonkiyonu
def olustur():
    dosya_ismi = ""
    metin = ""
    
    dosya_ismi = giris2.get()
    dosya = open(dosya_ismi+".txt","w")

    metin =giris1.get()
    dosya.write(metin)
    etiket1["text"] = "E.posta adresiniz başarı ile kaydedildi."
    etiket2["text"] = "E.posta adresiniz başarı ile kaydedildi."

#Arayüzden çıkış fonksiyonu
def cikis():
    pencere.destroy()

#Buttonlar arası boşluk bırakma fonksiyonu
def ara_birak():
    cerceve = Frame()
    cerceve.pack(pady = 6)

#Pencere oluşturuluyor.
pencere = Tk()
pencere.geometry("500x300+400+500")
pencere.resizable(width = FALSE , height = FALSE)
baslik = pencere.title("FRAME")


etiket2 = Label(text="Aşağıdaki kutucuğa e.posta adresinizi yazınız!")
etiket2["font"] = "Times 15 bold"
etiket2["fg"] = "white"
etiket2["bg"] = "black"
etiket2.pack()

ara_birak()

#Birinci metin yazma aralığı oluşturuluyor.
giris1 = Entry(font = "Times 15 bold", fg = "black" , bg = "white")
giris1.pack()

ara_birak()

etiket1 = Label(text="Kaydedileceği dosyanın ismini .txt\nyazmadan aşağıdaki kutucuğa yazınız.")
etiket1["font"] = "Times 15 bold"
etiket1["fg"] = "white"
etiket1["bg"] = "black"
etiket1.pack()

ara_birak()

#İkinci metin alma aralığı oluşturuluyor.
giris2 = Entry(font = "Times 15 bold", fg = "black" , bg = "white")
giris2.pack()

ara_birak()

#Dosya oluşturacak düğme oluşturuluyor.
dugme = Button(text = "Gönder" , command = olustur)
dugme["font"] = "Times 15 bold"
dugme["fg"] = "white"
dugme["bg"] = "black"
dugme.pack()

ara_birak()

#Çıkış yapacak düğme oluşturuluyor.
dugme2 = Button(text = "Çıkış" , command = cikis)
dugme2["font"] = "Times 15 bold"
dugme2["fg"] = "white"
dugme2["bg"] = "black"
dugme2.pack()

mainloop()

