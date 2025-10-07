def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len in (0, 1):
        return False
    divisor_counter: int = 2
    while divisor_counter < str_len:
        remainder_result: int = str_len - (str_len // divisor_counter) * divisor_counter
        if remainder_result == 0:
            return False
        divisor_counter += 1
    return True