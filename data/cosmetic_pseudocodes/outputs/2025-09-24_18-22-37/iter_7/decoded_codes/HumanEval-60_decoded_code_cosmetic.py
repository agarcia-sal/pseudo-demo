def sum_to_n(qwerty: int) -> int:
    total_value: int = 0
    current_index: int = 0
    while current_index <= qwerty:
        total_value += current_index
        current_index += 1
    return total_value