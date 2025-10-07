def sum_to_n(number_x: int) -> int:
    accumulator: int = 0
    index: int = 0

    while index <= number_x:
        accumulator += index
        index += 1

    return accumulator