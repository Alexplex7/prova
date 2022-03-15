# -*- coding: utf-8 -*-
"""
Crie um programa que lê um número n e mostra a sequência de Fibonacci até seu n-ésimo termo.

* for: 1
* if: 1
* var: 1
"""

n = int(input("n: "))
x = 1
y = 1   
aux = y  
for _ in range(n):
    print(x)
    x = y 
    y = x + aux
    aux = x
