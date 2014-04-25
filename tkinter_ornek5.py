#-*- coding:utf-8 -*-

#######################
#  Pencere Araçları   #
#    Checkbutton      #
#######################

from Tkinter import *

#Arayüzden çıkış programı.
def cikis():
    pencere.quit()

#Ekle fonksiyonu.
def ekle():
    istek = ""
    istek = giris.get()
    dosya = open("Alisveris_listesi.txt","a")
    dosya.write(istek+"\n")
    giris.delete(0,END)

#Metin belgesine son halini yazdırma fonksiyonu
def yazdir():
    dosya = open("Alisveris_listesi.txt","a")
    if a.get() == 1:
        dosya.write("Elma" + "\n")
    if b.get() == 1:
        dosya.write("Armut" + "\n")
    if c.get() == 1:
        dosya.write("Muz" + "\n")
    if d.get() == 1:
        dosya.write("Kiraz" + "\n")
    etiket["text"] = "Alışveriş listeniz başarı ile oluşturuldu.\nMevcut dizininize \"Alisveris_listesi.txt\"\nadında metin belgesi oluşturuldu."

#Alışveriş listesinden malzeme çıkarma fonksiyonu.
def cikar():
    dosya = open("Alisveris_listesi.txt","r")
    liste = dosya.readlines()
    if giris.get() != "":
        liste.remove(giris.get()+"\n")
    if a.get() == 0:
        if "Elma\n" in liste:
            liste.remove("Elma\n")
    if b.get() == 0:
        if "Armut\n" in liste:
            liste.remove("Armut\n")
    if c.get() == 0:
        if "Muz\n" in liste:
            liste.remove("Muz\n")
    if d.get() == 0:
        if "Kiraz\n" in liste:
            liste.remove("Kiraz\n")
    
    dosya = open("Alisveris_listesi.txt","w")
    dosya.writelines(liste)
    giris.delete(0,END)
    etiket["text"] = "Alışveriş listenizden istediğiniz ürünler başarı\nile silindi.Mevcut dizininizdeki \"Alisveris_listesi.txt\"\nadındaki metin belgesiniz düzlenlendi."
    
    

#Pencerenin oluşturlması ve özelliklerinin verilmesi.
pencere = Tk()
pencere.geometry("500x400+400+300")
pencere.resizable(width = FALSE , height = FALSE)
baslik = pencere.title("Alışveriş listesi.")
        
a = IntVar()
a.set(0)

b = IntVar()
b.set(0)

c = IntVar()
c.set(0)

d = IntVar()
d.set(0)


#Etiketin oluşturlması.
etiket = Label(text = "Aşağıdakilerden lazım olanları işaretleyiniz\nEğer listede istediğiniz şey yoksa\naşağıdaki kutucuğa yazınız ve ekle butonuna basınız.",font = "Times 13 bold")
etiket.pack()

#Giriş kutucuğunun oluşturulması
giris = Entry(font = "Times 13 bold")
giris.pack()

#Checkbuttonların oluşturuması
onay_elma = Checkbutton(text = "Elma",variable = a)
onay_elma["font"] = "Times 13 bold"
onay_elma.place(relx = 0.4, rely = 0.3)

onay_armut = Checkbutton(text = "Armut",variable = b)
onay_armut["font"] = "Times 13 bold"
onay_armut.place(relx = 0.4, rely = 0.4)

onay_muz = Checkbutton(text = "Muz",variable = c)
onay_muz["font"] = "Times 13 bold"
onay_muz.place(relx = 0.4, rely = 0.5)

onay_kiraz = Checkbutton(text = "Kiraz",variable = d)
onay_kiraz["font"] = "Times 13 bold"
onay_kiraz.place(relx = 0.4, rely = 0.6)

#Çıkış düğmesi oluşturuluyor
dugme = Button(text = "Çıkış" , command = cikis ,font = "Times 13 bold",width = 8)
dugme.place(relx = 0.6,rely = 0.8)

#Ekle düğmesinin oluşturulması
dugme1 = Button(text = "Ekle" , command = ekle ,font = "Times 13 bold",width = 8)
dugme1.place(relx = 0.2,rely = 0.7)

#Yazdır butonunun oluşturulması
dugme2 = Button(text = "Yazdır" , command = yazdir ,font = "Times 13 bold",width = 8)
dugme2.place(relx = 0.6,rely = 0.7)

#Çıkarma butonunun oluşturulması
dugme3 = Button(text = "Çıkar" , command = cikar ,font = "Times 13 bold",width = 8)
dugme3.place(relx = 0.2 ,rely = 0.8)

mainloop()

