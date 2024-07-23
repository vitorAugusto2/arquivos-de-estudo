"""
Faça um programa que preencha uma lista com dez números inteiros
aleatórios (de 0 a 100). Calcule e mostre os números superiores a 50 e
suas respectivas posições. O programa deverá mostrar uma mensagem
caso não exista nenhum número nessa condição
"""

import random

l = [random.randint(0, 100) for i in range(10)]

print(f"Indice e Numeros superior a 50:")
for i in range(len(l)):
    if l[i] > 50:
        print(f"({i}, {l[i]})")
        
        