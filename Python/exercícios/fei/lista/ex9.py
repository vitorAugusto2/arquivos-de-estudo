"""
Faça um programa que crie uma lista com vinte números inteiros
aleatórios (de 0 a 200). Ordene, então, essa lista de forma crescente
"""

import random

l = [random.randint(0, 200) for i in range(20)]

print(f"Lista original = {l}")
print(f"Lista crescente = {sorted(l)}")