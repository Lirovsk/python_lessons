''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
"""C = int(input()) 
for i in range (C): 
    hp_level = input()
    if int(hp_level) > 8000:
        print("Mais de 8000!")
    else:
        print("Inseto!")"""
def calcular_refrigerantes(N, K):
    total_bebidas = N
    garrafas_vazias = N

    
    novas_bebidas = garrafas_vazias // K
    total_bebidas = (total_bebidas-(K *novas_bebidas)) + novas_bebidas
    garrafas_vazias = garrafas_vazias % K + novas_bebidas

    return total_bebidas

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    resultado = calcular_refrigerantes(N, K)
    print(resultado)
