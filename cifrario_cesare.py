from string import ascii_lowercase
def cifrario(s:str, k:int) -> str:
    l:str = ""

    for carattere in s:
        index: int = ascii_lowercase.index(carattere)
        index = (index + k) % len(ascii_lowercase)
        l += ascii_lowercase[index]
    return l


print(cifrario_cesare("ciao", 28))
print(decifra("ekcq", 28))
