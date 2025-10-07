def prime_length(input_string: str) -> bool:
    length = len(input_string)
    if length in (0, 1):
        return False
    max_divisor = length - 1
    current_divisor = 2
    while current_divisor <= max_divisor:
        if length % current_divisor == 0:
            return False
        current_divisor += 1
    return True