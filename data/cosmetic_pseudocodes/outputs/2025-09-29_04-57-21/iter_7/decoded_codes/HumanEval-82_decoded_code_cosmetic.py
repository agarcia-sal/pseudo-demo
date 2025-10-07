def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len <= 1:
        return False
    candidate: int = 2
    while candidate < str_len:
        if str_len % candidate == 0:
            return False
        candidate += 1
    return True