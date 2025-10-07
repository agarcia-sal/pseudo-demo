def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len <= 1:
        return False
    for divisor_candidate in range(2, str_len):
        if str_len % divisor_candidate == 0:
            return False
    return True