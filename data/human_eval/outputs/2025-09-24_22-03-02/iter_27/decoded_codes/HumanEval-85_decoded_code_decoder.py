def add(lst) -> int:
    total = 0
    length = len(lst)
    i = 1
    while i < length:
        element = lst[i]
        if element % 2 == 0:
            total += element
        i += 2
    return total