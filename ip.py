def is_valid_ipv4(address: str) -> bool:
    lista: list[str] = address.split('.')
    if len(lista) != 4:
        return False
    for elem in lista:
        for number in elem:
            if not number.isdigit():
                return False
        if not (0 <= int(elem) <= 255):
            return False
    return True
