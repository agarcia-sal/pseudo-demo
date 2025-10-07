def add(lst):
    total = 0
    length = len(lst)
    index = 1
    while index < length:
        element = lst[index]
        if element % 2 == 0:
            total += element
        index += 2
    return total