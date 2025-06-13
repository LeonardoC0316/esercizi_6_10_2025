def count_unique_words(stringa:str)-> dict[str: int]:
    elemento: list[str] = stringa.split()
    risultato: dict = {}
    for elemento in elemento:
        elemento = elemento.lower().strip(",.!?;:")
        if elemento:
            if elemento in risultato:
                risultato[elemento] += 1
            else:
                risultato[elemento] = 1
    return risultato
