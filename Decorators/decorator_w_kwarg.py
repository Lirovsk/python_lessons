# Nessa seção vamos entender melhor o comportamento de **Kwargs para garantir um funcionamento adequador do decorador

from functools import wraps

def decorator_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for item in args:
            if item < 0:
                raise ValueError("Argumentos devem ser positivos")
        else:
            return func(*args, **kwargs)
    return wrapper


def decorator_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'multplier' not in kwargs:
            raise TypeError("Missinh on argument")
        else:
            return func(*args, **kwargs)
    return wrapper

    
@decorator_1    
def print_number(number: int):
    """imprime um número."""
    print(number)

@decorator_2
def multiply(number: int, multplier: int):
    """multiplica dois números."""
    return number * multplier

print(multiply(5, multplier=3))


print_number(10)  # Deve funcionar normalmente
try:
    print_number(-5)  # Deve levantar um ValueError
except ValueError as e:
    print(e)