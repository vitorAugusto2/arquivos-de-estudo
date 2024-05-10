"""
Existem restrições para que uma pessoa possa doar sangue.
Uma delas é relativa ao peso. Mulheres tem que pesar no
mínimo 50kg e homens no mínimo 60kg. Faça uma função para
informar se uma pessoa está ou não apta a doar sangue
sabendo seu sexo e seu peso.
O programa principal deve ler as entradas, acionar a função e
exibir a resposta.
"""


# mulher > 50 : homem > 60


def apta_sangue(sexo: str, peso: float) -> str:
    if sexo == "mulher" and peso >= 50:
        print("Esta apta a doar sangue") 
    else:
        print("nao tem peso suficente para doar sangue")

    if sexo == "homem" and peso >= 60:
        print("Esta apta a doar sangue") 
    else:
        print("nao tem peso suficente para doar sangue")
    

print(apta_sangue("mulher", 40))
print(apta_sangue("mulher", 60))

print(apta_sangue("homem", 45))
print(apta_sangue("homem", 70))