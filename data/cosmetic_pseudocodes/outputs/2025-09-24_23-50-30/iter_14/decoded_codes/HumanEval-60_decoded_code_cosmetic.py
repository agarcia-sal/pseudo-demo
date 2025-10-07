def sum_to_n(number_m: int) -> int:
    accumulator: int = 0
    index: int = 0
    while index <= number_m:
        accumulator += index
        index += 1
    return accumulator