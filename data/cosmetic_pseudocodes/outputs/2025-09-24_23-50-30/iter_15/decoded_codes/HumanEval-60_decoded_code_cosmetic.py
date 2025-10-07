def sum_to_n(alpha: int) -> int:
    total_storage: int = 0
    index_counter: int = 0

    while not (index_counter > alpha):
        total_storage += index_counter
        index_counter += 1

    return total_storage