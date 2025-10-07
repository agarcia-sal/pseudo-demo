def sum_to_n(integer_n: int) -> int:
    accumulator: int = 0
    counter: int = 0
    while counter <= integer_n:
        accumulator += counter
        counter += 1
    return accumulator