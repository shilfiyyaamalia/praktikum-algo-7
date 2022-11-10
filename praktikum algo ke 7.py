# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 23:22:54 2022

@author: shila
"""

print ("Ordinal Number")
print ("ketik 0 untuk menghentikan program")

def ordinalnumber(a):
    a == angka
    if a % 10 == 1:
        return a,"st"
    elif a % 10 == 2:
        return a, "nd"
    elif a % 10 == 3:
        return a, "rd"
    elif a % 10 in range (4,21):
        return a, "th"
    elif a % 10 == 0:
        return a, "th"
    else :
        return ordinalnumber(a)
    
angka = ""
while angka != 0:
    angka = int(input("masukan angka :"))
    print(ordinalnumber(angka))
    
print("terimaksih telah menggunakan program ini")
    
