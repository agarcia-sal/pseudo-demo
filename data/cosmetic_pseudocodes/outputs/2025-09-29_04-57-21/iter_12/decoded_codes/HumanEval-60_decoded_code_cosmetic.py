def sum_to_n(integer_n: int) -> int:
    accumulator: int = 0
    index: int = 0

    while index <= integer_n:
        accumulator += index
        index += 1

    return accumulator