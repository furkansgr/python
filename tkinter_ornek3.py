#-*- coding:utf-8 -*-

########################
#   Pencere Araçları   #
#       Entry          #
########################

from Tkinter import *

#Dosya oluşturma fonkiyonu
def olustur():
    dosya_ismi = ""
    metin = ""
    
    dosya_ismi = giris.get()
    dosya = open(dosya_ismi+".txt","a")
    
    metin =giris2.get()
    dosya.write(metin+"\n")
    giris2.delete(0,END)

#Giriş kısmındaki yazıyı silme fonksiyonu   
def sil():
    giris.delete(0,END)

#Arayüzden çıkma fonksiyonu 
def cikis():
    exit()

#Pencere oluşturma ve özelliklerini verme fonksiyonu.
pencere = Tk()
pencere.geometry("500x300+400+200")
pencere.resizable(width = FALSE ,height = FALSE)
baslik = pencere.title("Girdi")


etiket = Label(text = "Dosyanın ismini sonunda \n.txt yazmadan giriniz." , font = "Times 14 bold")
etiket.pack()

#Tek satırlık metin okuma kutucuğu oluşturma.
giris = Entry(font = "Times 12 bold")
giris.pack()

etiket2 = Label(text = "Dosya içine yazmak istediginiz\nmetni aşağıdaki kutucuğa yazınız." , font = "Times 14 bold")
etiket2.pack()

giris2 = Entry(font = "Times 12 bold")
giris2.pack()

#Oluştur fonksiyonunun düğmesinin oluşturulması.
dugme = Button(text = "Yaz" , command = olustur , font = "Times 14 bold")
dugme.pack()

#Silme fonksiyonunun düğmesinin oluşturulması.
dugme1 = Button(text = "Sil" , command = sil , font = "Times 14 bold")
dugme1.pack()

#Arayüzden çıkış fonksiyonunun düğmesinin oluşturulması.
dugme2 = Button(text = "Çıkış" , command = cikis , font = "Times 14 bold")
dugme2.pack()



mainloop()
