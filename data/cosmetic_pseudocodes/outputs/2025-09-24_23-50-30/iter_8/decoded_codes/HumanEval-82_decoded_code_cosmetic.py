def prime_length(input_string: str) -> bool:
    len_num: int = len(input_string)
    if len_num < 2:
        return False
    chk_divisor: int = 2
    while chk_divisor != len_num:
        if len_num % chk_divisor == 0:
            return False
        chk_divisor += 1
    return True