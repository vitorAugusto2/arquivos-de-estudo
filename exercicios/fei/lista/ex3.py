""""
Faça um programa para criar uma lista de 10 elementos (pedir para o
usuário) e apresentar: a soma dos ELEMENTOS pares e a soma dos
elementos de ÍNDICE par
"""

l = [x for x in range(10)]

soma_pares = 0
soma_indice = 0

for indice, elemento in enumerate(l): 
    if elemento % 2 == 0:
        soma_pares += elemento
    if indice % 2 == 0:
        soma_indice += elemento

print(soma_pares, soma_indice)