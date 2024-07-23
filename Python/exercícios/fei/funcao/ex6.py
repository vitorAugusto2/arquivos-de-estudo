"""
Escreva uma função que calcula o quociente e o resto da
divisão inteira entre dois números. Utilize apenas as operações
de soma e subtração para calcular o resultado. Dica: utilize uma
estrutura de repetição para isso.

Faça um programa principal que recebe o dividendo e o divisor
do usuário e, depois de chamar a função, exibe o quociente e o
resto.
"""

def exibe_quociente_resto(dividendo: int, divisor: int) -> int:
    quociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    resto = dividendo
    print(f"Quociente: {quociente} - Resto: {resto}")

print(exibe_quociente_resto(10, 2))
