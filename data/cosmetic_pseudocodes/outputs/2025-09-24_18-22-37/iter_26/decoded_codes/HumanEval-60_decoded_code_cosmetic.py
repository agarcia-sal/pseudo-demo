def sum_to_n(x_val: int) -> int:
    total_accumulator: int = 0
    current_index: int = 0
    while current_index <= x_val:
        temp: int = total_accumulator + current_index
        total_accumulator = temp
        current_index += 1
    return total_accumulator