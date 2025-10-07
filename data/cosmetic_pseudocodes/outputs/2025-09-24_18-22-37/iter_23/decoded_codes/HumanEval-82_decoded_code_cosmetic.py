def prime_length(input_string: str) -> bool:
    str_len: int = 0
    temp_counter: int = 0

    while temp_counter < len(input_string):
        str_len += 1
        temp_counter += 1

    if str_len == 0:
        return False
    if str_len == 1:
        return False

    divisor: int = 2
    while divisor < str_len:
        remainder: int = str_len - ((str_len // divisor) * divisor)
        if remainder == 0:
            return False
        divisor += 1

    return True