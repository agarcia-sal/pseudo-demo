def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len <= 1:
        return False
    divisor: int = 2
    while divisor < str_len:
        if str_len % divisor == 0:
            return False
        divisor += 1
    return True