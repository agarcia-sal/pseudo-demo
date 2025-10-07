def sum_to_n(k: int) -> int:
    if k < 0:
        return 0
    accumulator = 0
    index = 0
    while index <= k:
        accumulator += index
        index += 1
    return accumulator