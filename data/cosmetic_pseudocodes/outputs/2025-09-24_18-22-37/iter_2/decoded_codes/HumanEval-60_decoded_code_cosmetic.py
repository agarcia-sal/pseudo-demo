def sum_to_n(number_limit: int) -> int:
    accumulator: int = 0
    index: int = 0
    while index <= number_limit:
        accumulator += index
        index += 1
    return accumulator