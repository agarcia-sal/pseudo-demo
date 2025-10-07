def add(lst):
    total = 0
    length = len(lst)
    i = 1
    while i < length:
        element = lst[i]
        remainder = element % 2
        if remainder == 0:
            total += element
        i += 2
    return total