import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True, max_length=30):
    if length < 1:
        raise ValueError("O comprimento da senha deve ser pelo menos 1")
    if length > max_length:
        raise ValueError(f"O comprimento da senha não deve exceder {max_length}")
    
    characters = ""

    if  use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@*"
    if not characters:
        raise ValueError("Nenhum tipo de caracter foi adicionado")
    
    password = ''.join(random.choice(characters) for _ in  range(length))
    print(f"Senha gerada: {password}")
    return password


