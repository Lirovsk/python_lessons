import sys
import time

class TEXTO:
    MENU = """O que deseja fazer?
    1 - Depositar
    2 - Sacar
    3 - Transferir
    4 - Ver saldo
    5 - investir
    6 - Sair
    """
    pass
class conta:
    def __init__(self):
        self.nome = input("Digite o nome do titular da conta: ")
        self.cpf = input("Digite o CPF do titular da conta: ")
        self.idade = int(input("Digite a idade do titular da conta: "))
        self.saldo = 1500

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado com sucesso.")
        
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    
    def investir(self):
        if self.acesso_inves == True:
            print("Você tem acesso a investimentos.")
        else:
            print("Você não tem acesso a investimentos.")

    def transferir(self):
        print("oi")

class conta_corrente(conta):
    def __init__(self):
         #using 'super' to inherit the attributes from the parent class
        super().__init__()
        if self.idade < 18:
            print("Conta corrente não pode ser aberta para menores de 18 anos.")
        
        else:
            self.agencia = input("Digite a agência da conta: ")
            self.n_conta = input("Digite o número da conta: ")
            self.acesso_inves = True
        
    def transferir (self):
        valor = float(input("Digite o valor que deseja transferir: "))
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Transferência de R${valor} realizada com sucesso.")
        else:
            print("Saldo insuficiente.")

    def saldo_conta(self):
        print(f"Seu saldo é de R${self.saldo}.")
    
    
class conta_poupanca(conta):
    def __init__(self):
        #using 'super' to inherit the attributes from the parent class
        super().__init__()
        self.agencia = input("Digite a agência da conta: ")
        self.n_conta = input("Digite o número da conta: ")
        self.acesso_inves = False
        pass
    
    def transferir (self):
        print("Você não pode transferir de uma conta poupança.")

    def saldo_conta(self):
        print(f"Seu saldo da sua poupança é: R${self.saldo}.")

def transferencia(conta):
    #defining one function to work with both classes of accounts
    conta.transferir()
    return

def main():
    print("Bem vindo ao banco do povo!")
    time.sleep(1)
    print("Vamos abrir uma conta para você!")
    time.sleep(1)
    print("primeiro crie uma conta corrente")
    conta1 = conta_corrente()
    print("Agora crie uma conta poupança")
    conta2 = conta_poupanca()
     
    while True:
        anwser = input("qual conta deseja usar? conta 1 ou 2?")
        if anwser == "1":
            conta_ = conta1
        else:
            conta_ = conta2
        print(TEXTO.MENU)
        opcao = input("Digite o número correspondente a opção desejada: ")
        if opcao == "1":
            valor = float(input("Digite o valor que deseja depositar: "))
            conta_.deposito(valor)

        elif opcao == "2":
            valor = float(input("Digite o valor que deseja sacar: "))
            conta_.saque(valor)
            
        elif opcao == "3":
            transferencia(conta_)

        elif opcao == "4":
            conta_.saldo_conta()

        elif opcao == "5":
            conta_.investir()

        elif opcao == "6":
            print("Obrigado por utilizar nossos serviços!")
            sys.exit()

if __name__ == "__main__":
    main()