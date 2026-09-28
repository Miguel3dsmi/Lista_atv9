'''7. (ExeMatriz07) Escreva um algoritmo que leia uma matriz M[5][5] e que calcule e imprima as somas:
a) da linha 4 de M.
b) da coluna 2 de M.
c) da diagonal principal.
d) todos os elementos da matriz M.
e) Escrever também a matriz.
Dica para calcular a diagonal principal: if(i == j){soma += matrizM[i][j]}'''
import biblioteca

valor = int(input("Digite o valor da matriz quadrada (ex. 5x5=5, 6x6=6): "))
matriz = biblioteca.matriz_quadrada(valor) #------ E ------
diagonal = []

#------ A ------
linha = sum(matriz[4])

#------ B ------
soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j == 2:
            soma += matriz[i][j]

#------ C ------
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            diagonal.append(matriz[i][j])

#------ D ------
vetor = biblioteca.matriz4vetor(matriz,valor)
soma_total = sum(vetor)

print(f"A) Soma da linha 4: {linha}\nB) Soma da coluna 2: {soma}\n"
      f"C) Soma da diagonal principal: {diagonal}\nD) Soma da matriz: {soma_total}\nE) Escreva a matriz: {matriz}")