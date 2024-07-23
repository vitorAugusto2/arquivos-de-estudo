"""
Neste exercício, você criará um programa que lê palavras do usuário até que
o usuário entre com uma linha em branco. Após o usuário digitar uma linha
em branco, seu programa deve exibir cada palavra digitada pelo usuário
exatamente uma vez. As palavras devem ser exibidas na mesma ordem em
que foram inseridas. Por exemplo, se o usuário inserir:
""" 

l = []

while True:
    palavra = str(input("Escreva uma palavra: "))
    if palavra == " ": 
        break
    elif palavra not in l:
        l.append(palavra)

print(f"\n{l}")