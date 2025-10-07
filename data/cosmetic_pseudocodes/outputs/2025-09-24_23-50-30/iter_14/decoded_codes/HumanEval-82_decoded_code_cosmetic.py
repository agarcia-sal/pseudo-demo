def prime_length(input_string: str) -> bool:
    size: int = len(input_string)
    if size <= 1:
        return False
    divisor: int = 2
    while divisor < size:
        if size % divisor == 0:
            return False
        divisor += 1
    return True