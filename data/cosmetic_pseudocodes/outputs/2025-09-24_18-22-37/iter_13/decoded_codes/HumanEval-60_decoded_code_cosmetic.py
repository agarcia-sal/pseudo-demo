def sum_to_n(counter_limit: int) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator <= counter_limit:
        accumulator += iterator
        iterator += 1
    return accumulator