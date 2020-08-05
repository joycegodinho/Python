# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:43:34 2020

@author: joyce
"""
#Implementação de um circuito lógico orientado à objetos (F:0 e V:1)
'''
No topo da hierarquia,a porta lógica apresenta uma etiqueta
para identificação (label) e a saída dos métodos.
'''
class PortaLogica:
    
    def __init__(self, n):
        
        self.label = n
        self.output = None
        
    def Label(self):
        
        return self.label
    
    def Output(self):
        
        self.output = self.logica()
        return self.output
    


'''
O portão AND possui duas linhas de entrada. O portão OR também 
possui duas linhas de entrada. A BinaryGateclasse será uma subclasse 
de LogicGatee adicionará duas linhas de entrada. 
'''
class EntradaBinaria(PortaLogica):
    
    
    def __init__(self, n):
        
        PortaLogica.__init__(self, n) # herdadndo as variáveis de __init__ da classe mãe PortaLogica
        self.pinA = None
        self.pinB = None
        
    def getPinA(self):
        
        if self.pinA == None:      
            return int(input("Digite a entrada do pin A para a porta "+ self.Label()+"-->"))
        else:
            return self.pinA.getFrom().Output()
        
    def getPinB(self):
        
        if self.pinB == None:
            return int(input("Digite a entrada do pin B para a porta "+ self.Label()+"-->"))
        else:
            return self.pinB.getFrom().Output()
    
    '''
    Precisamos adicionar esse método às nossas classes de gateways, 
    para que cada umtogatepossa escolher a linha de entrada apropriada 
    para a conexão.Para portões com duas linhas de entrada possíveis, o 
    conector deve ser conectado a apenas uma linha. Se os dois estiverem 
    disponíveis, escolheremos pinApor padrão. Se pinAjá estiver conectado, 
    escolheremos pinB. Não é possível conectar a um portão sem linhas de 
    entrada disponíveis.
    
    '''
            
    def proximoPin(self, fonte):
        
        if self.pinA == None:
            self.pinA == fonte
            
        else:
            if self.pinB == None:
                self.pinB == fonte
                
            else:
                raise RuntimeError("Sem pins disponíveis")
    
class PortaAND(EntradaBinaria):
    
    def __init__(self, n):
        
        EntradaBinaria.__init__(self, n)
        
    def logica(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
#Os NandGates funcionam como AndGates que possuem um Not anexado à saída.
            
class PortaNAND(EntradaBinaria):
    
    def __init__(self, n):
        
        EntradaBinaria.__init__(self, n)
        
    def logica(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 and b==1:
            return 0
        else:
            return 1
        
class PortaOR(EntradaBinaria):
    
    def __init__(self, n):
        
        EntradaBinaria.__init__(self, n)
        
    def logica(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 or b ==1:
            return 1
        else:
            return 0
#O NorGates trabalha no lago OrGates que possui um Não anexado à saída.       

class PortaNOR (EntradaBinaria):
    
    def __init__(self, n):
        
        EntradaBinaria.__init__(self, n)
        
    def logica(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if a == 1 or b ==1:
            return 0
        else:
            return 1
        
class PortaXOR (EntradaBinaria):
    
    def __init__(self, n):
        
        EntradaBinaria.__init__(self, n)
        
    def logica(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if (a == 1 and b ==1):
            return 0
        elif (a==0 and b==1) or (a==1 and b==0):
            return 1
        else :
            return 0
        
'''
Half adder é um circuito aritmético combinacional que adiciona 
dois números e produz um bit de soma (S) e bit de transporte (C) 
como saída. Se A e B são os bits de entrada, o bit de soma (S) é o
 X-OR de A e B e o bit de transporte (C) será o AND de A e B.
'''
        
class HalfAdder (EntradaBinaria):
    
    def __init__(self, n):
        
        EntradaBinaria.__init__(self, n)
        
    def logica(self):
        
        a = self.getPinA()
        b = self.getPinB()
        
        if (a == 1 and b ==1):
            return 0
        elif (a==0 and b==1) or (a==1 and b==0):
            return 1
        else :
            return 0
        
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        

'''
Os portões NOT têm uma linha de entrada. A UnaryGateclasse também 
terá subclasse, LogicGatemas terá apenas uma única linha de entrada.
'''

class EntradaUnitaria(PortaLogica):
    
    def __init__(self, n):
        
        PortaLogica.__init__(self, n)
        self.pin = None
        
    def getPin(self):
        
        if self.pin == None:
            return int(input("Digite a entrada do pin para a porta "+ self.Label()+"-->"))
        else:
            return self.getFrom().Output()
        
    def proximoPin(self, fonte):
        
        if self.pin == None:
            self.pin == fonte
            
        else:
            raise RuntimeError("Sem pins disponíveis")
        

class PortaNOT(EntradaUnitaria):
    
    def __init__(self, n):
        
        EntradaUnitaria.__init__(self, n)
        
    def logica(self):
        
        c = self.getPin()
        
        if c == 1:
            return 0
        else:
            return 1
'''
essa classe conectará a saída de uma porta à entrada de
outra porta. HAS-A: não faz parte da hierarquia do programa.

'''

class Conector:
    
    def __init__(self, porta_from, porta_to):
        
        self.porta_from = porta_from
        self.porta_to = porta_to
        
        porta_to.proximoPin(self)
        
    def getFrom(self):
        
        return self.porta_from
        
    
    def getTo(self):
        
        return self.porta_to
    
def main():
    
    g1 = PortaAND("G1")
    g2 = PortaAND("G2")
    g3 = PortaOR("G3")
    g4 = PortaNOT("G4")
    c1 = Conector(g1, g3)
    c2 = Conector(g2, g3)
    c3 = Conector(g3, g4)
    
    print(g4.Output())

main()



