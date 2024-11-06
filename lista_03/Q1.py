from cmath import sqrt
import math
class Retangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0
    
    def set_base(self, v):
        if v > 0: self.__b = v
        else: raise ValueError("a base do retangulo não pode ser negativa")
   
    def set_altura(self, v):
        if v > 0: self.__h = v
        else: raise ValueError("a altura do retangulo não pode ser negativa")
   
    def get_base(self):
        return self.__b
    
    def get_altura(self):
        return self.__h
   
    def calc_area(self):
        return self.__b * self.__h  
    def calcDiagonal (self):
        return sqrt((self.__b*self.__b)+(self.__h*self.__h))

    def __str__(self) :
        frase = f"A base do retangulo é: {self.__b}  A altura do retangulo é:  {self.__h}"
        return frase


x= Retangulo()
print(x)