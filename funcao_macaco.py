# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:21:36 2020

@author: joyce
"""

'''
Teorema do macaco infinito. A frase que vamos filmar é: "acho que é como uma doninha"

A maneira como simularemos isso é escrever uma função que 
gera uma string com 27 caracteres, escolhendo letras 
aleatórias das 26 letras do alfabeto mais o espaço. 

Escreveremos outra função que marcará cada sequência 
gerada comparando a sequência gerada aleatoriamente com a meta.

Uma terceira função chamará repetidamente gerar e marcar, e 
se 100% das letras estiverem corretas, terminamos. Se as 
letras não estiverem corretas, geraremos toda uma nova string. 
Para facilitar o acompanhamento do progresso do programa, essa 
terceira função deve imprimir a melhor string gerada até agora e 
sua pontuação a cada 1000 tentativas.
'''

import random
import string

# Primeira: função que gera um string de 27 caracteres

def geradora():
    
   gerada = [] 
   
   for l in range (27):
       gerada.append(random.choice(string.ascii_lowercase + " "))
   return gerada
       


# Segunda: compara a sequencia gerada com a meta

meta = "acho que é como uma doninha"

def contador(meta, tentativa):
    
    cont = 0
    for i in range(len(meta)):
        if meta[i] == tentativa[i]:
            cont = cont + 1
    return cont
            



# Terceira: chamará repetidamente a primeira e a segunda 


def macaco():
    c = 0
    melhor_contador = 0
    melhor_gerada = ""
    tentativa = geradora()
    tentativa_contador = contador(meta, tentativa)
     
    while tentativa_contador != 27:
        tentativa = geradora()
        tentativa_contador = contador(meta, tentativa)
        c = c + 1
        
        if tentativa_contador > melhor_contador:
            melhor_contador = tentativa_contador
            melhor_gerada = tentativa
            
        if c % 1000 == 0:
            print("Tentativa: %d\nMelhor pontuação: %d\nMelhor string: %s"
                % (c, melhor_contador, melhor_gerada))
    print("Encontrado")
    
    
macaco()
            
            
            
















