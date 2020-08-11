# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:52:07 2020

@author: joyce
"""
###Estruturas de dados lineares

'''
Pilhas, filas, deques e listas são exemplos de estruturas de dados lineares. 
O que distingue uma estrutura linear de outra é a maneira pela qual os itens 
são adicionados e removidos, em particular o local onde essas adições e 
remoções ocorrem.
'''

class Pilha: #os itens são adicionados e removidos apenas na frente
    
    def __init__(self):
        self.itens = []
        
    def vazia(self):
        
        return self.itens == [] #retorna um boleano
    
    def push(self, item):
        
        self.itens.append(item)
        
    '''
    push(item)adiciona um novo item ao topo da pilha. Ele 
    precisa do item e não retorna nada.
    '''
        
    def pop(self):
        
        return self.itens.pop()
    
    '''
    pop()remove o item superior da pilha. Ele não precisa de 
    parâmetros e retorna o item. A pilha é modificada.
    '''
    
    def peek(self):
        
        return self.itens[len(self.itens) - 1]
    
        '''
    peek()retorna o item superior da pilha, mas não o remove. 
    Não precisa de parâmetros. A pilha não é modificada.
    '''
    
    def tamanho(self):
        
        return len(self.itens)
    


class Fila: #os itens são adicionados e removidos apenas atrás
    
    def __init__(self):
        self.itens = []
        
    def vazia(self):
        
        return self.itens == [] #retorna um boleano
    
    def adc(self, item):
        
        self.itens.insert(0, item)
        
    '''
    adc(item)adiciona um novo item ao final da fila. Ele 
    precisa do item e não retorna nada.
    '''
        
    def pop(self):
        
        return self.itens.pop()
    
    '''
    pop()remove o item frontal da fila. Ele não precisa de 
    parâmetros e retorna o item. A pilha é modificada.
    '''
    

    def tamanho(self):
        
        return len(self.itens)
    
class Deque: #os itens são adicionados e removidos apenas na frente, presumirá que a parte traseira do deque está na posição 0 na lista.
    
    def __init__(self):
        self.itens = []
        
    def vazia(self):
        
        return self.itens == [] #retorna um boleano
    
    def adcFrente(self, item): #adiciona um novo item à frente do deque
        
        self.itens.append(item)
    
    def adcTras(self, item): #adiciona um novo item na parte traseira do deque
        
        self.itens.insert(0, item)
        
    def retiraFrente(self): #remove o item da frente do deque
        
        return self.itens.pop()
    
    def retiraTras(self): #remove o item traseiro do deque
        
        return self.itens.pop(0)
    
    def tamanho(self):
        
        return len(self.itens)
    
############# lista não ordenada
        
'''
Cada objeto de nó deve conter pelo menos duas informações. Primeiro, o nó 
deve conter o próprio item da lista. Chamaremos isso de campo de dados do 
nó. Além disso, cada nó deve conter uma referência ao próximo nó.
'''

class Node:
    
    def __init__(self, inicdata):
        
        self.data = inicdata
        self.next = None
        
    def getData(self):
        
        return self.data
    
    def getNext(self):
        
        return self.next
    
    def setData(self, novodata):
        
        self.data = novodata
        
    def setNext(self, novonext):
        
        self.next = novonext
        
        
class ListaDesordenada:
    
    def __init__(self):
        
        self.head = None
        self._tamanho = 0
        self._ultimo = None


    def para_python (self): #retorna a lista desordenada como uma lista python regular
               
        current = self.head
        python_lista = []
        
        while current != None:
            
            python_lista.append(current.getData())
            current = current.getNext()
            
        return python_lista
    
    def __str__ (self): 
               
        current = self.head
        strings = []
        
        while current != None:
            
            strings.append(str(current.getData()))
            current = current.getNext()
            
        return "Lista Desordenada: " + strings
        
    def isEmpty(self):
        
        return self.head == None

    def add(self,item): #adiciona no começo da lista
        
        new_head = Node(item)
        new_head.setNext(self.head)
        
        if self.head == None:
            self._ultimo = new_head
        
        self.head = new_head
        self._tamanho = self._tamanho + 1
        
    def tamanho(self):

        return self._tamanho

    def procura(self,item):
        
        current = self.head
        found = False
        
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        
        current = self.head
        previous = None
        found = False
        
        while not found: 
            
            if current.getData() == item:
                found = True
                self._tamanho = self._tamanho - 1
            else:
                previous = current
                current = current.getNext()

        if previous == None: 
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def append(self, item): #adiciona um novo item à frente
        
        if self.head == None:
            self.add(item)    
        else:
            new_node = Node(item)
            self._ultimo.setNext(new_node)
            self._ultimo = new_node
            self._tamanho = self._tamanho + 1

    
    def insert(self, i, item): #adiciona um novo item em determinada posição 
        
        count = 0
        current = self.head
        previous = None
        
        while count < i and current != None:
            previous = current
            current = current.getNext()
            count = count + 1
            
        if current == None:
            if count == 1:
                self.append(item)
        else:
            if previous == None:
                self.add(item)
            else:
                new_node = Node(item)
                previous.setNext(new_node)
                new_node.setNext(current)
                
                self._tamanho = self._tamanho + 1
                
    def indice(self,item): #retorna o indice do item procurado
        
        current = self.head
        found = False
        count = 0
        
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                count = count + 1

        if found == False:
            return found
        else:
            return count

                
    def pop(self): #remove o item do final
        
       if self.head == None:
           return ("Lista Vazia")
       else:
           current = self.head
           if current.getNext() == 0: #lista com um elemento
               popped = self.head
               self.head = None
               self._ultimo = None
           else:
               previous = None
               while current.getNext() != None:
                   previous = current
                   current = current.getNext()
                   
               popped = current
               self._ultimo = previous
               previous.setNext(None)
               
           self._tamanho = self._tamanho - 1
           
           return popped.getData()
              
    
    def ultimo(self): #retorna o último elemento da lista 

       if self.head == None:
           return ("Lista Vazia")
       else:
            return self._ultimo.getData()

############# lista não ordenada  
            
class ListaOrdenada:
    
    def __init__(self):
        
        self.head = None
        
    def isEmpty(self):
        
        return self.head == None

    def add(self,item): #adiciona no começo da lista
              
        current = self.head
        previous = None
        stop = False
        
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
        
    def tamanho(self):

        current = self.head
        count = 0
        
        while current != None:
            count = count + 1
            current = current.getNext()
        
        return count

    def procura(self,item):
        
        current = self.head
        found = False
        stop = False
        
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self,item):
        
        current = self.head
        previous = None
        found = False
        
        while not found: 
            
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None: 
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


##### TESTES
        
def main():
    
    print("Testes com Pilhas - LIFO")
    
    s = Pilha()
    
    print(s.vazia())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.tamanho())
    print(s.vazia())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.tamanho())

    
    print("Testes com Filas - FIFO")
    
    q = Fila()
    
    print(q.vazia())
    q.adc(4)
    q.adc('dog')
    print(q.tamanho())
    print(q.vazia())
    print(q.pop())
    print(q.tamanho())
    
    print("Testes com Deques")
    
    d = Deque()
    
    print(d.vazia())
    d.adcTras(4)
    d.adcTras('dog')
    d.adcFrente('cat')
    d.adcFrente(True)
    print(d.tamanho())
    print(d.vazia())
    d.adcTras(8.4)
    print(d.retiraTras())
    print(d.retiraFrente())
    
    print("Testes Listas Desordenadas")
    

    l = ListaDesordenada()
    
    l.add(31)
    l.add(77)
    l.add(17)
    l.add(93)
    l.add(26)
    l.add(54)
    
    print(l.tamanho())
    print(l.procura(93))
    print(l.procura(100))
    print(l.indice(93))
    print(l.indice(100))
    l.add(100)
    print(l.procura(100))
    print(l.tamanho())
    l.remove(54)
    print(l.tamanho())
    l.append(93)
    print(l.tamanho())
    l.insert(2, 31)
    print(l.tamanho())
    print(l.indice(93))
    l.pop()
    print(l.tamanho())
    print(l.ultimo())
    print(l.para_python())
    
    
    print("Testes Listas Desordenadas")
    
    j = ListaOrdenada()
    
    j.add(31)
    j.add(77)
    j.add(17)
    j.add(93)
    j.add(26)
    j.add(54)
    
    print(j.tamanho())
    print(j.procura(93))
    print(j.procura(100))
    j.add(100)
    print(j.procura(100))
    print(j.tamanho())
    j.remove(54)


main()
