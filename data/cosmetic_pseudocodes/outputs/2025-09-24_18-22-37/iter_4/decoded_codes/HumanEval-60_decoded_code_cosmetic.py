def sum_to_n(number_limit: int) -> int:
    total_sum: int = 0
    current_index: int = 0
    while current_index <= number_limit:
        total_sum += current_index
        current_index += 1
    return total_sum