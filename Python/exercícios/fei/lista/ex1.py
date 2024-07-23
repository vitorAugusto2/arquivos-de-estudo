"""
Crie um programa em que peça 10 números reais, armazene-os em uma
lista e diga qual é o índice do maior, e seu valor.
"""

l = []

for i in range(10):
    numero = int(input(f"[{i}] Digite o numero: "))
    l.append(numero)

indice_maior = 0
maior = 0

for i in range(len(l)):
    if l[i] > maior:
        maior = l[i]
        indice_maior = i


print(f"Lista = {l}")
print(f"Maior valor da lista = {max(l)}")
print(f"Posicao do maior: {indice_maior}")
