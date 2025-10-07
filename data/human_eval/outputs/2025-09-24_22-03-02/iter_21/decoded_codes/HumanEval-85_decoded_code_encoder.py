def add(lst):
    total = 0
    length = len(lst)
    for i in range(1, length, 2):
        element = lst[i]
        if element % 2 == 0:
            total += element
    return total