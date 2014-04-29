#-*- coding:utf-8 -*-

##############################
#   Tkinter listbox aracı    #
##############################

from Tkinter import *

def ekle():
    liste.insert(END , girdi.get() )
    girdi.delete(0,END)
    etiket1_1["text"] = "Ekleme işlemi gerçekleştirildi."
def sil():
    liste.delete(ACTIVE)
    girdi.delete(0,END)
    etiket1_1["text"] = "Silme işlemi gerçekleştirildi."
    

#Pencere özellikleri.
pencere = Tk()
pencere["bg"] = "blue"
pencere.geometry("300x400+400+400")
pencere.resizable(width = FALSE,height = FALSE)
baslik = pencere.title("Sınıf Listesi")

#Liste başlığı.
etiket1_0 = Label(text = "Sınıf Listesi",bg = "blue",fg = "black",font = "Times 15 bold")
etiket1_0.pack()

#Listbox'ın oluşturulması.
liste = Listbox(bg = "white" , fg = "black")
liste.pack()

#Etiket
etiket1_1 = Label(text = "Eklemek veya silmek istediğiniz\nismi aşağıdaki boşluğa giriniz.",bg = "blue",fg = "black",font = "Times 10 bold")
etiket1_1.pack()

#Veri girişi yapılacak kutucuk.
girdi = Entry(font = "Times 10 bold",bg = "white",fg = "black")
girdi.pack()


#Sınıf listesini ekleme yapma düğmesi
dugme1_0 = Button(text = "Ekle" ,fg = "black",bg = "white",width = 6 ,height = 1,command = ekle)
dugme1_0.place(relx = 0.20,rely = 0.7)

#Sınıf listesinden silme işlemi gerçekleştiren düğme.
dugme1_1 = Button(text = "Sil" ,fg = "black",bg = "white",width = 6,height = 1,command = sil)
dugme1_1.place(relx = 0.6,rely = 0.7 )

#Programdan çıkış düğmesi.
dugme1_2 = Button(text = "çıkış" ,fg = "black",bg = "white",width = 6,height = 1,command = pencere.quit)
dugme1_2.place(relx = 0.4,rely = 0.82 )


mainloop()

