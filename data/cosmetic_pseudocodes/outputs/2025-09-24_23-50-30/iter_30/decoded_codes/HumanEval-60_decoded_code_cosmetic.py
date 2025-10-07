def sum_to_n(index_limit: int) -> int:
    accumulator: int = 0
    cursor: int = 0
    while not (cursor > index_limit):
        accumulator += cursor
        cursor += 1
    return accumulator