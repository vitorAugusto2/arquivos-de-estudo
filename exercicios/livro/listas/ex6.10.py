l = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
q = int(input("Digite o segundo valor a procurar: "))

x = 0
while x < len(l):
    if l[x] == p:
        print(f"{p} achado na posicao {x}")
    elif l[x] == q:
        print(f"{q} achado na posicao {x}")
    x += 1
else:
    print(f"Valor nao encontrado !")