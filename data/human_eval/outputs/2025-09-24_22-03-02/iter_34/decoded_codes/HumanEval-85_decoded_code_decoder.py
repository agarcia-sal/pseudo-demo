def add(lst):
    result = 0
    i = 1
    while i < len(lst):
        if lst[i] % 2 == 0:
            result += lst[i]
        i += 2
    return result