import math
from multiprocessing import Value
class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0

    def set_distancia(self, d):
        if d > 0:
            self.__distancia = d
        else: raise ValueError ("distancia precisa ser positiva")
    
    def set_tempo(self, t):
        if t > 0:
            self.__tempo = t
    def get_distancia(self):
        d = self.__distancia
        return d
    def get_tempo(self):
        t = self.__tempo
        return t

    def velocidade_media(self):
        return self.__distancia / self.__tempo

x = Viagem()
x.set_distancia (float(input("distancia: ")))
x.set_tempo (float(input("tempo: ")))
print("a velocidade media em KM/h é: ", x.velocidade_media())