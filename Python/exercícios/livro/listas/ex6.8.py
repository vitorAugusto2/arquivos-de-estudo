l = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))

x = 0
while x < len(l):
    if l[x] == p:
        print(f"{p} achado na posicao {x}")
        break
    x += 1
else:
    print(f"{p} nao encontrado")