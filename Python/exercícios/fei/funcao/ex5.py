"""
Faça uma função que receba três notas de um aluno como
parâmetros e uma letra. Se a letra for A, a função deverá
calcular a média aritmética das notas do aluno; se for P deverá
calcular a média ponderada com pesos 5, 3 e 2. A média
calculada deve ser devolvida à função principal para, então, ser
mostrada.
"""


def notas_alunos(n1: float, n2: float, n3: float, letra: str) -> float:
    # A: media aritmetica
    if letra == "A":
        return (n1+n2+n3) / 3
        
    # P: media ponderada (5, 3 e 2)
    elif letra == "B":
        return (n1*5 + n2*3 + n3*2) / 10


print(notas_alunos(5, 8, 7, "A"))
print(notas_alunos(5, 8, 7, "B"))
