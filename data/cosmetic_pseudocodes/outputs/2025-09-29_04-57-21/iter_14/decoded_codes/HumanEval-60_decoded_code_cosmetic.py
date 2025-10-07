def sum_to_n(integer_n: int) -> int:
    cumulative_total: int = 0
    iterator_index: int = 0

    while iterator_index <= integer_n:
        cumulative_total += iterator_index
        iterator_index += 1

    return cumulative_total