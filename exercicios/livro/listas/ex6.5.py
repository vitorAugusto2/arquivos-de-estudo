ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adcionar um cliente ao fim da fila,")
    print("ou A para relaizar o atendimento. S para sair")
    
    op = input("Digite os comandos (no maximo 10) de uma vez so: ")
    op = op.upper() 

    for letra in op:
        if letra == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila Vazia ! Ninguem para atender.")            
        elif letra == "F":
            ultimo += 1
            fila.append(ultimo)
        elif letra == "S":
            break
        else:
            print("Operacao invalida !") 