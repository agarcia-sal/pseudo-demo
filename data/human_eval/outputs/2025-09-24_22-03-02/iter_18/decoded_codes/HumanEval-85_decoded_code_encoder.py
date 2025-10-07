def add(lst):
    result = 0
    length = len(lst)
    index = 1
    while index < length:
        if lst[index] % 2 == 0:
            result += lst[index]
        index += 2
    return result