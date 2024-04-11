def valida(validas: str):
    validas = validas.lower()

    while True:
        op = str(input("Digite uma opcao: ")).lower()

        if op in validas:
            return op
        else:
            print("op invalida")




