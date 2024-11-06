import random
from random import randint

class Bingo():
    def __init__(self):
        self.__numBolas = 0
        self.__bolas = []

    def set_num_bolas(self, n_b):
        self.__numBolas = n_b
    
    def proximo(self,):
        n = 0
        numero_aleatorio = random.randint(1, self.__numBolas)
        while n <= len(self.__bolas):
            if numero_aleatorio in self.__bolas:
                numero_aleatorio = random.randint(1, self.__numBolas)
            else:
                self.__bolas.append(numero_aleatorio)
            n = n+1
        # return numero_aleatorio
    
    def sorteados(self):
        return self.__bolas        
        
class Cartela():
    def __init__(self):
        self.__ns_cartela = []
        while n <= 10:
            if numero_aleatorio in self.__ns_cartela:
                numero_aleatorio = random.randint(1, self.__numBolas)
            else:
                self.__ns_cartela.append(numero_aleatorio)
            n = n+1

class Jogador():
    def set_cartela(self, Cartela):
        cartela = Cartela


x= Bingo()
x.set_num_bolas(10)
for i in range(0, 10):
    x.proximo()

print(x.sorteados())
