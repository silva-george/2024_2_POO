import math
class Circulo:
    def __init__(self):
        self.__raio = 0
        self.__pi = 3.14
    def calc_area(self):
        return self.raio ** 2 * math.pi  
    def calc_circunferencia(self):
        return (2*self.pi) * self.raio
    def set_raio(self, v):
        if v > 0:
            self.raio = v
        else: raise ValueError("a altura do triângulo não pode ser negativa")
    def get_raio(self):
        return self.raio


x = Circulo()
x.set_raio (float(input("raio: ")))

operacao = int(input("Digite 1 para calcular a área ou 2 para calcular a circunferência: "))
if operacao == 1:
    print("a área do circulo é: ", x.calc_area())
else: print("a circunferência do circulo é: ", x.calc_circunferencia())