"""
Escreva uma função com parâmetros chamada multiplo(x, y).
Esta função deve receber dois números e retornar True se o
primeiro for múltiplo do segundo número; a função retorna
False caso contrário.
"""

def multiplo(x: int, y: int) -> bool:
    return x % y == 0



print(multiplo(5, 10))