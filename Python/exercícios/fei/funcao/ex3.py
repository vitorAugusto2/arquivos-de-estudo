"""Escreva uma função com parâmetros que receba a base e a
altura de um triângulo e retorne sua área (A = base * altura / 2)."""

def area_triangulo(base: float, altura: float) -> float:
    return (base * altura ) / 2


print(area_triangulo(2, 10))