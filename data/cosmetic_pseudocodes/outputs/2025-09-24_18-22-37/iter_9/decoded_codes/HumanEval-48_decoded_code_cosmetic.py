def is_palindrome(str_param: str) -> bool:
    len_value: int = len(str_param)
    idx_counter: int = 0
    while idx_counter < len_value:
        first_char: str = str_param[idx_counter]
        second_char: str = str_param[len_value - 1 - idx_counter]
        if first_char != second_char:
            return False
        idx_counter += 1
    return True