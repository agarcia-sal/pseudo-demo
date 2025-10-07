def prime_length(data_input: str) -> bool:
    str_len: int = len(data_input)
    if str_len <= 1:
        return False
    divisor_candidate: int = 2
    while divisor_candidate < str_len:
        if str_len % divisor_candidate == 0:
            return False
        divisor_candidate += 1
    return True