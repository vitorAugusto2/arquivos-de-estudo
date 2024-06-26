from typing import List

def soma(lista: List[int]) -> int:
    soma = 0

    for i in range(len(lista)):
        soma += lista[i]
    
    return soma

lista = [1, 7, 2, 9, 15]
print(soma(lista))
