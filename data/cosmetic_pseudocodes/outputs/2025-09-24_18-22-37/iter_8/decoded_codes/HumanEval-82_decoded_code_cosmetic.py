def prime_length(input_string_param: str) -> bool:
    str_len_var: int = len(input_string_param)
    if str_len_var <= 1:
        return False

    current_divisor: int = 2
    # The loop runs while current_divisor < str_len_var (as simplified from pseudocode)
    while current_divisor < str_len_var:
        if str_len_var % current_divisor == 0:
            return False
        current_divisor += 1

    return True