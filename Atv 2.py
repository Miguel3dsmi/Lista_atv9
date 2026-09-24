'''2. (ExeMatriz02) Dada uma matriz M[1..6][1..8] criada randomicamente, criar um vetor C que
contenha em cada posição a quantidade de elementos negativos da linha correspondente de
M. Tamanho de C igual ao número de linhas da matriz. Imprimir o vetor C ao final.'''
import random
linha = 6
coluna = 8
c = [0] * linha
matriz = [0] * linha

for i in range(len(matriz)):
    matriz[i] = [0] * coluna

for i in range(linha):
    for j in range(coluna):
        matriz[i][j] = random.randint(-10, 10)
        print(f"{matriz[i][j]:2} ", end="")
        if matriz[i][j] < 0:
            c[i] +=1
    print()
print(f"Linhas de C: {c}")
