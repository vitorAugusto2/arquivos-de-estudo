def mdc(a: int, b: int ) -> int:
    if b == 0:
        return a
    return mdc(b, a % b)
    
def mmc(a: int, b: int) -> int:
    return abs(a * b) / mdc(a, b)


mdc(10, 5)
mmc(10, 5)