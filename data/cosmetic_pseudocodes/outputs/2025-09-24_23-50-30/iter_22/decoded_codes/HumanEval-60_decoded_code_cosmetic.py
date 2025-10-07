def sum_to_n(delta: int) -> int:
    total = 0
    index = 0
    while index <= delta:
        total += index
        index += 1
    return total