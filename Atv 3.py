'''3. (ExeMatriz03) Faça um algoritmo que gere randomicamente uma matriz de 5 X 5 de inteiros
positivos e mostre a soma de cada coluna separadamente.'''
import random

numero = 1
matriz = []
matriz_soma = []
linha, coluna = 5, 5
soma = 0

matriz = [0] * linha

for i in range(linha):
    matriz[i] = [0] * coluna
    for j in range(coluna):
        matriz[i][j] = random.randint(1, 100)

for j in range(coluna):
    soma = 0
    for i in range(linha):
        soma += matriz[i][j]
    matriz_soma.append(soma)

print(matriz)
print(matriz_soma)
