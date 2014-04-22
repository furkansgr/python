#-*- coding:utf-8 -*-

################################
#   Try Expect Hata Ayıklama   #
################################

try:
    sayi = int(raw_input("Lütfen bir sayı girin: "))
    print "Girdiğiniz sayı", sayi
except ValueError:
    print "Lütfen harf değil, sayı girin!"
print "Teşekkürler. Hoşçakalın!"



