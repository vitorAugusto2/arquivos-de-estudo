expressao = input("Digite a expressao de parenteses a validar: ")

pilha = []

for char in expressao:
    if char == "(":
        pilha.append("(")
    elif char == ")":
        if pilha and pilha[-1] == "(":
            pilha.pop()
        else:
            pilha.append(")")

if not pilha:
    print("OK")
else:
    print("Erro")
