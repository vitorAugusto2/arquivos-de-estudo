"""
Escreva uma função chamada exponencial que recebe um valor
n passado por valor e dois inteiros b e k passados por
“referência". Sua função deve retornar em b e k valores tal que
b**k = n e b seja o menor possível.
"""

def exponencial(n: int, b: int, k: int) -> int:
# 2**3 = 2 * 2 * 2 = n(8), caso n = 20 decrementa até achar o menor possivel
    while n > 1:
        if b**k == n:
            return n
        else:
            n -= 1

print(exponencial(12, 2, 3))