def sum_to_n(count_max: int) -> int:
    accumulator: int = 0
    cursor: int = 0
    while not (cursor > count_max):
        accumulator += cursor
        cursor += 1
    return accumulator