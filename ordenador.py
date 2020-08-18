# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:02:02 2020

@author: Joyce
"""

import time
class Ordenador:

            
    '''
    O bubble sort realiza múltiplas passagem por uma lista. Ele compara 
    itens adjacentes e troca aqueles que estão fora de ordem. O maior 
    valor na lista será continuamente empurrado até o fim da passagem.
    Se existem n itens na lista, então existem n−1 pares de itens que precisam 
    ser comparados na primeira passagem.No começo da segunda passagem, o maior 
    valor agora está ordenado. Ainda existem n−1 itens para serem ordenados, o 
    que significa que teremos n−2 pares de comparação. Como cada passagem colocar o 
    próximo maior valor encontrado no lugar certo, o número total de passagens 
    necessárias será n−1. 
    '''
    
    def bubbleSort(self,lista):
        
        antes = time.time()
        
        for i in range(len(lista)-1, 0, -1): #range (start, stop, step). Esse for vai definir o número de passagens
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        
        depois = time.time()
                    
        return lista, depois - antes
    
    '''
    A ordenação por seleção melhora o bubble sort ao realizar apenas uma troca a 
    cada passagem pela lista. Para conseguir isso, uma ordenação por seleção 
    procura pelo valor mais alto enquanto faz uma passagem e, depois de completá-la, 
    coloca-o na posição correta. Assim como o bubble sort, depois da primeira passagem, 
    o maior item sempre está na posição correta. Depois da segunda passagem, o próximo 
    maior item também vai para a posição adequada. O processo continua dessa forma e 
    demanda n−1 passagens para ordenar n itens,
    '''
    
    def selectionSort(self, lista):
        
        antes = time.time()
        for i in range(len(lista)-1, 0, -1):
            posicao_do_maximo = 0
            
            for j in range(1, i + 1):
                if lista[j] > lista[posicao_do_maximo]:
                    posicao_do_maximo = j
                    
            #para trocar de lugar os elementos na posição i e posicao_do_máximo
            lista[i], lista[posicao_do_maximo] = lista[posicao_do_maximo], lista[i]
        
        depois = time.time()
        return lista, depois - antes
    
    '''
    Cria uma sublista e a cada passagem retira um item da lista de input e insere
    ordenadamente na sublista. Começamos pressupondo que uma lista com um único 
    item (posição 0) está ordenada. A cada passagem, do item 1 a n−1, uma vez que 
    esses são os itens que precisam ser inseridos nas sublistas ordenadas, o item atual 
    é comparado com os que já estão na sublista ordenada. 
    '''
    def insertionSort(self, lista):
        
        antes = time.time()
        for i in range(1, len(lista)):
            valor_atual = lista[i]
            
            while i > 0 and lista[i - 1] > valor_atual:
                lista[i] = lista[i - 1]
                i = i - 1
            
            lista[i] = valor_atual
            
        depois = time.time()    
        return lista, depois - antes
    
    '''
    O shell sort, às vezes chamaado de “ordenação por incrementos diminutos”, melhora 
    a ordenação por inserção ao quebrar a lista original em um número menor de sublistas, 
    as quais são ordenadas usando a ordenação por inserção. A forma única como essas sublistas 
    são escolhidas é a chave para o shell sort. Em vez de quebrar a lista em sublistas de 
    itens contíguos, o shell sort usa um incremento i, às vezes chamado de gap, para criar 
    uma sublista escolhendo todos os itens que estão afastados i itens uns dos outros. Finalmente
    é realizada uma ordenação por inserção final usando um incremento de um; em outras palavras, 
    uma ordenação por inserção convencional.  Ao realizar as ordenações de sublistas anteriores, 
    reduzimos agora o número total de operações de deslocalmento necessárias para colocar a lista 
    na sua ordem final
    '''
    
    def shellSort(self, lista):
        
        antes = time.time()
        gap = len(lista)//2
        
        while gap > 0: #loog sobre os gaps
            for i in range(gap, len(lista)): # faz o insertion sort
                valor_atual = lista[i]
                
                while i > gap and lista[i - gap] > valor_atual:
                    lista[i] = lista[i - gap]
                    i = i - gap
                
                lista[i] = valor_atual
                
            gap = gap // 2
            
        depois = time.time()   
        return lista, depois - antes    

    '''
    O merge sort, é um algoritmo recursivo que divide uma lista continuamente pela metade. Se a 
    lista estiver vazia ou tiver um único item, ela está ordenada por definição (o caso base). 
    Se a lista tiver mais de um item, dividimos a lista e invocamos recursivamente um merge sort 
    em ambas as metades. Assim que as metades estiverem ordenadas, a operação fundamental, chamada 
    de intercalação, é realizada. Intercalar é o processo de pegar duas listas menores ordenadas e 
    combiná-las de modo a formar uma lista nova, única e ordenada.
    '''

    def mergeSort(self, lista):  
        

        antes = time.time()
        if len(lista) >  1:

            meio = len(lista) // 2
            esquerdo = lista[:meio]
            direito = lista[meio:]
            
            lado_direito = Ordenador() #chamo a classe
            lado_direito.mergeSort(direito) #chamo a função
            
            lado_esquerdo = Ordenador()
            lado_esquerdo.mergeSort(esquerdo) #pressupõe que as lista já estão ordenadas
            

            i = 0
            j = 0
            k = 0
        
            while i < len(esquerdo) and j < len(direito):
                if esquerdo[i] < direito[j]:
                    lista[k] = esquerdo[i]
                    i = i + 1
                else:
                    lista[k] = direito[j]
                    j = j + 1
                k = k + 1
                
            while i < len(esquerdo):
                
                    lista[k] = esquerdo[i]
                    i = i + 1
                    k = k + 1
                    
            while j < len(direito):
                
                    lista[k] = direito[j]
                    j = j + 1
                    k = k + 1

        depois = time.time()        
        return lista, depois - antes
                
    '''
    O quick sort primeiro seleciona um valor, chamado de pivô. Embora existam muitas maneiras de 
    selecionar o pivô, iremos utilizar simplesmente o primeiro item na lista. O papel do pivô é 
    ajudar na divisão da lista. A posição à qual o pivô pertence de fato na lista ordenada, conhecida 
    como ponto de divisão, será usada para quebrar a lista em chamadas subsequentes do quick sort.
    O processo de partição ocorrerá em seguida. Ele irá encontrar o ponto de divisão e, ao mesmo tempo, 
    moverá os itens para o lado apropriado da lista, isto é, maior ou menor que o valor do pivô.
    '''     

    def quickSort(self,lista): #só aceita len(lista) impar
        
        antes = time.time() 
        if len(lista) < 2:
            return lista
        
        else:
            pivot = len(lista)//2
            menor = [i for i in lista if i < lista[pivot]]
            meio = [i for i in lista if i == lista[pivot]]
            maior = [i for i in lista if i > lista[pivot]]
            
            
            menor_ = Ordenador()
            menor_.quickSort(menor)
            meio_ = Ordenador()
            meio_.quickSort(meio)
            maior_ = Ordenador()
            maior_.quickSort(maior)
        
        depois = time.time()
        return menor + meio + maior, depois - antes
        

                
    '''
    se durante uma passagem não houver trocas, então sabemos que a lista está ordenada. O bubble sort 
    pode ser modificado para terminar antes se descobrir que a lista ficou ordenada. Isso significa 
    que para listas que requerem apenas algumas passagens, o bubble sort pode ter a vantagem de 
    reconhecer a lista ordenada e parar. 
    '''                
    def shortBubble(self,lista):
        
        antes = time.time()
        fim = len(lista) - 1
        trocou = True
        
        while fim > 0 and trocou:
            trocou = False
            for j in range(fim):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou = True
            fim =fim - 1
        
        depois = time.time()
        return lista, depois - antes
            
            
            
#### Testes  
        
import random
    
def main():


    testlist = []  
    
    for i in range(0, 21):
        n = random.randint(1, 100)
        testlist.append(n)
        
    
    print("Testes com Bubble Sort")
    
    s = Ordenador() #chamo a classe

    print(s.bubbleSort(testlist)) #chamo a função
    
    print("Testes com Ordenação Por Seleção")
     
    r = Ordenador() #chamo a classe

    print(r.selectionSort(testlist))    
    
    print("Testes com Ordenação Por Inserção")
     
    t = Ordenador() #chamo a classe

    print(t.insertionSort(testlist))  
    
    print("Testes com Shell Sort")
     
    u = Ordenador() #chamo a classe

    print(u.shellSort(testlist))  

    
    print("Testes com Merge Sort")
     
    v = Ordenador() #chamo a classe

    print(v.mergeSort(testlist)) 
    
    '''
    print("Testes com Quick Sort")
     
    x = Ordenador() #chamo a classe

    print(x.quickSort(testlist)) 
    '''
        
    
    print("Testes com Short Bubble")
     
    w = Ordenador() #chamo a classe

    print(w.shortBubble(testlist)) 
    
main()            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
