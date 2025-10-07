def sum_to_n(integer_n: int) -> int:
    total: int = 0
    index: int = 0
    while index <= integer_n:
        total += index
        index += 1
    return total