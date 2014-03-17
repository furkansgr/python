#-*- coding:utf-8 -*-
#Onluk tabandaki sayıyı ikili tabana çeviren program.

dizi = []
sonuc =""

for i in range(1,100):
    print "%s  " %(i),
    while i != 0:
       if i%2==0:
           dizi.append(0)
           i = i/2
       else: 
           dizi.append(1)
           i = (i-1)/2
    
    boyut = len(dizi)
    
    for k in range(boyut):
        print "%s" %(dizi[(boyut-1)-k]),
    print
    dizi = []
  
    
       
       
  
