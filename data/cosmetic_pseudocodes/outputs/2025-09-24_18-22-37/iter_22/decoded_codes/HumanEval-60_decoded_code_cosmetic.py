def sum_to_n(amount: int) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator <= amount:
        accumulator += iterator
        iterator += 1
    return accumulator