def fibfib(integer_n: int) -> int:
    if integer_n <= 0:
        return 0
    if integer_n <= 1:
        return 0
    if integer_n <= 2:
        return 1

    total = 0
    index = 1
    while index < 4:
        total += fibfib(integer_n - index)
        index += 1

    return total