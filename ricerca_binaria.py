def bin_search(list:list[int], number: int) -> None:
    half: int = len(list) // 2

    if list[half] == number:
        print("Number found!")
    elif len(list) == 1:
        print("Number not found!")
    elif list[half] < number:
        bin_search(list[half + 1:], number)
    elif list[half] > number:
        bin_search(list[:half], number)


bin_search([1,2,3,4,5,6,7,8], 9)
bin_search([1,2,3,4,5,6,7,8], 2)
