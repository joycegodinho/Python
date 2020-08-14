# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 07:49:58 2020

@author: Joyce
"""



class Buscador:
    
    def busca_sequencial1(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return True
        return False

    def busca_sequencial2(self, lista, x):
        
        i = 0
        encontrado = False
        while i < len(lista) and not encontrado:
            if lista[i] == x:
                encontrado = True
            else:
                i = i + 1
        return encontrado
    
    def busca_sequencial_ordenada(self, lista, x):
        
        i = 0
        encontrado = False
        stop = False #interrompe a busca de o elemento na lista for maior que o buscado
        
        while i < len(lista) and not encontrado and not stop:
            if lista[i] == x:
                encontrado = True
            else:
                if lista[i] > x:
                    stop = True
                else:
                    i = i + 1
        return encontrado
            
    ##### busca binaria
    '''
    Essa busca é realizada em uma lista que já está ordenada.Em vez de procurar o item sequencialmente, 
    uma busca binária irá começar examinando o item do meio. Se esse elemento é o que estamos buscando, 
    a procura terminou. Se não for o item correto, podemos utilizar o fato da lista estar ordenada para 
    eliminar metade dela.
    Considere o elemento m do meio da lista e o elemento buscado x, 
    existem 3 casos:
    1- x == m
    2- x < m , busca apenas na primeira metade
    3- x > m , busca apenas na segunda metade
    Esse processo pode ser feito iterativamente.
    '''
       
    def busca_binaria(self, lista, x):
        
        primeiro = 0
        ultimo = len(lista) - 1 #len da o número de elementos na lista, como a contagem começa em 0, a posição do ultimo da lista é len - 1
        encontrado = False
        
        while primeiro <= ultimo and not encontrado:
            meio = (primeiro + ultimo)//2
            
            if lista[meio] == x:
                encontrado = True
                
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return encontrado
    
#### Testes    
    
def main():
    
    print("Testes com Busca Sequêncial")

    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]    
    
    s = Buscador() #chamo a classe

    print(s.busca_sequencial1(testlist, 3)) #chamo a função
    print(s.busca_sequencial1(testlist, 13))
    print(s.busca_sequencial1(testlist, 2))
    print(s.busca_sequencial1(testlist, -1))
    
    print("Testes com Busca Sequêncial 2")
    
    r = Buscador() #chamo a classe

    print(r.busca_sequencial2(testlist, 3)) #chamo a função
    print(r.busca_sequencial2(testlist, 13))
    print(r.busca_sequencial2(testlist, 2))
    print(r.busca_sequencial2(testlist, -1))
    
    print("Testes com Busca Sequêncial em lista ordenada")
    
    testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    
    t = Buscador() #chamo a classe

    print(t.busca_sequencial_ordenada(testlist2, 3)) #chamo a função
    print(t.busca_sequencial_ordenada(testlist2, 13))
    print(t.busca_sequencial_ordenada(testlist2, 0)) 
    print(t.busca_sequencial_ordenada(testlist2, -1))

    print("Testes com Busca Binária")
        
    u = Buscador() 

    print(u.busca_binaria(testlist2, 3))
    print(u.busca_binaria(testlist2, 13))
    print(u.busca_binaria(testlist2, 0))
    print(u.busca_binaria(testlist2, -1))
    
    
main()






