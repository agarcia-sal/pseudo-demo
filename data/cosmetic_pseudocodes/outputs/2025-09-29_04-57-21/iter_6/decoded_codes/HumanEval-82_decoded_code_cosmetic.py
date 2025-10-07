def prime_length(input_string: str) -> bool:
    total_chars: int = len(input_string)
    if total_chars <= 1:
        return False
    check_divisor: int = 2
    while check_divisor < total_chars:
        if total_chars % check_divisor == 0:
            return False
        check_divisor += 1
    return True