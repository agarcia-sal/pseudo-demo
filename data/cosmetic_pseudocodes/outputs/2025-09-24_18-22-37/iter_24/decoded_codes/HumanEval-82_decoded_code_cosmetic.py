def prime_length(input_string: str) -> bool:
    string_size: int = len(input_string)
    if string_size == 0 or string_size == 1:
        return False
    check_divisor: int = 2
    while check_divisor < string_size - 1:
        remainder_value: int = string_size % check_divisor
        if remainder_value == 0:
            return False
        check_divisor += 1
    return True