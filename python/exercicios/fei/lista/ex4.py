"""
Faça um programa para criar uma lista de 10 elementos inteiros e
apresentar todos os conteúdos que forem maiores que a soma de dois
de seus antecessores
"""

l = []

for i in range(10):
    num = int(input("Digite o numero: "))
    l.append(num)

print(f"\n Lista = {l}")

print("\nNumeros maiores que a soma de dois de seus antecessores : ")
for i in range(len(l) - 2):
    if l[i + 2] > l[i] + l[i + 1]:
        print(l[i + 2])