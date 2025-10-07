def sum_to_n(delta: int) -> int:
    accumulator: int = 0
    for index in range(delta + 1):
        accumulator += index
    return accumulator