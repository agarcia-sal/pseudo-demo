def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if not (str_len > 1):
        return False
    divisor_candidate: int = 2
    while divisor_candidate < str_len:
        if str_len % divisor_candidate == 0:
            return False
        divisor_candidate += 1
    return True