"""
O uso dos decoradores funciona ao chamar uma função que recebe como argumento outra função, dessa forma conseguimos 
realizar ações de maneira sistémica sem poluir o código.
Para entender como os decoradores funcionam, vamos primeiro criar uma função e chamar ela de dentro de outra função como argumento.
"""
from functools import wraps


def saudacao(nome):
    print(f"olá {nome}")
    
def fazer_saudacao(funcao):
    nome = input("Qual o seu nome? ").title()
    funcao(nome)
    
fazer_saudacao(saudacao)

"""
Com esse primeiro exemplo é possível ver como o python consegue receber funções como argumentos.
Agora vamos para um próximo passo: onde iremos definir uma função dentro de outra função. 
"""
def definindo_funcao():
    def dizer_ola():
        print("oi")
    return dizer_ola()

definindo_funcao()

"""
Com esse exemplo podemos enxergar que não só é possível definir funções dentro de outras funções, como também é possível usar funções como valor de retorno.
Abaixo camos criar o primeiro decorador. Será de maneira simples, mas ainda sim será um decorador.
"""
def meu_decorador(func):
    print("antes da função ser chamada")
    func()
    print("depois da função ser chamada")
    
def dizer_peido():
    print("peidei")
    
meu_decorador(dizer_peido)

"""
ainda que náo contenha toda a sintaaxe de um decorador completo, ssa é a lógica por trás de um decorador em python: um conjunto de lógicas a serem executadas
antes e depois da execução de uma função
"""
def decorador(func):
    @wraps(func)  # Preserva o nome e a docstring da função original
    def wrapper(*args, **kwargs):
        print("Antes da função ser chamada")
        resultado = func(*args, **kwargs)
        print("Depois da função ser chamada")
        return resultado
    return wrapper


@decorador
def minha_funcao(nome):
    """Essa é uma função de exemplo."""
    print(f"Olá, {nome}!")
    
minha_funcao("João")