import time
class bicicleta :
    def __init__(self, modelo, ano, valor, cor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.cor = cor
        self.buzina = "bi bi"
        self.andando = False
        self.freio = False
        self.parado = True
        self.pedalando = False
    
    def buzinar(self):
        print(self.buzina)
    
    def andar(self):
        if self.parado:
            self.freio = False
            self.pedalando = True
            self.parado = False
            print("Começando a pedalar")
            time.sleep(1)
            self.andando = True
            print("Andando")
            self.pedalando = False
        else:
            print("Você já está andando")
    
    def parar(self):
        if self.andando:
            self.freio = True
            print("Freando")
            time.sleep(1)
            self.andando = False
            self.parado = True
            print("Parado")
        else:
            print("Você já está parado")
    
    def __str__(self):
        return f"{self.__class__.__name__}: {' | '.join([f"{key} = {value}" for key, value in self.__dict__.items()])}"

b1 = bicicleta("Caloi", 2020, 1000, "Azul")
print(b1)