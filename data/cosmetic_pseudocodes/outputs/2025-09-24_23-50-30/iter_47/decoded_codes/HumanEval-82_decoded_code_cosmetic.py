def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if not (str_len > 1):
        return False
    divisor_value: int = 2
    while divisor_value < str_len:
        if str_len % divisor_value == 0:
            return False
        divisor_value += 1
    return True