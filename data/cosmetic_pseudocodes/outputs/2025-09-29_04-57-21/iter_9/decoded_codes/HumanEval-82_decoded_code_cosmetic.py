def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if not (str_len > 1):
        return False
    candidate_divisor: int = 2
    while candidate_divisor < str_len:
        if str_len % candidate_divisor == 0:
            return False
        candidate_divisor += 1
    return True