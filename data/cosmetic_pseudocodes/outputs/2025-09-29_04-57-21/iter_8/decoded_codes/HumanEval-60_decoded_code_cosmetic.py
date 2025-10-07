def sum_to_n(limit: int) -> int:
    accumulator: int = 0
    counter: int = 0
    while counter <= limit:
        accumulator += counter
        counter += 1
    return accumulator