def maior_numero(x: int, y: int) -> int:
    if x >= y:
        return x
    else:
        return y 

print(maior_numero(5, 6))
print(maior_numero(2, 1))
print(maior_numero(7, 7))