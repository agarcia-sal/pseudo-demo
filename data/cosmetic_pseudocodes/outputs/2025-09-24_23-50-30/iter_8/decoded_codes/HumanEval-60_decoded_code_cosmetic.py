def sum_to_n(integer_n: int) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator < integer_n + 1:
        accumulator += iterator
        iterator += 1
    return accumulator