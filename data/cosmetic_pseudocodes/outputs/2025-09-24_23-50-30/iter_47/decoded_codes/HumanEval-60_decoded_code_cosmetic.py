def sum_to_n(index_end: int) -> int:
    accumulated_sum = 0
    iterator = 0

    while iterator <= index_end:
        accumulated_sum += iterator
        iterator += 1

    return accumulated_sum