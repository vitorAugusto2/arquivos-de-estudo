def valid_str(palavra: str, num_mim: int, num_max: int) -> bool:
    tam = len(palavra)

    if tam >= num_mim and tam <= num_max: 
        return True
    else: 
        return False
    
    

print(valid_str("", 1, 5))
print(valid_str("ABC", 2, 5))
print(valid_str("ABCEFG", 3, 5))
print(valid_str("ABCEFG", 1, 10))