def sum_to_n(delta: int) -> int:
    total: int = 0
    index: int = 0
    while index <= delta:
        total += index
        index += 1
    return total