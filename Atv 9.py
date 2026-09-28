'''9. (ExeMatriz09) Faça um algoritmo que leia uma matriz 3x3 e após a leitura multiplique cada
elemento da diagonal principal pela média do valor de todos os elementos.'''
import biblioteca

valor = int(input("Digite o valor da matriz quadrada (ex. 5x5=5, 6x6=6): "))
matriz = biblioteca.matriz_quadrada(valor)
mult,diagonal = [],[]

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            mult.append(matriz[i][j])

vetor = biblioteca.matriz4vetor(matriz,valor)
media = sum(vetor)/len(vetor)

for i in range (len(mult)):
    media_total = mult[i] * media
    diagonal.append(media_total)

print(diagonal)

