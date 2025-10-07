def sum_to_n(upper_bound: int) -> int:
    total_accumulator: int = 0
    current_index: int = 0
    while current_index <= upper_bound:
        total_accumulator += current_index
        current_index += 1
    return total_accumulator