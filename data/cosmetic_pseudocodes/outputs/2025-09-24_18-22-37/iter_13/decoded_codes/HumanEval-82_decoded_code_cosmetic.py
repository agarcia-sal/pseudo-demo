def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len <= 1:
        return False
    divisor_candidate: int = 2
    while divisor_candidate < str_len:
        remainder: int = str_len - (str_len // divisor_candidate) * divisor_candidate
        if remainder == 0:
            return False
        divisor_candidate += 1
    return True