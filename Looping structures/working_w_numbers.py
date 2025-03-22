import math
import sys 

#declaração de variáveis

# definição de funções


#classes
class PrimeNumbers:
    def prime_numbers(till_number):
        divisors = 0
        cont = 2
        list = []
        number = 2
        while number <= till_number:
            while cont <= number and divisors <=1:
                if number % cont == 0:
                    divisors += 1
                cont += 1
            if divisors == 1:
                    list.append(number)
            cont = 2 
            number += 1
            divisors = 0
        print(list)

    def is_prime(number):
        divisors = 0
        cont = 2
        list = []
        number
        while cont <= number and divisors <=1:
            if number % cont == 0:
                divisors += 1
            cont += 1
        if divisors == 1:
            return True
        elif number == 1:
            return True
        else:
            return False
        
class Palindromes:
    def pldrm_nbr(initial_number, final_number):
        number = initial_number
        lista = []
        while number <= final_number:
            numero_str=str(number)
            if numero_str==numero_str[::-1]:
                lista.append(number)
            number+=1
        print(lista)

    def is_pldrm(number):
        numero_str=str(number)
        if numero_str==numero_str[::-1]:
            return True
        else:
            return False
#código
