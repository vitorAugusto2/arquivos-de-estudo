"""
Escreva uma função com parâmetros que retorne o maior de
dois números. A função deve se chamar maximo(x, y).
"""

def maior_numero(x: float, y: float) -> None:
    if x > y:
        print(x)
    else:
        print(y)

maior_numero(5, 2)