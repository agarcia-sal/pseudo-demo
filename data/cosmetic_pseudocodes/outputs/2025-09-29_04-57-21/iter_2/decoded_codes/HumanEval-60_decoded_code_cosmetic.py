def sum_to_n(integer_n: int) -> int:
    accumulator: int = 0
    counter: int = integer_n
    while counter >= 0:
        accumulator += counter
        counter -= 1
    return accumulator