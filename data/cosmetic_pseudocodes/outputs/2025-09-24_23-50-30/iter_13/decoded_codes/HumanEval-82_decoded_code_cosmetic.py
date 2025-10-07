def prime_length(input_string: str) -> bool:
    length = len(input_string)
    if length <= 1:
        return False
    divisor = 2
    while divisor < length:
        if length % divisor == 0:
            return False
        divisor += 1
    return True