l = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar: "))
q = int(input("Digite o segundo valor a procurar: "))
primeiro = 0

x = 0
while x < len(l):
    if l[x] == p:
        print(f"{p} achado na posicao {x}")
        if not p:
            primeiro = 1

    elif l[x] == q:
        print(f"{q} achado na posicao {x}")
        if not q:
            primeiro = 2
    x += 1

if primeiro == 1:
    print(f"Primeiro valor encontrado foi: {p}")
else:
    print(f"Primeiro valor encontrado foi: {q}")
