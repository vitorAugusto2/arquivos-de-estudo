ultimo = 10
fila1 = list(range(1, ultimo + 1))
fila2 = list(range(1, ultimo + 1))

while True:
    print(f"""
        \n---------+ FILA 1 +---------
        \nExistem {len(fila1)} clientes na fila
        \nFila atual: {fila1}
        \n -> Digite 'A' para atendimento fila 1
        \n -> Digite 'B' para atendimento fila 2
          """)
    
    print(f"""
        \n---------+ FILA 2 +---------
        \nExistem {len(fila2)} clientes na fila
        \nFila atual: {fila2}
        \n -> Digite 'F' para chegada fila 1
        \n -> Digite 'G' para chegada fila 2
          """)
    
    print(f"\nDigite 'S' para sair\n")
    
    op = input("Digite os comandos (no maximo 10) de uma vez so: (Exemplo: 'AAFGGBBS') ").upper()

    for letra in op: 
        if letra == "A":
            if len(fila1) > 0:
                atendido = fila1.pop(0)
                print(f"Cliente {atendido} atendido da fila 1")
            else:
                print("Fila Vazia ! Ninguem para atender.")            
        elif letra == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido da fila 2")
            else:
                print("Fila Vazia ! Ninguem para atender.")       
        elif letra == "F":
            ultimo += 1
            fila1.append(ultimo)
        elif letra == "G":
            ultimo += 1
            fila2.append(ultimo)
        elif letra == "S":
            break
        else:
            print("Operacao invalida !") 