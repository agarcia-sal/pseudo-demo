def sum_to_n(integer_n: int) -> int:
    accumulator: int = 0
    iterator: int = 0
    while iterator <= integer_n:
        temp: int = accumulator + iterator
        accumulator = temp
        iterator += 1
    return accumulator