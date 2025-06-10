def cifrario_cesare(testo: str, chiave: int) -> str:
    risultato = ""
    chiave = chiave % 26
    for carattere in testo:
        if 'a' <= carattere <= 'z':
            spostato = (ord(carattere) - ord('a') + chiave) % 26 + ord('a')
            risultato += chr(spostato)
        elif 'A' <= carattere <= 'Z':
            spostato = (ord(carattere) - ord('A') + chiave) % 26 + ord('A')
            risultato += chr(spostato)
        else:
            risultato += carattere
    return risultato

def decifra(testo: str, chiave: int) -> str:
    risultato = ""
    chiave = chiave % 26
    for carattere in testo:
        if 'a' <= carattere <= 'z':
            spostato = (ord(carattere) - ord('a') - chiave) % 26 + ord('a')
            risultato += chr(spostato)
        elif 'A' <= carattere <= 'Z':
            spostato = (ord(carattere) - ord('A') - chiave) % 26 + ord('A')
            risultato += chr(spostato)
        else:
            risultato += carattere
    return risultato


print(cifrario_cesare("ciao", 28))
print(decifra("ekcq", 28))