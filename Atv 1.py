'''(ExeMatriz01) Faça um algoritmo que gere aleatoriamente uma matriz de inteiros 7 x 9,
imprima a matriz e calcule e imprima a soma dos seus elementos.'''
import random
linhas = 7
colunas = 9

matriz = [0] * linhas
for i in range(len(matriz)):
    matriz[i] = [0] * colunas

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(1, 10)
        print(f"{matriz[i][j]:2} ", end="")
    print()