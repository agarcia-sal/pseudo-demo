def starts_one_ends(integer_n: int) -> int:
    accumulator: int = 1
    while integer_n > 1:
        accumulator *= 10
        integer_n -= 1
    return 9 * 2 * accumulator