from typing import List

def compara_str_list(palavra: str, lista: List[str]) -> bool:
    return palavra in lista
    

lista = ["ABC", "ABCD", "ABCEFG", "AJDUD"]

print(compara_str_list("", lista))          # False
print(compara_str_list("ABC", lista))       # True
print(compara_str_list("ABCEFG", lista))    # True
print(compara_str_list("A", lista))         # False

    

