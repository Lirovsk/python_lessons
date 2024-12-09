def verifica_encaxe(n, pares):
    resultados = []
    for num_a, num_b in pares:
        if num_a.endswith(num_b):
            resultados.append("encaixa")
        else:
            resultados.append("não encaixa")
    return resultados

def main():
    try:
        # Leitura da quantidade de pares
        n = int(input().strip())

        # Leitura dos pares
        pares = []
        for _ in range(n):
            num_a = input().strip()
            num_b = input().strip()
            pares.append((num_a, num_b))

        # Verificação dos encaixes
        resultados = verifica_encaxe(n, pares)

        # Exibição dos resultados
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
