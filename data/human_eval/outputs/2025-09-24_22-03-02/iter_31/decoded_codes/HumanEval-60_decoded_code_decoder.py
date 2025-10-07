def sum_to_n(n: int) -> int:
    total = 0
    index = 0
    while index <= n:
        total += index
        index += 1
    return total