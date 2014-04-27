#-*- coding:utf-8 -*-

##################################
#    Tkinter Toplevel aracı      #
#   Sisteme giriş çıkış programı #
##################################

from Tkinter import *
import webbrowser

dosya = open("kayitlar.txt","a")
girdi2_0 = ""
girdi2_1 = ""
girdi2_2 = ""
etiket2_0 = ""
etiket2_1 = ""
etiket2_2 = ""
etiket2_3 = ""
    

#Boşluk bırakma fonksiyonu
def ara_birak():
    cerceve = Frame()
    cerceve.pack(pady = 5) 

#Yeni kullanıcı kaydı
def uyelik():
    global etiket2_3
    
    dosya = open("kayitlar.txt","a")
    kullanici = girdi2_0.get() + " " + girdi2_1.get() + "\n"
    dosya.write(kullanici)
    etiket2_3["text"] = "Kaydınız başarı ile yapılmıştır."
    
#Kullanıcı bilgileri kontrol fonksiyonu
def kontrol():
    global girdi2_0
    global girdi2_1
    global girdi2_2
    global etiket2_0
    global etiket2_1
    global etiket2_2
    global etiket2_3
    k = ""
    
    
    sifre = girdi2_1.get()
    sifre_tekrar = girdi2_2.get()
    kullanici = girdi2_0.get()
    
    if kullanici == "" or sifre == "" or sifre_tekrar == "":
        etiket2_3["text"] = "Boşlukları doldurup tekrar deneyin!"
    elif(sifre == sifre_tekrar):
        dosya = open("kayitlar.txt","r")
        liste = dosya.readlines()
        bul = 0
        for i in liste:
            for j in range(len(i)):
                if i[j] == " ":
                    k = i[0:j]
                    if(k == kullanici):
                        bul = 1
                    else:
                        pass
        if bul == 0:
            uyelik()
        else:
            etiket2_3["text"] = "Oppss ! Bu kullanıcı adı zaten alınmış!"
            bul = 0
    else:
        etiket2_3["text"] = "Oppss ! Şifreleri aynı girmediniz!"
    
    girdi2_0.delete(0,END)
    girdi2_1.delete(0,END)
    girdi2_2.delete(0,END)
    
               
#Kayıt penceresinin oluşturulması
def kayit():
    global girdi2_0
    global girdi2_1
    global girdi2_2
    global etiket2_0
    global etiket2_1
    global etiket2_2
    global etiket2_3
    
    pencere2 = Toplevel()
    pencere2.geometry("350x350+800+200")
    pencere2.resizable(width = FALSE , height = FALSE)
    pencere2["bg"] = "blue"
    baslik2 = pencere2.title("Kayıt Ekranı")
    ara_birak()
    
    etiket2_0 = Label(pencere2,text = "E-mail:",font = "Times 15 bold",bg = "blue" ,fg = "black")
    etiket2_0.pack()
    girdi2_0 =Entry(pencere2,font = "Times 15 bold", fg = "black" , bg = "white")
    girdi2_0.pack()
    ara_birak()
    
    etiket2_1 = Label(pencere2,text = "Şifre:",font = "Times 15 bold",bg = "blue" ,fg = "black")
    etiket2_1.pack()
    girdi2_1 = Entry(pencere2,font = "Times 15 bold", fg = "black" , bg = "white")
    girdi2_1.pack()
    ara_birak()
 
    etiket2_2 = Label(pencere2,text = "Şifre Tekrar:",font = "Times 15 bold",bg = "blue" ,fg = "black")
    etiket2_2.pack()
    girdi2_2 =Entry(pencere2,font = "Times 15 bold", fg = "black" , bg = "white")
    girdi2_2.pack()
    
    etiket2_3 = Label(pencere2,text = "Kayıt için düğmeye basın",font = "Times 15 bold",bg = "blue" ,fg = "black")
    etiket2_3.pack()
    
    dugme2_0 = Button(pencere2,text = "Kayıt Ol" , font = "Times 15 bold",fg = "black" , bg = "white",command = kontrol)
    dugme2_0.place(relx = 0.2,rely =0.7)
    dugme2_1 = Button(pencere2,text = "Çıkış" , font = "Times 15 bold",fg = "black" , bg = "white",command = pencere2.destroy)
    dugme2_1.place(relx = 0.6,rely =0.7)
     
    
#Giriş bilgilerini kontrol eden fonksiyon
def giris_kontrol():
    kullanici_bilgi = girdi1_0.get() + " " + girdi1_1.get() + "\n"
    dosya = open("kayitlar.txt","r")
    liste = dosya.readlines()
    bul = 0
    for i in liste:
        if kullanici_bilgi == i:
            bul = 1
        else:
            pass
    mesaj(bul)
        
        
#Giriş yapıldı mı yapılmadı mı onu kontrol ediyor.
def mesaj(a):
    if a == 1:
        pencere3 = Toplevel()
        pencere3.geometry("400x50+800+200")
        pencere3.resizable(width = FALSE , height = FALSE)
        pencere3["bg"] = "blue"
        baslik3 = pencere3.title("Oyun Ekranı")
        
        ara_birak()
        etiket3_0 = Label(pencere3,text = "Başarılı bir şekilde giriş yaptınız.",font = "Times 20 bold",bg = "blue" ,fg = "black")
        etiket3_0.pack()
        webbrowser.open("http://kenansubasii.blogspot.com.tr/")
    else:
        etiket1_2["text"] = "Kullanıcı adı veya parola hatalı."
    girdi1_0.delete(0,END)
    girdi1_1.delete(0,END)
             
#Ana pencerenin oluşturlması ve özelliklerinin verilmesi.
pencere = Tk()
pencere.geometry("300x350+400+200")
pencere["bg"] = "blue"
pencere.resizable(width = FALSE , height = FALSE)
baslik = pencere.title("Ana Ekran")
ara_birak()

#E-mail girişi
etiket1_0 = Label(text = "E-mail:",font = "Times 15 bold",bg = "blue" ,fg = "black")
etiket1_0.pack()
ara_birak()
girdi1_0 =Entry(font = "Times 15 bold", fg = "black" , bg = "white")
girdi1_0.pack()
ara_birak()

#Şifre girişi    
etiket1_1 = Label(text = "Şifre:",font = "Times 15 bold",bg = "blue" ,fg = "black")
etiket1_1.pack()
ara_birak()
girdi1_1 = Entry(font = "Times 15 bold", fg = "black" , bg = "white")
girdi1_1.pack()
ara_birak()

etiket1_2 = Label(text = "Giriş yapınız",font = "Times 15 bold",bg = "blue" ,fg = "black")
etiket1_2.pack()  

#İkinci pencerenin açılmasını sağlıyacak buttonun oluşturulması.
dugme1_0 = Button(text = "Kayıt Ol",command = kayit)
dugme1_0["font"] = "Times 15 bold"
dugme1_0["bg"] = "white"
dugme1_0["fg"] = "black"
dugme1_0.place(relx = 0.6,rely =0.65)

#Girişi kontrol edecek buttonun oluşturulması.
dugme1_1 = Button(text = "Giriş Yap",command = giris_kontrol)
dugme1_1["font"] = "Times 15 bold"
dugme1_1["bg"] = "white"
dugme1_1["fg"] = "black"
dugme1_1.place(relx = 0.1,rely = 0.65)

#Çıkış düğmesi
dugme1_1 = Button(text = "Çıkış",command = pencere.quit)
dugme1_1["font"] = "Times 15 bold"
dugme1_1["bg"] = "white"
dugme1_1["fg"] = "black"
dugme1_1.place(relx = 0.4,rely = 0.8)

mainloop()


