"""
Faça um programa que imprime uma sequência de n números em ordem
inversa à da leitura. Utilize uma lista para isso.
"""

l_original = [x for x in range(5)]
l_inversa = []

i = len(l_original) - 1

while i >= 0:
    num = l_original[i]
    l_inversa.append(num)
    i -= 1

print(f"Lista original = {l_original} \n Lista Inversa = {l_inversa}")