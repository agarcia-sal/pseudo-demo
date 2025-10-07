def add(lst):
    total = 0
    index = 1
    while index < len(lst):
        if lst[index] % 2 == 0:
            total += lst[index]
        index += 2
    return total