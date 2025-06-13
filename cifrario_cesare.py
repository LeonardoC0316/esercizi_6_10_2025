from string import ascii_lowercase, ascii_uppercase

def crifrario(s: str, k: int) -> str:
    l = ""
    for carattere in s:
        if carattere in ascii_lowercase:
            index = (ascii_lowercase.index(carattere) + k) % len(ascii_lowercase)
            l += ascii_lowercase[index]
        elif carattere in ascii_uppercase:
            index = (ascii_uppercase.index(carattere) + k) % len(ascii_uppercase)
            l += ascii_uppercase[index]
        else:
            l += carattere 
    return l

def decifrazione(s: str, k: int) -> str:
    l = ""
    for carattere in s:
        if carattere in ascii_lowercase:
            index = (ascii_lowercase.index(carattere) - k) % len(ascii_lowercase)
            l += ascii_lowercase[index]
        elif carattere in ascii_uppercase:
            index = (ascii_uppercase.index(carattere) - k) % len(ascii_uppercase)
            l += ascii_uppercase[index]
        else:
            l += carattere 
    return l

testo_cifrato = crifrario("Ciao mi chiamo Leonardo", 7)
print("Testo cifrato:", testo_cifrato)

testo_decifrato = decifrazione(testo_cifrato, 7)
print("Testo decifrato:", testo_decifrato)
