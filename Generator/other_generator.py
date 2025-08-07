# Nesse primeiro caso o gerador multiplica os números de uma lista por números de 1 ao limite estabelicido.
def generator(numeros: list[int], number: int):
    limit =0
    while limit < number:
        for numero in numeros:
            yield numero * (limit + 1)
            print('==' * 20)
        
        limit += 1

lista = [1, 2, 3, 4, 5]
    
for numer in generator(lista, 4):
    print(numer)

# Nesse segundo caso o gerador multiplica os número de 1 ao número dado por números de 1 ao limite estabelecido.
def second_generator(numero: int):
    limit = 0
    while limit < numero:
        numero_ = 1
        while numero_ <= numero:
            yield numero_ * (limit + 1)
            numero_ += 1
        limit += 1
        
for numero in second_generator(4):
    print(numero)