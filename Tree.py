# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 11:26:46 2020

@author: joyce
"""
####### Árvore Binária 

from orientado_estruturas_lineares import Fila

ROOT = "root"

class Node: #contem os dados e duas referencia que permite ligar ao proximo nó
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)
    
class BinaryTree: #o importante é a raiz, pois a partir dela voce chega a qualquer lugar da arvore
    
    def __init__ (self, data=None, node = None):
        
        if node:
            self.root = node
        
        elif data:
            node = Node(data) #crio um nó com o dado e atribuo a raiz a ele
            self.root = node     
        else:
            self.root = None
        
    def inorder(self, node = None): #percurso simétrico: esq-centro-dir
        
        if node is None:
            node = self.root #se o nó for vazio, comece o percurso da raiz
            

        if node.left:
            self.inorder(node.left) #self permite acessar não so as variaveis self como as funções que começam com self
            
        print(node, end=' ') 
        
        if node.right:
            self.inorder(node.right)          
        
    def preorder(self, node = None): 
        
        if node is None:
            node = self.root #se o nó for vazio, comece o percurso da raiz

        print(node, end='')     

        if node.left:
            self.preorder(node.left) #self permite acessar não so as variaveis self como as funções que começam com self
                    
        if node.right:
            self.preorder (node.right) 
            
    def posorder(self, node = None): #só exibe o nó depois de percorre à esquerda e à direita
        
        if node is None:
            node = self.root #se o nó for vazio, comece o percurso da raiz
            
        if node.left:
            self.posorder(node.left) #self permite acessar não so as variaveis self como as funções que começam com self
                   
        if node.right:
            self.posorder(node.right) 
            
        print(node, end='') 
        
    def height(self, node = None): #altura da árvore
        
        if node is None:
            node = self.root 
        
        hleft = 0
        hright = 0
            
        if node.left:
            hleft = self.height(node.left) 
                   
        if node.right:
            hright = self.height(node.right) 
        
        if hright > hleft:           
            return hright + 1
        else:
            return hleft + 1
            
    def levelorder(self, node=ROOT): 
        
        if node == ROOT:
            node = self.root 
            
        fila = Fila() #os itens são adicionados pela frente  e removidos apenas atrás (primeiro a entrar, primeiro a sair)
        fila.adc(node)
        
        while (fila.tamanho()):
            node = fila.pop()
            
            if node.left:
                fila.adc(node.left)
            if node.right:
                fila.adc(node.right)
            print(node, end=" ")
             
            
## árvore binária de busca: a esquerda sempre haverá valores menores que o nó e a direita, maiores
class BinarySearchTree(BinaryTree):
    
    def insert(self, value):
        
        parent = None
        x = self.root
        
        while(x):
            parent = x
            if value < x.data:
                x = x.left
                
            else:
                x = x.right
                
        if parent is None:
            self.root = Node(value)
            
        elif value < parent.data:
            parent.left = Node(value)
            
        else:
            parent.right = Node(value) 
            
    def search(self, value, node = 0):
        
        if node == 0:
            node = self.root
       
        if node is None: 
            return node
        if node.data == value:
            return BinarySearchTree(node)
        
        if value < node.data:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)
        
    def min(self, node=ROOT): #menor valor é o primeiro que não tem filhos à esquerda
        
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT): #maior valor é o primeiro que não tem filhor à direita
        
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data
    
    '''
    Para manter a estrutura da árvore existem 3 casos de remoção:
    1. Folha, nada precisa ser feito
    2. apaneas 1 filho ou 1 braço, liga-se esse diretamente ao pai original
    3. 2 braços, em que o menor entre os maiores (à direita), assume o lugar do retirado e avalia-se o caso do substituto
    '''

    def remove(self, value, node=ROOT):

        if node == ROOT: #caso base
            node = self.root
            
        if node is None:
            return node
        
        if value < node.data:
            node.left = self.remove(value, node.left) # recursão sobre o caminho esquerdo
            
        elif value > node.data:
            node.right = self.remove(value, node.right) 
       
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                subst = self.min(node.right)
                node.data = subst
                node.right = self.remove(subst, node.right)
      
        return node
    
class BinHeap: #porque é uma arvore binaria completa, permite sua representação atraves de uma lista        

    def __init__(self):
        
        self.heapList = [0]
        self.currentSize = 0
        
    '''
    o insert anexa o item ao final da lista e provavelmente violará a propriedade 
    da estrutura do heap, corrigido através de um método que nos permitirá recuperar 
    a propriedade da estrutura do heap, comparando o item recém-adicionado com seu pai. 
    Se o item recém-adicionado for menor que seu pai, então podemos trocar o 
    item por seu pai.
    '''
    def percUp(self, i):
        
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2
            
    def insert(self, k):
        
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    '''
    Como a propriedade heap requer que a raiz da árvore seja o menor item da árvore, 
    é fácil encontrar o item mínimo. A parte difícil delMin é restaurar a conformidade  
    total com a estrutura de heap e propriedades de ordem de heap após a remoção da raiz. 
    Podemos restaurar nosso heap em duas etapas. Primeiro, iremos restaurar o item raiz 
    pegando o último item da lista e movendo-o para a posição raiz. Mover o último item 
    mantém nossa propriedade de estrutura de heap. No entanto, provavelmente destruímos a 
    propriedade de ordem do heap de nosso heap binário. Em segundo lugar, restauraremos a 
    propriedade de ordem do heap empurrando o novo nó raiz para baixo na árvore até sua 
    posição adequada.
    '''

    def percDown(self, i):
        
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc
            
    def minChild(self, i):
        
        if i * 2 + 1 > self.currentSize:
            return i*2
        
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
        
    def delMin(self):
        
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)   
        return retval
        
    '''
    No método para construir um heap, embora comecemos no meio da árvore e voltemos 
    em direção à raiz, para diminuir o numero de trocas, o percDownm é todo garante que o 
    filho maior sempre seja movido para baixo na árvore. Como o heap é uma árvore binária 
    completa, quaisquer nós além do ponto médio serão folhas e, portanto, não terão filhos. 
    '''
    
    def buildHeap(self, alist):
        
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        
        while i > 0:
            self.percDown(i)
            i = i - 1
            
    
#######################TESTES###################################
         
import random
    
def main():
    
    testlist = []  
    
    for i in range(0, 42):
        n = random.randint(1, 1000)
        testlist.append(n)
###############################################################
        
    print("Testes com construção inorder de Árvore Binária")
   
    b = BinarySearchTree() #chamo a classe
    
    for j in testlist:
        b.insert(j)
        
    b.inorder()

###############################################################
    
    print("\n") 
    print("Testes com construção por nível de Árvore Binária")
   
    c = BinarySearchTree() #chamo a classe
    
    for j in testlist:
        c.insert(j)
        
    c.levelorder()
 
###############################################################
    
    print("\n")     
    print("Testes em Árvore Binária de Busca")
    
    itens = [1, 3 ,981, 510, 1000]
    
    for k in itens:
        
        r = b.search(k)
        
        if r is None:
            print(k, "Não Encontrado")
            
        else:
            print(r.root.data, "Encontrado")
###############################################################
            
    print("\n")        
    print("Testes com máximo e mínimo em Árvore Binária de Busca")
    
    print("Máximo:", b.max())
    print("Mínimo:", b.min())

###############################################################
    
    print("\n")        
    print("Testes com remoção em Árvore Binária de Busca")
    
    testlist2 = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    
    t = BinarySearchTree()
    
    for w in testlist2:
        t.insert(w)
        
    x = 61
    
    t.remove(x)
    print("Após remover {}".format(x))
    t.inorder() 
    print("\n") 
    t.levelorder()

###############################################################
    
    print("\n")        
    print("Testes com Bin Heap")
    
    testlist3 = [9,5,6,2,3]
    bh = BinHeap()
    
    bh.buildHeap(testlist3)
    
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())   
        
main()
    
    