'''4. (ExeMatriz04) Faça um algoritmo que gere randomicamente uma matriz de 10 X 10 de
inteiros. Calcule e mostre a soma das linhas pares da matriz.'''
import random

linha, coluna = 10, 10
matriz = [0] * linha
soma_matriz = []
soma_total = 0
soma_par = 0

for i in range (linha):
    matriz[i] = [0] * coluna
    for j in range (coluna):
        matriz[i][j] = random.randint(1, 30)
    if i % 2 == 0:
        soma = 0
        soma = sum(matriz[i])
        soma_matriz.append(soma)

for i in range(len(matriz)):
    soma_total += sum(matriz[i])
for i in range(len(soma_matriz)):
    soma_par += soma_matriz[i]

print(matriz)
print(soma_matriz)
print(soma_total)
print(soma_par)