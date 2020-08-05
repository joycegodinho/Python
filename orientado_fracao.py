# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:19:07 2020

@author: joyce
"""
## Programa orientado à objetos para realizar operações com frações
'''
Algorítico de Euclides, função para reduzir a menor fração, 
dividindo o numerador e denominador pelo maior divisor comum
'''

def mdc(m,n):
    while m%n != 0:
            oldm = m
            oldn = n
            
            m = oldn
            n = oldm%oldn
            
    return n

# função para operar frações
    
class fracao:
    
    # definição do método construtor
    def __init__(self, numerador, denominador):
  
        comum = mdc(numerador, denominador)
        
        self.num = numerador
        self.den = denominador
        
        if self.num == int(numerador) and self.den == int(denominador):
            self.num = numerador//comum
            self.den = denominador//comum
        else:
            raise Exception ("O numerador ou o denominador não são inteiros")
        
    def getNum (self):
        
        return self.num
    
    def getDen(self):
        
        return self.den
        
    def __str__(self):
        
        return str(self.num)+"/"+str(self.den)
    
    def __repr__(self):
        
        return str(self.num)+"/"+str(self.den)
    
    
    
    def __add__(self, outra):
        
        novo_den = self.den*outra.den
        novo_num = self.num*outra.den + self.den*outra.num
        
        return fracao(novo_num, novo_den)
    
    def __radd__(self, outra):
        
        return fracao.__add__(self, outra)
    
    def __iadd__(self, outra):
        
        return fracao.__add__(self, outra)
    
    def __sub__(self, outra):
        novo_den = self.den*outra.den
        novo_num = self.num*outra.den - self.den*outra.num
        comum = mdc(novo_num, novo_den)
        
        return fracao(novo_num//comum, novo_den//comum) 
    
    def __mul__(self, outra):
        
        novo_den = self.den*outra.den
        novo_num = self.num*outra.num
        comum = mdc(novo_num, novo_den)
        
        return fracao(novo_num//comum, novo_den//comum)
    
    def __truediv__(self, outra):
        novo_num = self.num*outra.den
        novo_den = self.den*outra.num
        comum = mdc(novo_num, novo_den)
        
        return fracao(novo_num//comum, novo_den//comum)       
    
    def __eq__(self, outra):
        
        prim_num = self.num*outra.den
        seg_num = outra.num*self.den
        
        return prim_num == seg_num
    
    def __gt__(self, outra):
        
        prim_num = self.num*outra.den
        seg_num = outra.num*self.den
        
        return prim_num > seg_num
    
    def __ge__(self, outra):

        prim_num = self.num*outra.den
        seg_num = outra.num*self.den
        
        return prim_num >= seg_num
    
    def __lt__(self, outra):
        
        prim_num = self.num*outra.den
        seg_num = outra.num*self.den
        
        return prim_num < seg_num
    
    def __le__(self, outra):
        
        prim_num = self.num*outra.den
        seg_num = outra.num*self.den
        
        return prim_num <= seg_num
    
    def __ne__(self, outra):

        prim_num = self.num*outra.den
        seg_num = outra.num*self.den
        
        return prim_num != seg_num
    

        
##### testes    
    
x = fracao(1,2)
y = fracao(2,3)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x == y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x != y)

    
    
