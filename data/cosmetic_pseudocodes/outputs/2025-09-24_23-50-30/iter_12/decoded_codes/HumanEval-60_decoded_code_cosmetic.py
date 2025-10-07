def sum_to_n(delta: int) -> int:
    accumulator: int = 0
    index: int = 0
    while index <= delta:
        accumulator += index
        index += 1
    return accumulator