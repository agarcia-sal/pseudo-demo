def sum_to_n(parameter_x: int) -> int:
    accumulator: int = 0
    cursor: int = 0
    while cursor <= parameter_x:
        accumulator += cursor
        cursor += 1
    return accumulator