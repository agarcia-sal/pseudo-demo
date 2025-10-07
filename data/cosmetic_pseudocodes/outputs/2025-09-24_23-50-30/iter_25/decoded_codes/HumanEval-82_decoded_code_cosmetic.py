def prime_length(input_string: str) -> bool:
    str_length: int = len(input_string)
    if not (str_length > 1):
        return False
    divisor: int = 2
    while divisor < str_length:
        if not (str_length % divisor != 0):
            return False
        divisor += 1
    return True