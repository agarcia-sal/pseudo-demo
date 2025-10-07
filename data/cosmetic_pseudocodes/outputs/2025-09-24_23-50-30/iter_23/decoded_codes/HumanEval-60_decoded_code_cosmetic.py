def sum_to_n(delta: int) -> int:
    accumulator: int = 0
    cursor: int = 0
    while cursor <= delta:
        accumulator += cursor
        cursor += 1
    return accumulator