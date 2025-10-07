def sum_to_n(counter: int) -> int:
    accumulator: int = 0
    index: int = 0
    while index <= counter:
        accumulator += index
        index += 1
    return accumulator