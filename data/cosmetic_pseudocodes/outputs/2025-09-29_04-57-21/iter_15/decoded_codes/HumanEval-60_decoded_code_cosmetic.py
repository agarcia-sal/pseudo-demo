def sum_to_n(integer_n: int) -> int:
    tally = 0
    index = 0
    while index <= integer_n:
        tally += index
        index += 1
    return tally