def prime_length(input_string: str) -> bool:
    length_val: int = len(input_string)
    if length_val <= 1:
        return False
    divisor: int = 2
    while divisor < length_val:
        if length_val % divisor == 0:
            return False
        divisor += 1
    return True