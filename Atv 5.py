'''5. (ExeMatriz05) Dadas duas matrizes A 5x5 e B 5x5 inicializadas pelo usuário
via teclado, criar e imprimir a matriz S sendo a soma de A e B.'''
matriz_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
matriz_b = [[26,27,28,29,30], [31, 32, 33, 34, 35],[36,37,38,39,40], [41, 42, 43, 44, 45],[46,47,48,49,50]]
matriz_s = [0] * 10
soma_matriz = []
# Como a questão ficou ambígua irei fazer as duas interpretações:

# Cenario 1 a junção das duas matrizes em uma só
for i in range(len(matriz_s)):
    if i < 5:
        matriz_s[i] = matriz_a[i]
    else:
        matriz_s[i] = matriz_b[i-5]

print(f"Matriz S: {matriz_s}")

# Cenario 2 a soma dos valores de cada indice
for i in range(len(matriz_s)):
    soma = 0
    soma += sum(matriz_s[i])
    soma_matriz.append(soma)

soma = 0
for i in range(len(soma_matriz)):
    soma += soma_matriz[i]
print(f"A soma dos componentes da matriz S: {soma_matriz}\nSoma total: {soma}")


