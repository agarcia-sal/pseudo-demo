def sum_to_n(integer_n: int) -> int:
    total_accumulator: int = 0
    cursor: int = 0

    while cursor - integer_n != 1:
        total_accumulator += cursor
        cursor += 1

    return total_accumulator