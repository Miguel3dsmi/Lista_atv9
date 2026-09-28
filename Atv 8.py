'''8. (ExeMatriz08) Faça um algoritmo que calcule a média dos elementos da diagonal principal
de uma matriz 10X10 de inteiros.'''
import biblioteca
valor = int(input("Digite o valor da matriz quadrada (ex. 5x5=5, 6x6=6): "))
matriz = biblioteca.matriz_quadrada(valor)
media =[]
contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            media.append(matriz[i][j])
print(matriz)
print(sum(media)/len(media))