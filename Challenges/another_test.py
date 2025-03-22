#n = int(input())
#n_aux= 0
#matrix = [[0 for x in range(2)] for y in range(n)]
#while n_aux < n:
#    matrix [n_aux][0] = 0
#    matrix [n_aux][1] = 1
#    n_aux += 1

#print(matrix)


n = int(input())
n_aux= 0
matrix = []
NUM_A = 0
NUM_B = 1
RESULTADO = 2

while n_aux < n:
    matrix.append([])
    matrix [n_aux].append(str(input()))
    matrix [n_aux].append(str(input()))
    n_aux += 1

n_aux = -1
comander = 0
for linha in range(len(matrix)):
    comander = 0
    if len(matrix[linha][NUM_B]) > len(matrix[linha][NUM_A]):
            matrix[linha].append("nao encaixa")
            comander = 10
    else:
        for n in range(len(matrix[linha][NUM_B])):
            if matrix[linha][NUM_A][n_aux] == matrix[linha][NUM_B][n_aux]:
                n_aux -= 1
            else:
                if comander == 10:
                    continue
                else:
                    matrix[linha].append("nao encaixa")
                    comander = 10
                    continue
            if n_aux == -(len(matrix[linha][NUM_B])):
                matrix[linha].append("encaixa")
    n_aux = -1

for linha in range(len(matrix)):
    print(matrix[linha][RESULTADO])
           