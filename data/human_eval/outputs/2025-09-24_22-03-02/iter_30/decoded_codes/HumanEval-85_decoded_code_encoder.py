def add(lst) -> int:
    total = 0
    index = 1
    while index < len(lst):
        element = lst[index]
        if element % 2 == 0:
            total += element
        index += 2
    return total