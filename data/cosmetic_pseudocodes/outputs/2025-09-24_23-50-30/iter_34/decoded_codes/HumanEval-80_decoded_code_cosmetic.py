def is_happy(alpha_param: str) -> bool:
    pos_counter: int = 0
    str_len: int = len(alpha_param)
    if str_len <= 2:
        return False
    while pos_counter <= str_len - 3:
        a, b, c = alpha_param[pos_counter], alpha_param[pos_counter + 1], alpha_param[pos_counter + 2]
        if a == b or b == c or a == c:
            return False
        pos_counter += 1
    return True