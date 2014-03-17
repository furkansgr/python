#-*- coding: utf-8 -*-
#100 tane fibonacci sayısını ekrana basan program.
def fibonacci():
    fibo = [1,2]
    sayac = 0
    for i in range(2,100):
        sayac = fibo[i-1]+fibo[i-2]
        fibo.append(sayac)
    for i in range(100):
        print fibo[i]

fibonacci()
