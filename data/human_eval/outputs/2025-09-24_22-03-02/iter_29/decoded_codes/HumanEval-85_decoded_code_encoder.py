def add(lst) -> int:
    result = 0
    length = len(lst)
    for i in range(1, length, 2):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result