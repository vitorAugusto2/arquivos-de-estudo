from typing import List 

def pesquise(lista: List[int], valor: int) -> int:
    if valor in lista:
        return lista.index(valor)
    
lista = [10, 20, 25, 30]
print(pesquise(lista, 25))
print(pesquise(lista, 27))
