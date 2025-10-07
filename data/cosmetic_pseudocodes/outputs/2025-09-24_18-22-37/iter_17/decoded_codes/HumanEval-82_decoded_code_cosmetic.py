def prime_length(input_string: str) -> bool:
    total_chars: int = len(input_string)
    if total_chars <= 1:
        return False
    current_index: int = 2
    while current_index < total_chars:
        remainder_value: int = total_chars % current_index
        if remainder_value == 0:
            return False
        current_index += 1
    return True