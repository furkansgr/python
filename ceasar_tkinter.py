#-*- coding:utf-8 -*-

###################################
#   Ceasar şifreleme algoritması  #
###################################

from Tkinter import *
from datetime import datetime 
import webbrowser

etiket2_3 = ""
girdi2_1 = ""
girdi2_2 = "" 
etiket3_3 = ""
girdi3_1 = ""
girdi3_2 = ""

tarih = datetime.now()

#Boşluk bırakma fonksiyonu.
def ara_birak():
    cerceve = Frame()
    cerceve.pack(pady = 8)

#Bloga yölendirme fonksiyonu.
def takip_et():
    webbrowser.open("http://kenansubasii.blogspot.com.tr/")

#Çözüm fonksiyonu.
def cozum():
    global etiket3_3
    global girdi3_1
    global girdi3_2
    
    dosya_adi = girdi3_1.get() + ".txt"
    anahtar = int(girdi3_2.get())
    liste2 = []
    
    try:
        dosya = open(dosya_adi,"r")
    except IOError,(hatakodu,hataadi):
        etiket3_3["text"] = "Dosya bulunamadı!!!"
        girdi3_1.delete(0,END)
        girdi3_2.delete(0,END)
        
    
    liste = dosya.readlines()
    
    for i in liste:
        for k in i:
            karakter = chr((ord(k)-anahtar)%255)
            liste2.append(karakter) 
    
    dosya_adi = girdi3_1.get() + "_cozum" + ".txt"
    dosya2 = open(dosya_adi, "w")
    dosya2.writelines(liste2)
    dosya2.close()
    
    etiket3_3["text"] = "Masaüstünüzde " + dosya_adi + "\nisminde çözüm dosyası oluşturuldu."
    girdi3_1.delete(0,END)
    girdi3_2.delete(0,END)

#Şifreleme fonksiyonu.
def sifrele():
    global etiket2_3
    global girdi2_1
    global girdi2_2
    
    dosya_adi = girdi2_1.get() + ".txt"
    anahtar = int(girdi2_2.get())
    liste2 = []
    
    try:
        dosya = open(dosya_adi,"r")
    except IOError,(hatakodu,hataadi):
        etiket2_3["text"] = "Dosya bulunamadı!!!"
        girdi2_1.delete(0,END)
        girdi2_2.delete(0,END)

    liste = dosya.readlines()
    
    for i in liste:
        for k in i:
            karakter = chr((ord(k)+anahtar)%255)
            liste2.append(karakter) 
    
    dosya_adi = girdi2_1.get() + "_sifre" + ".txt"
    dosya2 = open(dosya_adi, "w")
    dosya2.writelines(liste2)
    dosya2.close()
    
    etiket2_3["text"] = "Masaüstünüzde " + dosya_adi + "\nisminde şifreli dosya oluşturuldu."
    girdi2_1.delete(0,END)
    girdi2_2.delete(0,END)
    
    
                  
              
#Çözme fonksiyonu.
def cozum_ekran():
    global etiket3_3
    global girdi3_1
    global girdi3_2
    
    #Çözüm penceresi özellikleri.
    pencere3 = Toplevel()
    pencere3.geometry("300x500+800+300")
    pencere3.resizable(width = FALSE,height = FALSE)
    pencere3["bg"] = "blue"
    baslik3 = pencere3.title("Çözüm")
    
    tarih3 = "Tarih\n" +str(tarih.day) + "." + str(tarih.month) + "." + str(tarih.year) 
    etiket3_0 = Label(pencere3,text = tarih3 , bg = "blue" ,fg = "black")
    etiket3_0["font"] = "Times 10 bold"
    etiket3_0.place(relx = 0.6,rely = 0.0) 
    
    etiket3_1 = Label(pencere3,text = "Dosyanın adını giriniz\n.txt uzantısını yazmayınız:" , bg = "blue" ,fg = "black")
    etiket3_1["font"] = "Times 15 bold"
    etiket3_1.place(relx = 0.05,rely = 0.1) 
   
    #Dosyanın adını alan Entry()
    girdi3_1 = Entry(pencere3,font = "Times 15 bold",width = 25)
    girdi3_1.place(relx = 0.1 ,rely = 0.25)
     
    etiket3_2 = Label(pencere3,text = "Anahtar değerini giriniz:" , bg = "blue" ,fg = "black")
    etiket3_2["font"] = "Times 15 bold"
    etiket3_2.place(relx = 0.1,rely = 0.35) 

    #Anahtar değerini alan Entry()
    girdi3_2 = Entry(pencere3,font = "Times 15 bold",width = 25)
    girdi3_2.place(relx = 0.1 ,rely = 0.45)
    
    #Mesaj veriliyor.
    etiket3_3 = Label(pencere3,text = "" , bg = "blue" ,fg = "black")
    etiket3_3["font"] = "Times 11 bold"
    etiket3_3.place(relx = 0.1,rely = 0.55)
    
    #Çözüm metnini oluşturan düğme.
    dugme3_0 = Button(pencere3,text = "Çöz" , bg = "white" ,fg = "black",width = 8 , height = 1)
    dugme3_0["font"] = "Times 13 bold"
    dugme3_0["command"] = cozum
    dugme3_0.place(relx = 0.35,rely = 0.70)

    #Çıkış düğmesi.
    dugme3_1 = Button(pencere3,text = "Çıkış" , bg = "white" ,fg = "black",width = 8 , height = 1)
    dugme3_1["font"] = "Times 13 bold"
    dugme3_1["command"] = pencere3.destroy
    dugme3_1.place(relx = 0.35,rely = 0.80)




    

#Şifreleme ekranı oluşturulması.
def sifrele_ekran():
    global etiket2_3
    global girdi2_1
    global girdi2_2
    
    #Şifreleme penceresi özellikleri.
    pencere2 = Toplevel()
    pencere2.geometry("250x500+800+300")
    pencere2.resizable(width = FALSE,height = FALSE)
    pencere2["bg"] = "blue"
    baslik2 = pencere2.title("Şifreleme")
    
    tarih2 = "Tarih\n" +str(tarih.day) + "." + str(tarih.month) + "." + str(tarih.year) 
    etiket2_0 = Label(pencere2,text = tarih2 , bg = "blue" ,fg = "black")
    etiket2_0["font"] = "Times 10 bold"
    etiket2_0.place(relx = 0.6,rely = 0.0) 
    
    etiket2_1 = Label(pencere2,text = "Dosyanın adını giriniz\n.txt uzantısını yazmayınız:" , bg = "blue" ,fg = "black")
    etiket2_1["font"] = "Times 15 bold"
    etiket2_1.place(relx = 0.05,rely = 0.1) 
   
    #Dosyanın adını alan Entry()
    girdi2_1 = Entry(pencere2,font = "Times 15 bold")
    girdi2_1.place(relx = 0.1 ,rely = 0.25)
     
    etiket2_2 = Label(pencere2,text = "Anahtar değerini giriniz:" , bg = "blue" ,fg = "black")
    etiket2_2["font"] = "Times 15 bold"
    etiket2_2.place(relx = 0.1,rely = 0.35) 

    #Anahtar değerini alan Entry()
    girdi2_2 = Entry(pencere2,font = "Times 15 bold")
    girdi2_2.place(relx = 0.1 ,rely = 0.45)
    
    #Mesaj veriliyor.
    etiket2_3 = Label(pencere2,text = "" , bg = "blue" ,fg = "black")
    etiket2_3["font"] = "Times 11 bold"
    etiket2_3.place(relx = 0.1,rely = 0.55)
    
    #Şifreli metni oluşturan düğme.
    dugme2_0 = Button(pencere2,text = "Şifrele" , bg = "white" ,fg = "black",width = 8 , height = 1)
    dugme2_0["font"] = "Times 13 bold"
    dugme2_0["command"] = sifrele
    dugme2_0.place(relx = 0.3,rely = 0.70)

    #Çıkış düğmesi
    dugme2_1 = Button(pencere2,text = "Çıkış" , bg = "white" ,fg = "black",width = 8 , height = 1)
    dugme2_1["font"] = "Times 13 bold"
    dugme2_1["command"] = pencere2.destroy
    dugme2_1.place(relx = 0.3,rely = 0.80)
    
 
    
    
        

#Pencere özelliklerinin belirlenmesi.
pencere = Tk()
pencere.geometry("300x350+400+300")
pencere.resizable(width = FALSE , height = FALSE)
pencere["bg"] = "blue"
baslik = pencere.title("Ceasar")

#Tarih yazdırma.
tarih1 = "Tarih\n" +str(tarih.day) + "." + str(tarih.month) + "." + str(tarih.year) 
etiket1_0 = Label(text = tarih1 , bg = "blue" ,fg = "black")
etiket1_0["font"] = "Times 10 bold"
etiket1_0.place(relx = 0.6,rely = 0.0)
ara_birak()

#Başlık yazdırılması.
etiket1_1 = Label(text = "Ceasar Şifreleme Algoritması" , bg = "blue" , fg = "black")
etiket1_1["font"] = "Times 17 bold"
etiket1_1.place(relx = 0.0 , rely = 0.15)


#Şifreleme düğmesi
dugme1_0 = Button(text = "Şifrele" ,bg = "white" , fg = "black",width = 10 , height = 1)
dugme1_0["command"] = sifrele_ekran
dugme1_0["font"] = "Times 15 bold"
dugme1_0.place(relx = 0.3 , rely = 0.3)

#Çözme düğmesi
dugme1_1 = Button(text = "Çöz" ,bg = "white" , fg = "black",width = 10 , height = 1)
dugme1_1["font"] = "Times 15 bold"
dugme1_1["command"] = cozum_ekran
dugme1_1.place(relx = 0.3 , rely = 0.5)

#Çıkış düğmesi
dugme1_2 = Button(text = "Çıkış" ,bg = "white" , fg = "black",width = 10 , height = 1)
dugme1_2["command"] = pencere.destroy
dugme1_2["font"] = "Times 15 bold"
dugme1_2.place(relx = 0.3 , rely = 0.7)

#Bloğa yönlendirme düğmesi
dugme1_3 = Button(text = "Takip Et" ,bg = "white" , fg = "black",width = 6 , height = 1)
dugme1_3["command"] = takip_et
dugme1_3["font"] = "Times 9 bold"
dugme1_3.place(relx = 0.7 , rely = 0.9)


mainloop()




