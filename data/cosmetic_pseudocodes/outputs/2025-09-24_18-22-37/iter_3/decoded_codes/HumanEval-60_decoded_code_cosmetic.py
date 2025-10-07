def sum_to_n(integer_n: int) -> int:
    total = 0
    index = 0
    while index <= integer_n:
        total += index
        index += 1
    return total