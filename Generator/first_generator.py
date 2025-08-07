def generator(numeros: list[int]):
    for numero in numeros:
        yield numero * 2
        

# Test the generator function
lista = [1, 2, 3, 4, 5]
for numero in generator(lista):
    print(numero)