#-*- coding:utf-8 -*-
##############################################
#      Bu program istediğiniz bir dizin      #
#      altında size dizin yada dizinler      #
#      oluşturacaktır.(os modülü fonksiyon   #
#      ve nitelikleri kullanıldı.)           #
##############################################
import os

def dizin(isim):
    os.mkdir(isim)

diz = ""
adet = 0
ad = ""


print "\n","----------------------------------------------------"
print "Bulunduğunuz dizin = " , os.getcwd()
print "---------------------------------------------------------","\n"

print """
Hangi dizinde yeni bir dizin oluşturmak istiyorsunuz ?
Eğer bulunduğuz dizinin bir üst dizini ise P yada p yazın.
(Örnek : /home/kenan dizinindesiniz /home dizinine geçmek
istiyorsunuz.)
"""

diz =  raw_input("Gitmek istediğiniz dizini yazınız = \n")

if diz == 'p' or diz == 'P':
    os.chdir(os.pardir)   
else:
    os.chdir(diz)

adet = int(raw_input("Bu dizin altına kaç tane dizin oluşturmak istiyorsunuz:" ))

for i in range(adet):
    ad = raw_input("Oluşturmak istediğiniz dizinin adını giriniz:")
    dizin(ad)
