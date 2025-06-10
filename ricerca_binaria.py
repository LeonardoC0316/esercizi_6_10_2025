def ricerca_binaria(lista: list[int], numero: int) -> bool:
    sinistra = 0
    destra = len(lista) - 1

    while sinistra <= destra:
        centro = (sinistra + destra) // 2
        if lista[centro] == numero:
            return True
        elif lista[centro] < numero:
            sinistra = centro + 1
        else:
            destra = centro - 1

    return False


numeri = [2, 4, 5, 7, 10, 22, 45]
print(ricerca_binaria(numeri, 10)) 
print(ricerca_binaria(numeri, 23))  