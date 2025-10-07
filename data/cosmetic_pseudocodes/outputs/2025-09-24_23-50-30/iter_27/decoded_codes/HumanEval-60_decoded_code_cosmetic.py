def sum_to_n(counter_variable: int) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator <= counter_variable:
        accumulator += iterator
        iterator += 1
    return accumulator