class Conta_bancaria():
    def __init__(self):
        self.__nome = ""
        self.__numero_da_conta = 0
        self.__saldo = 0
    
    def set_nome(self, n):
        self.__nome = n
    def set_numero(self, n):
        self.__numero_da_conta = n    
    def get_nome(self):
        return self.__nome
    def get_numero(self):
        return self.__nome
    def get_saldo(self):
        return self.__saldo 
    def deposito(self, s):
        self.__saldo = self.__saldo + s

    def saque(self, s):
        if self.__saldo > 0:
            self.__saldo = self.__saldo - s
        elif (self.__saldo <= 0) or (self.__saldo < s):
            print("Saldo insuficiente")

c = Conta_bancaria()

c.set_nome(input("""Digite o nome do titular: 
"""))
c.set_numero(int(input("""Digite o numero da conta:
""")))
operacao = int(input("""[1] Ver saldo
[2] Deposito
[3] Saque """))

if operacao == 1:
    print("Seu saldo é: ", c.get_saldo())   
elif operacao == 2:
    c.deposito(float(input("Qual valor deseja depositar em sua conta? \n")))
elif operacao == 3:
    c.saque(float(input("Qual valor deseja sacar de sua conta? \n")))


