def sum_to_n(actual_number: int) -> int:
    interim_total: int = 0
    cursor: int = 0
    while cursor <= actual_number:
        interim_total += cursor
        cursor += 1
    return interim_total